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

"""
2. Reverse a String
Write a Python function that takes a string as input and returns the string reversed.
Example Input:
"hello"
Example Output:
"olleh"
"""
def reverse_string(s):
    reversed = ""
    i = len(s) - 1
    while i >= 0:
        reversed += s[i]
        i -= 1
    return reversed
input = input("Enter a string: ")
print("Reversed string:", reverse_string(input))

"""
3. Factorial of a Number
Write a Python program that calculates the factorial of a number (n!). For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
Example Input:
5
Example Output:
120
"""
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))
