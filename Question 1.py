"""
Question 1

In this question, you will practice reading a text file and performing basic text preprocessing
before computing word statistics.
Using sample-file.txt:
• Read the file and split it into tokens (words).
• Convert all tokens to lowercase.
• Remove punctuation characters from the beginning and end of each token.
• Keep only tokens that contain at least two alphabetic characters.
• Count word frequencies and print the 10 most frequent words in descending order in the
format: word -> count.

"""


#Makes removal of punctuations easier.
import string


# 1.) Read the file and split it into tokens.
with open("sample-file.txt", "r") as file:
    file_text = file.read()

tokens = file_text.split()


# 2.) Convert all tokens to lowercase.
lowercase_tokens = [token.lower() for token in tokens]


# 3.) Remove punctuation characters from the beginning and end of each token.
clean_lowercase_tokens =[]

for token in lowercase_tokens:
    new_token = ""

    for letter in token:
        if letter not in string.punctuation:
            new_token += letter

    clean_lowercase_tokens.append(new_token)

# 4.) Keep only tokens that contain at least two alphabetic characters.
clean_lowercase_nontrivial_tokens = []

for token in clean_lowercase_tokens:
    if len(token) >= 2:
        clean_lowercase_nontrivial_tokens.append(token)


# 5.) Count word frequencies and print the 10 most frequent words in descending order in the
# format: word -> count.

#Word counter.
word_count = {}
for token in clean_lowercase_nontrivial_tokens:
    if token in word_count:
        word_count[token] += 1
    else:
        word_count[token] = 1


#Filtered output.
print(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10])
