import random


def ssorted(somelist):
    for i in range(len(somelist)):
        mindex = i

        for j in range(i+1, len(somelist)):
            if somelist[mindex] > somelist[j]:
                mindex = j
#swapping
        somelist[i], somelist[mindex] = somelist[mindex],somelist[i]
        print(somelist)



def main():
    mylist = []
    n = int(input("Enter the length of your list: "))
    for i in range(1,n+1):
        j = random.randint(1,9)
        mylist.append(j)
        i = i + 1
    random.shuffle(mylist)
    ssorted(mylist)

if __name__ == "__main__":
    main()
