# Task :
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i2.

# Example
# n = 3

# The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.

# Input Format
# The first and only line contains the integer, n.

# Constraints
# 1 <= n <= 20

# Output Format
# Print n lines, one corresponding to each i.

n = int(input())
for i in range (0,n):
    print(i**2)