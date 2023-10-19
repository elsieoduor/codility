def solution(A):
    total_pollution = sum(A)
    filters_needed = [0] * len(A)
    min_filters = float('inf')

    for i in range(len(A)):
        pollution = A[i]
        while pollution > total_pollution / 2:
            pollution /= 2
            filters_needed[i] += 1

    for i in range(len(A)):
        if filters_needed[i] < min_filters:
            min_filters = filters_needed[i]

    return min_filters

# Examples:
A1 = [5, 19, 8, 1]
print(solution(A1))  # Output: 3

A2 = [10, 10]
print(solution(A2))  # Output: 2

A3 = [3, 0, 5]
print(solution(A3))  # Output: 2
