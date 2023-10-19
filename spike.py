#Pseudocode
#1.Initialize two variables to store the length of A and count of longest spike
#2.Use a for loop to iterate through the array, starting from the first to last element.
#3.For element at x, we will try to find the longest spike that starts at this element.
#4.Initialize two variables, increasing_part and decreasing_part, both set to 1.
#5.Start two while loops with the variable y set to the current index x.
#6.In the first while loop, we increment the increasing_part by 1 and move to the next element by increasing y.
#7.After finding increasing part, we reset the index y to its original.
#8.In the second while loop, we increment the decreasing_part by 1 and move to the next element by increasing y.
#9.Find the total length of the combined (starting at current by adding the lengths of the increasing and decreasing)
#10.Return the longest_spike

def solution(A):
  longest_spike = 0
  n = len(A)
  for x in range(n):
        increase = 1
        decrease = 1
        j = x

        # Calculating the increasing part
        while j < n - 1 and A[j] < A[j + 1]:
            increase += 1
            j += 1
        # Calculate the decreasing part
        while j < n - 1 and A[j] > A[j + 1]:
            decrease += 1
            j += 1
        # Calculate the length of both
        length = increase + decrease - 1

        # Update the longest spike length
        longest_spike = max(longest_spike, length)

  return longest_spike

A1 = [1, 2]
print(solution(A1))  

A2 = [2, 5, 3, 2, 4, 1]
print(solution(A2))  

A3 = [2, 3, 3, 2, 2, 2, 1]
print(solution(A3)) 