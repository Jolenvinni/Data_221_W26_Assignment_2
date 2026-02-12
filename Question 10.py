"""
Question 10
"""

def search_keyword_in_file(filename, keyword):

    results = []
    file = open(filename, "r", encoding="utf-8")
    for line_number, line in enumerate(file, start=1):

        #allows case insensitivity
        if keyword.lower() in line.lower():
            results.append(f"Line {line_number}: {line.strip()}")

            #print only 3
            if len(results) >= 3:
                break

    if not results:
        results = [f"No matches of '{keyword}' found in {filename}."]

    file.close()
    return (f"Keyword: {keyword}", results)


print(search_keyword_in_file("sample-file.txt", "lorem"))
print(search_keyword_in_file("sample-file.txt", "data"))