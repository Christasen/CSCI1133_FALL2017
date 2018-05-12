import math
import random
newlist = []

def main():
    for i in range(1,10001): #could i say range(10000)
        a = random.randint(1,6)
        b = random.randint(1,6)
        sum = a + b
        newlist.append(sum)
    for j in range(2,13):
        count = newlist.count(j)
        print(count)
if __name__ == "__main__":
    main()
