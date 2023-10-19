import re

def solution(S):
    sentences = re.split(r'[.!?]', S)
    max_word_count = 0
    max_sentence = ''

    for sentence in sentences:
        words = sentence.split()
        word_count = len([word for word in words if any(c.isalpha() for c in word)])  # Count words with at least one letter
        if word_count > max_word_count:
            max_word_count = word_count
            max_sentence = sentence.strip()  # Remove leading/trailing spaces

    return max_sentence

# Example:
S = "You would like to find the sentence containing the largest number of words in some given text. The text is specified as a string S consisting of N characters: letters, spaces, dots (.), question marks (?) and exclamation marks (!). The text can be divided into sentences by splitting it at dots, question marks and exclamation marks. A sentence can be divided into words by splitting it at spaces. A sentence without words is valid, but a valid word must contain at least one letter."
result = solution(S)
print(result)
