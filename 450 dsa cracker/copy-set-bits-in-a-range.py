x,y,l,r=map(int,input().split())
xs=bin(x)[2:][::-1]
ys=bin(y)[2:][::-1]
print(xs,ys)
for i in range(l-1,r):
    if ys[i]=='1' and xs[i]=='0':
        xs=xs[:i]+'1'+xs[i+1:]
print(xs[::-1])
print(int(xs[::-1],2))

# Copy set bits in a range
# Difficulty Level : Medium
# Last Updated : 28 Dec, 2021
# Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also.
# Examples : 

# Input  : x = 10, y = 13, l = 2, r = 3
# Output : x = 14
# Binary representation of 10 is 1010 and 
# that of y is 1101. There is one set bit
# in y at 3'rd position (in given range). 
# After we copy this bit to x, x becomes 1110
# which is binary representation of 14.

# Input  : x = 8, y = 7, l = 1, r = 2
# Output : x = 11

#https://www.geeksforgeeks.org/copy-set-bits-in-a-range/
