import csv

# Read text from txt file
with open("date.txt", "r") as file:
    text = file.read().strip()

# Search for text in CSV file
with open("dat_als.csv", "r") as file:
    reader = csv.reader(file)
    for row_idx, row in enumerate(reader):
        try:
            col_idx = row.index(text.lower().strip())
            print(f"Found '{text}' at cell ({row_idx+1}, {col_idx+1})")
            break  # Stop searching after finding the first match
        except ValueError:
            pass  # Text not found in this row

    else:
        print(f"Text '{text}' not found in CSV file")