# Lists

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands. 
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())  # Number of commands
    lst = []  # Initialize an empty list

    for _ in range(n):
        command = input().strip().split()  # Read the command and split into parts
        cmd = command[0]  # The first part is the command
        args = command[1:]  # Remaining parts are arguments
        
        if cmd == "insert":
            lst.insert(int(args[0]), int(args[1]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(args[0]))
        elif cmd == "append":
            lst.append(int(args[0]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()

