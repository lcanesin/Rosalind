#!/home/hades/anaconda3/bin/python

a = 4133
b = 8441 + 1
sum_odd = 0

for i in range(a,b):
  if i % 2 == 1:
    sum_odd += i
  
print (sum_odd)
