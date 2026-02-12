"""
Question 2

In this question, you will analyze pairs of consecutive words (called bigrams) from a text file.
Using sample-file.txt:
• Read the file and split it into tokens (words).
• Convert all tokens to lowercase.
• Remove punctuation characters from the beginning and end of each token.
• Keep only tokens that contain at least two alphabetic characters.
• Construct bigrams (pairs of consecutive cleaned words).
• Count the frequency of each bigram.
• Print the 5 most frequent bigrams in descending order in the format: word1 word2 ->
count.

"""


#Makes removal of punctuations easier.
import string


# 1.) Read the file and split it into tokens.
with open("sample-file.txt", "r") as file:
    file_text = file.read()

tokens = file_text.split()


# 2.) Convert all tokens to lowercase.
lowercase_tokens = [token.lower() for token in tokens]


# 3.) Remove punctuation characters from each token.
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


# 5.) Construct bigrams (pairs of consecutive cleaned words).
bigram_tokens = []

for token in range(len(clean_lowercase_nontrivial_tokens) - 1):
    bigram_tokens.append(
        f"{clean_lowercase_nontrivial_tokens[token]} {clean_lowercase_nontrivial_tokens[token + 1]}"
    )


# 6.) Count the frequency of each bigram.
bigram_count = {}
for token in bigram_tokens:
    if token in bigram_count:
        bigram_count[token] += 1
    else:
        bigram_count[token] = 1


# 7.) Print the 5 most frequent bigrams in descending order in the format: word1 word2 ->
# count.
print(sorted(bigram_count.items(), key=lambda x: x[1], reverse=True)[:5])