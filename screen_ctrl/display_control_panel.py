import re

def extract_numbers_from_line(line_number):
    try:
        with open('../database/db.txt', 'r') as file:
            lines = file.readlines()
            if line_number <= 0 or line_number > len(lines):
                raise ValueError("Line number out of range.")
            
            line = lines[line_number - 1]
            numbers = re.findall(r'\d+\.\d+|\d+', line)
            
            return [float(num) if '.' in num else int(num) for num in numbers]
    
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    
    return []