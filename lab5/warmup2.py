
def findlist():
    mylist = []

    a = input("Enter the word you want to add to the list: ")
    while a != "":
        i = 1
        while i < len(a):
            if a[0] == a[i]:
                mylist.append(a)
                i = len(a)
            i += 1

        a = input("Enter the word you want to add to the list: ")

    for i in mylist:
        print(i)



def main():

    findlist()

if __name__ == "__main__":
    main()
