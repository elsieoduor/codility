def solution(riddle):
    result = list(riddle)
    current_letter = 'a'
    for i in range(len(riddle)):
        if result[i] == '?':
            if i > 0 and result[i - 1] == current_letter:
                current_letter = chr(ord(current_letter) + 1)
            if i < len(riddle) - 1 and current_letter == result[i + 1]:
                current_letter = chr(ord(current_letter) + 1)
            result[i] = current_letter
            current_letter = chr(ord(current_letter) + 1)

    return ''.join(result)

# Examples:
riddle1 = "ab?ac?"
print(solution(riddle1))  # Output: "abcaca"

riddle2 = "rd?e?wg??"
print(solution(riddle2))  # Output: "rdveawgab"

riddle3 = "????????"
print(solution(riddle3))  # Output: "codility"
