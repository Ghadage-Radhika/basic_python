"""
1. Sum of Even Numbers
Write a Python program that calculates the sum of all even numbers between 1 and 100.
Example Input:
No input required.
Example Output:
2550
"""
def sum_of_even_numbers():
    num = 1
    total = 0
    while num <= 100:
        if num % 2 == 0:
            total += num
        num += 1
    return total
print("Sum of Even Numbers: ",sum_of_even_numbers())
