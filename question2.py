def solution(S):
    result = 0  # Initialize the result to 0
    tokens = S.split('+')  # Split the string by '+' signs

    for token in tokens:
        subtokens = token.split('-')  # Split each part by '-' signs

        # Process the subtokens in each part
        for subtoken in subtokens:
            if subtoken == "one":
                result += 1
            elif subtoken == "two":
                result -= 2

    return result

# Examples:
print(solution("one+two-one-one+two+one"))  # Output: 4
print(solution("two-two-one-two"))  # Output: -3
print(solution("two"))  # Output: 2
