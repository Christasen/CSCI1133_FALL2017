def mysplit(astring, deli):
    alist =[]
    word = ''
    for ch in astring:
        if ch == deli:
            if word != '': #and word != deli:
                alist.append(word)
            word = ''

        else:
            word += ch
    if word != deli and word!= '':
        alist.append(word)
    return alist

def main():

    astring = input("Enter a string: ")
    dele = input("Enter a delimiter: ")
    a = mysplit(astring,dele)
    print(a)


if __name__ == "__main__":
    main()
