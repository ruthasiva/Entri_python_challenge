# Problem Statement:
# Write a Python program to check whether a given number is an Armstrong number or not.

# 👉 A number is called an Armstrong number (also known as a narcissistic number) if the sum of its digits each raised to the power of the number of digits is equal to the number itself.

# Examples:

# 153 → 1³ + 5³ + 3³ = 153 ✅ (Armstrong)

# 9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅ (Armstrong)

# 123 → 1³ + 2³ + 3³ = 36 ❌ (Not Armstrong)

# Input:

# A single integer n

# Output:

# Print "Armstrong Number" if it is, otherwise "Not Armstrong Number"

# ⚡ Challenge Extension (Optional):

# Write a program that prints all Armstrong numbers in a given range.


n = int(input("Enter a number: "))
s = 0
N = n


while N > 0:
    digit = N % 10
    s += digit ** len(str(n))
    N //= 10


if s == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")



l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))


print("Armstrong numbers are:")

for i in range(l, u + 1):
    t = i
    s = 0
    while t > 0:
        d = t % 10
        s += d ** len(str(i))
        t //= 10
    if s == i:
        print(i)
