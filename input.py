import sys

def read_input_file(file_path):
    """Reads numbers from a file and returns them as a list of floats."""
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    data.append(float(line))
                except ValueError:
                    print(f"Warning: Skipping invalid data '{line}'")
    return data