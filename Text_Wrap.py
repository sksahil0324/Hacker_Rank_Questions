# # Task
# You are given a string S and width w.

# Your task is to wrap the string into a paragraph of width w.


# Input Format
# The first line contains a string, S.

# The second line contains the width, w.

# Constraints
# 0 < len(S) < 1000
# 0 < w < len(S)

# Output Format
# Print the text wrapped paragraph.


# Sample Input

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ



# Code :
import textwrap

def wrap(string, max_width):
    wrapped_text = ""
    for i in range(0, len(string), max_width):
        wrapped_text += string[i:i+max_width] + "\n"
    return wrapped_text.strip()

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
