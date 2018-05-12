def reverse(astring):
    sstring = ""
    for i in range(1, len(astring)+1):
        sstring  += astring.strip()[-i]
        print(sstring)
    return sstring

def ltrcount(astring):
    for ch in ",.!&*%@;: ":
        astring = astring.replace(ch, "")
    astring = astring.lower()
    return astring

def ispalindrome(astring):
    a = ltrcount(astring)
    b = reverse(a)
    if b == a:
        print(astring, "is a palindrome")
    else:
        print(astring, "is not a palindrome")


def main():
    ans = 'y'
    while ans == 'y':
        astring = input("Enter a string: ")
        ispalindrome(astring)
        ans = input("Continue: ")


if __name__ == "__main__":
    main()
