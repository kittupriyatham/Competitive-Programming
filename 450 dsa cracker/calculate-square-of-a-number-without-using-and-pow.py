# Calculate square of a number without using *, / and pow()
# Difficulty Level : Medium
# Last Updated : 23 Feb, 2021
# Given an integer n, calculate the square of a number without using *, / and pow(). 

# Examples : 

# Input: n = 5
# Output: 25

# Input: 7
# Output: 49

# Input: n = 12
# Output: 144


# https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/

n=abs(int(input()))
s=0
for i in range(n):
    s+=n
print(s)
