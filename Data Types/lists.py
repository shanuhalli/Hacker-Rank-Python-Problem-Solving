# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer  at position .
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer .
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of  followed by lines of commands 
# where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

# Example
# N = 4
# append 1
# append 2
# append 3 1

# print
# append 1: Append 1 to the list, arr = [1].
# append 2: Append 2 to the list, arr = [1,2].
# append 3 1: Insert 3 at index 1, arr = [1,3,2].
# print: Print the array.

# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.

N = int(input())
L = []

for i in range(0,N):
    x = input().split()
    if x[0] == "insert":
        L.insert(int(x[1]),int(x[2]))
    elif x[0] == "append":
        L.append(int(x[1]))
    elif x[0] == "pop":
        L.pop()
    elif x[0] == "print":
        print(L)
    elif x[0] == "remove":
        L.remove(int(x[1]))
    elif x[0] == "sort":
        L.sort()
    else:
        L.reverse()