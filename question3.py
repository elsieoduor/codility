def solution(A, B):
    N = len(A)
    count = 0
    
    for i in range(N):
        a_count = [0] * 26
        b_count = [0] * 26
        diff_count = 0
        
        for j in range(i, N):
            # Update the letter count for A and B
            a_count[ord(A[j]) - ord('a')] += 1
            b_count[ord(B[j]) - ord('a')] += 1
            
            # Compare letter counts
            for k in range(26):
                if a_count[k] != b_count[k]:
                    diff_count += 1
            
            # If there are no differences, we have a corresponding fragment
            if diff_count == 0:
                count += 1

    return count

# Examples:
print(solution("dBacaAA", "caBdaaA"))  # Output: 5
print(solution("zzzX", "zzzX"))  # Output: 10
print(solution("abc", "ABC"))  # Output: 0

