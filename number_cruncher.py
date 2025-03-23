def process_numbers():
    total = 0
    try:
        with open("numbers.txt", "r") as infile:
            for line in infile:
                # Strip whitespace and convert to float
                total += float(line.strip())
        
        with open("sum.txt", "w") as outfile:
            outfile.write(f"Total sum: {total}\n")
            
    except FileNotFoundError:
        print("Error: 'numbers.txt' not found. Please create the file with numbers.")
    except ValueError as e:
        print("Error: Found a non-numeric value. Please ensure all lines contain valid numbers.")
    finally:
        print("File processing complete.")

if __name__ == "__main__":
    process_numbers()
