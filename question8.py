def solution(S):
    S = list(S)
    left, right = 0, len(S) - 1

    while left < right:
        if S[left] == '?' and S[right] == '?':
            S[left] = S[right] = 'a'
        elif S[left] == '?' and S[right] != '?':
            S[left] = S[right]
        elif S[left] != '?' and S[right] == '?':
            S[right] = S[left]
        elif S[left] != S[right]:
            return "NO"
        left += 1
        right -= 1

    if left == right and S[left] == '?':
        S[left] = 'a'

    return ''.join(S)

# Examples:
S1 = "?ab??a"
print(solution(S1))  # Output: "aabbaa"

S2 = "bab??a"
print(solution(S2))  # Output: "NO"

S3 = "?a?"
print(solution(S3))  # Output: "aaa" or "zaz" (multiple valid answers)
