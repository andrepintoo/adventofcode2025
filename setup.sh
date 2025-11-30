#!/bin/bash

usage() {
cat << EOF
usage: $(basename "$0") [OPTIONS]

Description: This script automates getting a certain day's input content and creates the folder with the template files inside a template/ folder. Before using, set AOC_SESSION, and TEMPLATE_PATH (if needed) in a .env file inside the base folder.

Options:
	-h, --help	Show this help message and exit
	-d, --day DAY	Specify the day number (optional - default value will be the current date)
	-y, --year YEAR	Specify the year (optional - default value will be the current year)
	-t, --template 	Specify if a template path is needed or not. Possible values: 'no', 'yes', 0, 1. 
			Default value: 'no'

Examples:
	$0
	$0 -d 5
	$0 --day 2 --year 2024
	$0 -t no
EOF
	exit 0
}

DAY=$(date +%d)
YEAR=$(date +%Y)
TEMPLATE=false

# handle arguments
while [[ $# -gt 0 ]]; do
	case "$1" in
		-h|--help)
			usage
			;;
		-d|--day)
			if [[ -n "$2" && "$2" =~ ^[0-9]+$ ]]; then
				DAY=$(printf "%02d" $2)
				# go to the next argument
				shift
			else
				echo "Error: Please provide a valid day number."
				usage
			fi
			;;
		-y|--year)
			if [[ -n "$2" && "$2" =~ ^[0-9]{4}$ ]]; then
				YEAR="$2"
				shift
			else
				echo "Error: Please provide a valid year (4 digits)."
				usage
			fi
			;;
		-t|--template)
			# if it's a number not in [0,1]
			# or if it's not a string in [yes, no]
			# then reject
			if [[ "$2" =~ '^[0-9]+$' ]] && [[ "$2" != 0 ]] && [[ "$2" != 1 ]] && \  
			   [[ "${2,,}" =~ 'yes' ]] && [[ "${2,,}" =~ 'no' ]]; then
				echo "Error: for the template usage, please input either a positive response ['yes', 1] or a negative one ['no', 0]"
				shift
			fi

			if [[ "$2" == "1" ]] || [[ "$2" == "yes" ]]; then
				TEMPLATE=true
			fi
			shift
			;;
		*)
			echo "Error: Unknown option: $1"
			usage
			;;
	esac
	shift
done

if [ -d "$DAY" ]; then
	echo "error: $DAY directory already exists"
	exit 1
fi

CURR_YEAR=$(date +%Y)
CURR_DAY=$(date +%d)

if [ "$YEAR" -gt "$CURR_YEAR" ] || ([ "$YEAR" -eq "$CURR_YEAR" ] && [ "$DAY" -gt "$CURR_DAY" ]); then
	echo "error: cannot put a date in the future"
	exit 1
fi

set -a 
source .env 
set +a

if [ -z "$AOC_SESSION" ]; then
	echo "error: set the aoc session cookie in a .env file"
	echo "usage: AOC_SESSION=<xx>"
	exit 1
fi

if [ "$TEMPLATE" = true ] && [ -z "$TEMPLATE_PATH" ]; then
	echo "error: set a path to the template folder in your .env file first"
	echo "usage: TEMPLATE_PATH=template/"
	exit 1
fi

# check if the directory exists
if [ "$TEMPLATE" = true ] && [ ! -d "$TEMPLATE_PATH" ]; then
	echo "Error: directory provided ($TEMPLATE_PATH) does not exist"
	exit 1
fi

# create the folder if it doesn't exist
mkdir -p "$DAY"
if [ "$TEMPLATE" = true ]; then
	cp -r "$TEMPLATE_PATH"/* "$DAY/"
fi
# removes leading zeroes from days < 10 (03 --> 3...)
URL_DAY=$(echo "$DAY" | bc)
echo "ok: created folder '$DAY/'"
output_file="$DAY/input.txt"
: > $output_file

# fetch input file
status_code=$(curl -s -w "%{http_code}" \
	-H "Cookie: session=$AOC_SESSION" \
	-o "$output_file" \
	"https://adventofcode.com/$YEAR/day/$URL_DAY/input")

if head -n 1 "$output_file" | grep -q "Puzzle inputs differ by user" ; then
	echo "error: authentication failed - check if your session cookie is still valid"
	exit 1
fi

case "$status_code" in
	200)
		echo "ok: status code 200" ;;
	*)
		echo "error: status code $status_code"
		exit 1;;
esac

if [ -s $output_file ]; then
	echo "successfully dowloaded input for $DAY/dec/$YEAR"
else
	echo "failed to download input for day $DAY/dec/$YEAR"
	exit 1
fi

echo "Done."

