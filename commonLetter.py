def solution(S):
    N = len(S)
    M = len(S[0])

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if S[i][k] == S[j][k]:
                    return [i, j, k]

    return []

# Examples:
S1 = ["abc", "bca", "dbe"]
print(solution(S1))  # Output: [0, 2, 1] or [2, 0, 1]

S2 = ["zzzz", "ferz", "zdsr", "fgtd"]
print(solution(S2))  # Output: [0, 1, 3] or [1, 0, 3]

S3 = ["gr", "sd", "rg"]
print(solution(S3))  # Output: []

S4 = ["bdafg", "ceagi"]
print(solution(S4))  # Output: [0, 1, 2]
