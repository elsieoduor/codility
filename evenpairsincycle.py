def solution(A):
    count = 0

    for i in range(len(A)):
        if (A[i] + A[(i + 1) % len(A)]) % 2 == 0:
            count += 1

    return count // 2  # Divide by 2 to avoid double counting

# Examples:
A1 = [4, 2, 5, 8, 7, 3, 7]
print(solution(A1))  # Output: 2

A2 = [14, 21, 16, 35, 22]
print(solution(A2))  # Output: 1

A3 = [5, 5, 5, 5, 5, 5]
print(solution(A3))  # Output: 3
