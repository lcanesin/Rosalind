#!/home/hades/anaconda3/bin/python

import math
file = open ('rosalind_ini1.txt', 'r')

lines = file.readlines
numbers = lines[0].split()
a = numbers[0]
b = numbers[1]

print (a**2 + b **2)
