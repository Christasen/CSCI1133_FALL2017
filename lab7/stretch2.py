def reverse(astring):
    sstring = ""
    for i in range(1, len(astring)+1):
        sstring  += astring.strip()[-i]
        print(sstring)
    return sstring


def main():
    sn = input("Enter a single string: ")
    sn = reverse(sn)
    print(sn)

if __name__ == "__main__":
    main()
