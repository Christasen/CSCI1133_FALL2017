def morsetrans(str1):
    morse = {
        'A' : ". _",
        'B' : "_ . . .",
        'C' : "_ . _ .",
        'D' : "_ . .",
        'E' : ".",
        'F' : ". . _ .",
        'G' : "_ _ .",
        'H' : ". . . .",
        'I' : ". .",
        'J' : ". _ _ _",
        'K' : "_ . _",
        'L' : ". _ . .",
        'M' : "_ _",
        'N' : "_ .",
        'O' : "_ _ _",
        'P' : ". _ _ .",
        'Q' : "_ _ . _",
        'R' : ". _ .",
        'S' : ". . .",
        'T' : "_",
        'U' : ". . _",
        'V' : ". . . _",
        'W' : ". _ _",
        'X' : "_ . . _",
        'Y' : "_ . _ _",
        'Z' : "_ _ . ."
    }
    a = str1.upper()
    for ch in ",~.!@#$%^&*()+= ":
        a = a.replace(ch,"")
    for i in a:
        if i in morse:
            print(morse[i])
        else:
            print(" ")


def main():
    str1 = input("Enter a string: ")
    morsetrans(str1)



if __name__ == "__main__":
    main()
