#!/home/hades/anaconda3/bin/python

input = open('/home/hades/Downloads/rosalind_ini5.txt', 'r')
output = open('/home/hades/data_science/Rosalind/output_PV5.txt', 'w')
i = 0

for line in input:
  i += 1
  if i % 2 == 0:
    output.write(line)

input.close()
output.close()