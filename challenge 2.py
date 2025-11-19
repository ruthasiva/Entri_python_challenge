# Problem Statement:
# Write a Python program to print all prime numbers within a given range.

# Input:

# Two integers: start and end

# Output:

# Print all prime numbers between start and end (inclusive).

# If no prime numbers exist, print "No primes found".


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

found = False

for num in range(start, end + 1):

    if num < 2:  
        continue

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        found = True

if not found:
    print("No primes found")
