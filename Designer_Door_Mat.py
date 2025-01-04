# # Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications.

# Mat size must be N x M. (N is an odd natural number, and M is times N.)
# The design should have "WELCOME" written in the center.
# The design pattern should only use |,. and - characters.

# Input Format
# A single line containing the space separated values of N and M.
# Constraints
# 5 < N < 101
# 15 < M < 303

# Output Format
# Output the design pattern.
# Sample Input
# 9 27
# output:
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# code:
# Get user input for the pattern dimensions
n, m = map(int, input().split())  # We use map to convert input values directly to integers

# Initialize the number of ".|." symbols
s = 1

# Loop through each line of the pattern
for line in range(n):
    # For lines before the middle, print ".|." pattern
    if line < n // 2:
        print((".|." * s).center(m, "-"))
        s += 2  # Increase the number of symbols
    # For the middle line, print the word "WELCOME"
    elif line == n // 2:
        print("WELCOME".center(m, "-"))
    # For lines after the middle, decrease the number of ".|." symbols
    else:
        s -= 2
        print((".|." * s).center(m, "-"))
