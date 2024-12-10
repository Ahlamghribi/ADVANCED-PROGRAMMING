import os

def filter_subtractions(directory="."):
    output_file = "filtered_subtractions.csv"
    with open(output_file, "w") as output:
        for filename in os.listdir(directory):
            if filename.startswith("operations_file_") and filename.endswith(".csv"):
                with open(filename, "r") as file:
                    for line in file:
                        parts = line.split(",")
                        if parts[0] == "SUBTRACTION":
                            operands = parts[1].split("-")
                            try:
                                operand1 = int(operands[0])
                                operand2 = int(operands[1])
                                if operand1 < 21 and 0 <= operand2 < 10:
                                    output.write(line)
                            except ValueError:
                                continue   

    print(f"Filtered subtractions saved to {output_file}.")

if __name__ == "__main__":
    filter_subtractions()
