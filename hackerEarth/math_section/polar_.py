"""

Task
You are given a complex . Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number . Note: complex() function can be
used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of .
The second line should contain the value of .


"""
from cmath import polar
polarval=polar(complex(raw_input()))
print polarval[0]
print polarval[1]






