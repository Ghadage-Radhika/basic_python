"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
start = int(input("Start number: "))
end = int(input("End number: "))

print(f"Prime numbers in the range ({start} - {end}) :", end=" ")
num = start
while num <= end:
    if num > 1:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num, end=", ")
    num += 1
