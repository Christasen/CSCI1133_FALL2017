#stretch 1
def ltrcount(astring):
    for ch in ",.!&*%@;: ":
        astring = astring.replace(ch, "")
    astring = astring.lower()
    return astring

def main():
    s = input("Enter a single string: ")
    s = ltrcount(s)

if __name__ == "__name__":
    main()
