def analyze_numbers():
    import os

    input_file = input("Enter the name of the input file (e.g., numbers.txt): ")

    while not os.path.isfile(input_file):
        print(f"Error: '{input_file}' does not exist.")
        retry = input("Do you want to enter a new file name? (y/n): ").strip().lower()
        if retry == 'y':
            input_file = input("Enter a new file name: ")
        else:
            print("Exiting program.")
            return

    total = 0
    count = 0
    minimum = None
    maximum = None

    try:
        with open(input_file, "r") as infile, open("error_log.txt", "w") as error_log:
            for line_num, line in enumerate(infile, 1):
                stripped = line.strip()
                try:
                    num = float(stripped)
                    total += num
                    count += 1
                    if minimum is None or num < minimum:
                        minimum = num
                    if maximum is None or num > maximum:
                        maximum = num
                except ValueError:
                    error_log.write(f"Line {line_num}: Invalid number '{stripped}'\n")

        if count > 0:
            average = total / count
        else:
            average = 0

        with open("report.txt", "w") as report:
            report.write("Report:\n")
            report.write("-------\n")
            report.write(f"Count: {count}\n")
            report.write(f"Sum: {total}\n")
            report.write(f"Average: {average}\n")
            report.write(f"Minimum: {minimum}\n")
            report.write(f"Maximum: {maximum}\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File analysis complete.")

if __name__ == "__main__":
    analyze_numbers()
