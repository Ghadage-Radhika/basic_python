"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""
n = int(input("Total Numbers (n): "))
arr = list(map(int, input("Enter Array: ").split()))

e_sum = n * (n + 1) // 2  # Sum of first n natural numbers
a_sum = 0

index = 0
while index < len(arr):
    a_sum += arr[index]
    index += 1

missing_num = e_sum - a_sum
print("The missing number is:", missing_num)
