#!/bin/bash

output_file='valid_numbers.txt'

# Check if the input file exists
if [ ! -f "$output_file" ]; then
    echo "Input file '$output_file' not found. Please create it and add phone numbers for testing."
    exit 1
fi

# Use grep to search for valid phone numbers and print the results
grep -P '^\d{3}-\d{3}-\d{4}$|^\(\d{3}\) \d{3}-\d{4}$' "$output_file"
