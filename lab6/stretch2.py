import random
from WP1 import matrix

def order(m):

    order1 = len(m)

    order2 = len(m[order1 -1])

    return(order1,order2)

def populate(m,n,value):
    c,d = order(m)

    for i in range (n):
        a = random.randint(0,c-1)
        b = random.randint(0,d-1)
        m[a][b] = value

    return(m)


def main():
    # x = eval((input("Enter your matrix: ")))
    # y,z = order(x)
    # print(y,"is the length", z, "is the width")
    #
    # a = int(input("Enter the numbers of value you want to change: "))
    #
    # value = int(input("Enter the value you want to change to: "))

    x = matrix(3,0)
    a = 2
    value = 1
    populate(x,a,value)
    print(x)



if __name__ == "__main__":
    main()
