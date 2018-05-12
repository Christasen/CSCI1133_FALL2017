filename = open('all_day.csv','r')

a = filename.readline()
blist = a.split(",")
i = 0

while i < len(blist):
    print (i,"\t" ,blist[i])
    i = i + 1
    
