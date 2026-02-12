"""
Question 3

In this task, you will identify lines that are nearly identical after basic normalization.
Two lines are considered near-duplicates if they become identical after converting to lower-
case and removing all whitespace and punctuation characters.
Using sample-file.txt:
• Identify sets of near-duplicate lines.
• Print the number of such sets.
• Print the first two sets you find, including line numbers and original lines

"""


with open("sample-file.txt", "r") as file:
    duplicate_lines = {}

    # 1.) Identify sets of near-duplicate lines.
    for line_number, line in enumerate(file, start=1):
        original_line = line.rstrip("\n")
        cleaned_text_line = ""

        # simplify the text lines from the file
        for char in original_line:
            if char.isalnum():
                cleaned_text_line += char.lower()

        # ignore empty lines
        if not cleaned_text_line:
            continue

        duplicate_lines.setdefault(cleaned_text_line, []).append(
            (line_number, original_line)
        )

# 2.) Print the number of such sets.
duplicate_sets = [
    occurrences
    for occurrences in duplicate_lines.values()
    if len(occurrences) > 1
]
print(f"Number of duplicate sets: {len(duplicate_sets)}")

# 3.) Print the first two sets you find, including line numbers and original lines.
print("\nFirst two duplicate sets:\n")

for i, occurrences in enumerate(duplicate_sets[:2], start=1):
    print(f"Set {i}")
    for line_number, original_line in occurrences:
        print(f"Line {line_number}: {original_line}")
    print()


