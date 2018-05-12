import random

file1 = open('warm up file','w')
for i in range(0,1000):
    record = ''
    rand = random.randint(-1000, 1000)
    record = '1' +',' + str(rand)
    file1.write(record)
    file1.write('\n')
file1.close()
