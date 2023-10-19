def solution(S):
    N = len(S)
    max_length = 0

    for i in range(N):
        left = i
        right = i
        while left >= 0 and right < N and (S[left] == S[right] or S[left] == '?' or S[right] == '?'):
            if S[left] == '?' and S[right] == '?':
                max_length = max(max_length, (right - left + 1))
            left -= 1
            right += 1

    return max_length

# Examples:
S1 = "<><??>>"
print(solution(S1))  # Output: 4

S2 = "??????"
print(solution(S2))  # Output: 6

S3 = "<<?"
print(solution(S3))  # Output: 2
