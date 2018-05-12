def rankandSuitCount(cards):
    rank = dict()
    suit = dict()
    for i in cards:
        if i[0] not in list(rank.keys()): #this is important
            rank[i[0]] = 1
        else:
            rank[i[0]] = rank[i[0]] + 1
        if i[1] not in list(suit.keys()): #this is important
            suit[i[1]] = 1
        else:
            suit[i[1]] = suit[i[1]] + 1

    return rank,suit
def pokerHand(cards):
    str1 = ""
    rank,suit = rankandSuitCount(cards)
    alist = list(rank.keys)

    #flush and sflush
    if len(list(suit.keys())) == 1:
        alist = list(rank.keys)
        for i in range(5):
            if alist[i] isalpha():
                if alist[i] == 'A':
                    alist[i] = 1
                elif alist[i] == 'T':
                    alist[i] = 10
                elif alist[i] == 'J':
                    alist[i] = 11
                elif alist[i] == 'Q':
                    alist[i] = 12
                elif alist[i] == 'K':
                    alist[i] = 13
            else:
                alist = int(alist[i])
        if max(alist) - min(alist) = 4:
            str1 = "Straiht flush"

        else:
            str1 = "flush"

   elif len(list(suit.keys())) > 1:
       for i in rank:
           if rank[i] == 4:
               rank = "four-of-a-kind"
           elif rank[i] == 3 and len(alist) == 2:
               str1 = "full house"
           elif rank[i] == 3 and len(alist) == 3:
               str1 = "three of a kind"
           elif len(alist) == 3 and rank[i] == 2:
               str1 = "two pair"
           elif len(alist) == 4 and rank[i] == 2:
               str1 = "one pair"

      elif len(alist) = 4:
              for a in range(5):
                  if alist[a] isalpha():
                      if alist[a] == 'A':
                          alist[a] = 1
                      elif alist[a] == 'T':
                          alist[a] = 10
                      elif alist[a] == 'J':
                          alist[a] = 11
                      elif alist[a] == 'Q':
                          alist[a] = 12
                      elif alist[a] == 'K':
                          alist[a] = 13
                  else:
                      alist = int(alist[a])
              if max(alist) - min(alist) = 4:
                  str1 = "Straiht"
              else:
                  str1 = "High card"
    return str1

def main():
    cards =  ['AS','AD','2C','TH','TS']
    string1 = pokerHand(cards)
    print(string1)


if __name__ == "__main__":
    main()
