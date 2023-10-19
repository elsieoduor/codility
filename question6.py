import re

def solution(S):
    sentences = re.split(r'[.!?]', S)
    max_words = 0

    for sentence in sentences:
        words = sentence.split()
        word_count = len(words)
        max_words = max(max_words, word_count)

    return max_words

# Examples:
S1 = "We test coders. Give us a try?"
print(solution(S1))  # Output: 4

S2 = "Forget CVs..Save time . x x"
print(solution(S2))  # Output: 2
