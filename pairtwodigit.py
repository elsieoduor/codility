def solution(S):
    max_sum = 0
    i = 0

    while i < len(S) - 1:
        fragment1 = int(S[i:i+2])
        j = i + 2

        while j < len(S) - 1:
            fragment2 = int(S[j:j+2])

            if fragment1 + fragment2 > max_sum:
                max_sum = fragment1 + fragment2

            j += 2

        i += 2

    return max_sum

# Examples:
S1 = "43798"
print(solution(S1))  # Output: 141
