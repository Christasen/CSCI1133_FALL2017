import math
def GCD(a, b):
    a = abs(a)
    b = abs(b)
    if a < b:
        if a == 0:
            return b
        else:
            return GCD(a, b % a)
    else:
        if b == 0:
            return a
        else:
            return GCD(b, a % b)


def main():
    n = int(input("Enter a value for n: "))
    k = int(input("Enter a value for k: "))
    print(GCD(n,k))


if __name__ == "__main__":
    main()
