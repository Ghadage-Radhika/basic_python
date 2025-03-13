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

"""
4. Check if a Number is Prime
Write a Python function that checks if a given number is prime.
Example Input:
7
Example Output:
True
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print(f"Is {num} a prime number? {is_prime(num)}")

"""
5. Count Vowels in a String
Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string.
Example Input:
"programming"
Example Output:
3 
"""
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = input("Enter a string: ")
print(f"Number of vowels in '{s}' is: {count_vowels(s)}")

"""
6. Fibonacci Series
Write a Python program that prints the Fibonacci series up to the nth number, where n is provided by the user.
Example Input:
5
Example Output:
0 1 1 2 3
"""
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
n = int(input("Enter the number of terms: "))
fibonacci(n)

"""
7. Find the Largest Number in a List
Write a Python program that finds and prints the largest number from a given list of integers.
Example Input:
[10, 30, 25, 60, 12]
Example Output:
60
"""
def find_largest(arr):
    return max(arr)
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Largest number:", find_largest(arr))

"""
8. Check Palindrome
Write a Python function that checks whether a given string is a palindrome (reads the same backward as forward).
Example Input:
"madam"
Example Output:
True
"""
def is_palindrome(s):
    return s == s[::-1]
s = input("Enter a string: ")
print("Palindrome:", is_palindrome(s))

"""
9. Multiplication Table
Write a Python program that generates the multiplication table of a number up to 10.
Example Input:
4
Example Output:
    4 * 1 = 4 
    4 * 2 = 8 
    4 * 3 = 12 
    4 * 4 = 16 
    4 * 5 = 20 
    4 * 6 = 24 
    4 * 7 = 28 
    4 * 8 = 32 
    4 * 9 = 36 
    4 * 10 = 40
"""
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
num = int(input("Enter a number: "))
multiplication_table(num)

"""
10. Count Digits in a Number
Write a Python function that counts the number of digits in a given number.
Example Input:
12345
Example Output:
5
"""
def count_digits(num):
    return len(str(num))
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))

"""
11. Sum of Digits
Write a Python program that calculates the sum of the digits in a number.
Example Input:
1234
Example Output:
10
"""
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

"""
12. Find the Second Largest Number
Write a Python function that finds the second-largest number in a list of numbers.
Example Input:
[10, 20, 4, 45, 99]
Example Output:
45
"""
def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2] if len(arr) > 1 else "Not enough elements"
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Second largest number:", second_largest(arr))

"""
13. Convert Celsius to Fahrenheit
Write a Python program that converts a temperature in Celsius to Fahrenheit.
Example Input:
25
Example Output:
77.0
"""
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

"""
14. Check if a Number is Armstrong
Write a Python function to check whether a number is an Armstrong number. An Armstrong number is one where the sum of the cubes of its digits equals the number itself (for a 3-digit number).
Example Input:
153
Example Output:
True
"""
def is_armstrong(num):
    return sum(int(digit) ** len(str(num)) for digit in str(num)) == num
num = int(input("Enter a number: "))
print("Armstrong Number:", is_armstrong(num))

"""
15. Find the Common Elements in Two Lists
Write a Python program that finds the common elements between two lists.
Example Input:
[1, 2, 3, 4]
[3, 4, 5, 6]
Example Output:
[3, 4]
"""
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Common elements:", common_elements(list1, list2))

"""
16. Remove Duplicates from a List
Write a Python program that removes all duplicate elements from a list and returns the list with unique elements only.
Example Input:
[1, 2, 2, 3, 4, 4, 5]
Example Output:
[1, 2, 3, 4, 5]
"""
def remove_duplicates(arr):
    return list(set(arr))
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Unique elements:", remove_duplicates(arr))

"""
17. Sum of Odd Numbers
Write a Python program that calculates the sum of all odd numbers between 1 and 100.
Example Input:
No input required.
Example Output:
2500
"""
def sum_of_odds():
    num, sum_odd = 1, 0
    while num <= 100:
        sum_odd += num
        num += 2
    return sum_odd
print("Sum of odd numbers:", sum_of_odds())

"""
18. Check for Leap Year
Write a Python function that checks if a given year is a leap year.
Example Input:
2024
Example Output:
True
"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  
            else:
                return False  
        else:
            return True  
    else:
        return False  
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")

"""
19. Count Words in a Sentence
Write a Python program that counts the number of words in a given sentence.
Example Input:
"Python is fun"
Example Output:
4 
"""
def count_words(sentence):
    words = sentence.strip().split() 
    return len(words)
sentence = input("Enter a sentence: ").strip()
if sentence:
    print(f"Word count: {count_words(sentence)}")
else:
    print("No words entered.")
