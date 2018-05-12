def facto(n):
    if n == 1:
        return 1
    else:
        return(n*facto(n-1))
def choose(n,k):
    div = 0;
    if n == k:
        div = 1
    elif k == 1:
        div = n
    elif k > n:
        div = 0
    else:
        a = facto(n)
        b = facto(k)
        c = facto(n-k)
        div = a // (b * c)

    return(div)



def main():
    n = int(input("Enter a value for n: "))
    k = int(input("Enter a value for k: "))
    d = choose(n,k)
    print(d)


if __name__ == "__main__":
    main()
