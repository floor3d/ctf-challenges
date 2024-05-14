#!/bin/bash

# Check if the input file is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

# Input file
input_file="$1"

temp_file="answer.txt"

# Counter to keep track of line numbers
line_number=1

# Read each line from the input file
while IFS= read -r line; do
  # Check if the line number is odd
  if (( line_number % 2 != 1 )); then
    # Reverse the line
    echo "$line" | rev >> "$temp_file"
  else
    # Keep the line as is
    echo "$line" >> "$temp_file"
  fi
  # Increment the line number
  ((line_number++))
done < "$input_file"

echo "Every other line in $input_file has been reversed."

