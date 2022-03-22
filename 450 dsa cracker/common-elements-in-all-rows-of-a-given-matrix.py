# Common elements in all rows of a given matrix
# Difficulty Level : Medium
# Last Updated : 03 Jun, 2021
# Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.
# Example: 

# Input:
# mat[4][5] = {{1, 2, 1, 4, 8},
#              {3, 7, 8, 5, 1},
#              {8, 7, 7, 3, 1},
#              {8, 1, 2, 7, 9},
#             };

# Output: 
# 1 8 or 8 1
# 8 and 1 are present in all rows.



# https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/



n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    print(*mat[i],sep=" ")
s=set(mat[0])
for i in range(1,n):
    s=s.intersection(set(mat[i]))
print(*s)
