from collections import Counter

def solution(S, L, K):
    max_copies = 0
    letter_count = Counter(S)

    for word in L:
        word_count = Counter(word)
        min_copies = float('inf')

        for letter, count in word_count.items():
            if letter not in letter_count:
                min_copies = 0
                break
            min_copies = min(min_copies, letter_count[letter] // count)

        max_copies = max(max_copies, min_copies * K)

    return max_copies

# Examples:
S1 = "BILLOBILLOLLOBBI"
L1 = ["BILL", "BOB"]
K1 = 1
print(solution(S1, L1, K1))  # Output: 3

S2 = "CAT"
L2 = ["ILOVEMYDOG", "CATS"]
K2 = 1
print(solution(S2, L2, K2))  # Output: 0

S3 = "ABCDXYZ"
L3 = ["ABCD", "XYZ"]
K3 = 1
print(solution(S3, L3, K3))  # Output: 1
