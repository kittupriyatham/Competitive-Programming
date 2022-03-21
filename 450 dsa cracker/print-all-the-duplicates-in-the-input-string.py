# Print all the duplicates in the input string
# Difficulty Level : Easy
# Last Updated : 23 Nov, 2021
# Write an efficient program to print all the duplicates and their counts in the input string 


# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

s=input()
for i in set(s):
    if s.count(i)>1:
        print(i,"repeated",s.count(i),"times in",s )
