# Matrix-Script
HackerRank Python problem

Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).


To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers  (rows) and  (columns) respectively.
The next  lines contain the row elements of the matrix script.

Constraints


Note: A  score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.

Sample Input 0

7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
Sample Output 0

This is Matrix#  %!
Explanation 0

The decoded script is:

This$#is% Matrix#  %!
Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.

So, the final decoded script is:

This is Matrix#  %!



code:
#!/bin/python3

import re

# Read input dimensions
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

# Read the matrix
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Extract column-wise characters into a single string
string = ''
for col in range(m):
    for row in range(n):
        string += matrix[row][col]

# Clean the string by replacing non-alphanumeric sequences with a space
result = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', string)

# Print the cleaned string
print(result)
