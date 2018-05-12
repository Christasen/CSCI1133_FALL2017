
filename = open('acronyms.txt','r')
dict1 = {}

for line in filename:
    # for ch in ",.!-?_`/;():\[]{+}=@#$%^&*' ":
    #     line = line.replace(ch,"")
    # if '\t' in line:
    #     line = line.replace('\t',"")
    # elif '\n' in line:
    #     line = line.replace('\n',"")
    # elif '"' in line:
    #     line = line.replace('"',"")
    line1 = line.upper()
    for i in line1:
        if i.isalpha():
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

filename.close()
copy1 = list(dict1.items())
copy1.sort()
print(dict1)
for i, j in copy1:
    print(i," :",j)
