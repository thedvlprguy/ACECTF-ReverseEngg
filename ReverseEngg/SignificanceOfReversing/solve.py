# Open the input file (original file) and the output file (reversed file)
input_filename = "/home/thedvlprguy/ACECTF/ReverseEngg/SignificanceOfReversing/Reverseme.png"  # Source file name
output_filename = "reversed_file.LEF"  # Reversed file name

with open(input_filename, 'rb') as infile:
    # Read the entire content of the file and reverse the data
    data = infile.read()

# Reverse the byte data
reversed_data = data[::-1]

# Write the reversed data to the output file
with open(output_filename, 'wb') as outfile:
    outfile.write(reversed_data)

print(f"File has been reversed and saved to {output_filename}")


