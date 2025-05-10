import sys
from output import write_output_file
from calculation import perform_calculations
from input import read_input_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python data_processing.py <input_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output.txt"

    print(f"\nReading data from: {input_file}")
    data = read_input_file(input_file)
    
    if len(data) < 3:
        print("Error: The input file must contain at least 3 numbers.")
        sys.exit(1)

    print(f"Data read: {data}")

    total, average = perform_calculations(data)

    print("\nCalculations performed:")
    print(f" - Sum = {total}")
    print(f" - Average = {average}")

    write_output_file(output_file, total, average)

    print(f"\nResults have been saved to file: {output_file}")

if __name__ == "__main__":
    main()