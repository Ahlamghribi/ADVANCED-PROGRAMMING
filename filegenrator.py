import random
import datetime

def generate_files(file_count=5, lines_per_file=250_000):
    operations = ["SUBTRACTION", "ADDITION", "MULTIPLICATION", "DIVISION"]
    usernames = [f"anon{random.randint(1000, 9999)}" for _ in range(10)]
    
    for file_idx in range(file_count):
        filename = f"operations_file_{file_idx+1}.csv"
        with open(filename, "w") as f:
            for _ in range(lines_per_file):
                operation = random.choice(operations)
                operand1 = random.randint(1, 100)
                operand2 = random.randint(1, 100)
                if operation == "SUBTRACTION":
                    result = operand1 - operand2
                elif operation == "ADDITION":
                    result = operand1 + operand2
                elif operation == "MULTIPLICATION":
                    result = operand1 * operand2
                elif operation == "DIVISION":
                    result = operand1 / operand2 if operand2 != 0 else 0
                user = random.choice(usernames)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                line = f"{operation},{operand1}-{operand2},{result},{random.randint(10000, 99999)},{user},\"{timestamp}\"\n"
                f.write(line)

    print(f"{file_count} files generated successfully.")

if __name__ == "__main__":
    generate_files()
