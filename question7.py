def solution(S):
    # Check if the length of the string is valid
    if len(S) != 11:
        return 0

    # Check the format of the string
    for i in range(3):
        if S[i] != '-' or S[i+4] != '-' or not S[i+1:i+4].isdigit():
            return 0

    # Check if the last segment contains exactly three digits
    if not S[8:].isdigit() or len(S[8:]) != 3:
        return 0

    return 1

# Examples:
S1 = "123-123-123"
print(solution(S1))  # Output: 1

S2 = "123 123 123"
print(solution(S2))  # Output: 0

S3 = "123-123-1234"
print(solution(S3))  # Output: 0

S4 = "001-501-511"
print(solution(S4))  # Output: 1

S5 = "123-abc-123"
print(solution(S5))  # Output: 0
