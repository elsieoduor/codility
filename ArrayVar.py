def solution(A):
    max_multiple_of_4 = float("-inf")  # Initialize as negative infinity

    for num in A:
        if num % 4 == 0 and num > max_multiple_of_4:
            max_multiple_of_4 = num

    return max_multiple_of_4

# Example:
A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
result = solution(A)
print(result)  # Output: 84
