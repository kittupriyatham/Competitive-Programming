# Divide two integers without using multiplication, division and mod operator
# Difficulty Level : Medium
# Last Updated : 17 Feb, 2022
# Given a two integers say a and b. Find the quotient after dividing a by b without using multiplication, division and mod operator.

# Example: 

# Input : a = 10, b = 3
# Output : 3

# Input : a = 43, b = -8
# Output :  -5 


# https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/

a,b=map(int,input().split())
c=0
while a-abs(b)>0:
    a-=abs(b)
    c+=1
    print(a,b,c)
print()
print(a)
print(c)
