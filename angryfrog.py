def solution(blocks):
    max_distance = 0

    for i in range(len(blocks)):
        left, right = i, i

        while left > 0 and blocks[left] >= blocks[left - 1]:
            left -= 1

        while right < len(blocks) - 1 and blocks[right] >= blocks[right + 1]:
            right += 1

        max_distance = max(max_distance, right - left + 1)

    return max_distance

# Examples:
blocks1 = [2, 6, 8, 5]
print(solution(blocks1))  # Output: 3

blocks2 = [1, 5, 5, 2, 6]
print(solution(blocks2))  # Output: 4

blocks3 = [1, 1]
print(solution(blocks3))  # Output: 2
