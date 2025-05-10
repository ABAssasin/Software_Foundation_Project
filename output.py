import sys

def write_output_file(output_path, total, average):
    """Writes the results to an output file."""
    with open(output_path, 'w') as file:
        file.write(f"Sum of numbers: {total}\n")
        file.write(f"Average of numbers: {average}\n")