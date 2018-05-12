filename = open('all_day.csv','r')
list1 = filename.readlines()
i = 1
mag = []
loc = []
while i < len(list1):
    a = list1[i]
    a = a.replace('"',"")
    blist = a.split(',')
    c = blist[13] + "," + blist[14]
    loc.append(c)
    mag.append(blist[4])
    i = i + 1
i = 0
while i < len(loc):
    print("Location"," ",loc[i] )
    i = i + 1

while i < len(mag):
    print("Magnitude","",mag[i])
    i = i + 1
