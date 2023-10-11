#!/bin/bash

input_file="names.txt"
output_file="organized_names.txt"

if [ "$#" -eq 2 ]; then
    input_file="$1"
    output_file="$2"
elif [ "$#" -ne 0 ]; then
    echo "Usage: $0 [input_file output_file]"
    exit 1
fi

# Check if the output file exists; if not, create it
if [ ! -f "$output_file" ]; then
    touch "$output_file"
fi

awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            result[i] = $i;
        } else {
            result[i] = result[i] " " $i;
        }
    }
}
END {
    for (i = 1; i <= NF; i++) {
        print result[i];
    }
}
' "$input_file" > "$output_file"
