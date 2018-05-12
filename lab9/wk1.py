def rankandSuitCount(cards):

    rank = dict()
    suit = dict()
    for i in cards:
        if i[0] not in list(rank.keys()):
            rank[i[0]] = 1
        else:
            rank[i[0]] = rank[i[0]] + 1
        if i[1] not in list(suit.keys()):
            suit[i[1]] = 1
        else:
            suit[i[1]] = suit[i[1]] + 1

    return rank,suit

def main():
    cards =  ['AS','AD','2C','TH','TS']
    rank, suit = rankandSuitCount(cards)
    print(rank)
    print (suit)


if __name__ == "__main__":
    main()
