def solution(A, S):
    count = 0

    for recipe in A:
        ingredients_required = {}
        for ingredient in recipe:
            ingredients_required[ingredient] = ingredients_required.get(ingredient, 0) + 1

        can_prepare = True
        for ingredient, count_required in ingredients_required.items():
            if ingredient not in S or S.count(ingredient) < count_required:
                can_prepare = False
                break

        if can_prepare:
            count += 1

    return count

# Examples:
A1 = ["toast", "bread", "breada", "cheese"]
S1 = "abcdeeehrs"
print(solution(A1, S1))  # Output: 2

A2 = ["az", "azz", "zza", "zzz", "zzzz"]
S2 = "azzz"
print(solution(A2, S2))  # Output: 4
