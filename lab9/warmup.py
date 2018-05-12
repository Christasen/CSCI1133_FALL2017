def makeDic (names,scores):
    ind = 0
    scoreDict = dict()
    for name in names:
        scoreDict[names] = scores[ind]
        ind += 1
    return scoreDict
