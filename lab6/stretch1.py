#CSCI1133
#lab6

def identity(n):

    alist = []
    for i in range(n):
        blist = []
        for j in range(n): #m = [row]*init
           blist.append(0)
        alist.append(blist)

    for a in range(n):
        alist[a][a] = 1


    return(alist)

def main():
    x = int(input("Enter the n you wanna have for your matrix: "))
    m  = identity(x)
    print(m, "is the matrix you want")



if __name__ == "__main__":
    main()
