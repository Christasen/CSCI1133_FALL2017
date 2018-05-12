def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

def main():
    n1 = int(input("Enter a number you want: "))
    print(fibo(n1))

if __name__ == "__main__":
    main()
