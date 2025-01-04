# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

unique_grades = sorted(set(student[1] for student in students))
second_lowest_grade = unique_grades[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
second_lowest_students.sort()

for student in second_lowest_students:
    print(student)
