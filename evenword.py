def solution(S):
    letter_count = {}  # Dictionary to store the count of each letter

    # Count the frequency of each letter in the string
    for letter in S:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    # Initialize the count of letters to delete
    letters_to_delete = 0

    # Check the frequency of each letter and count letters to delete
    for count in letter_count.values():
        if count % 2 == 1:
            letters_to_delete += 1

    return letters_to_delete

# Examples:
S1 = "acbcbba"
print(solution(S1))  # Output: 1

S2 = "axxaxa"
print(solution(S2)) 
