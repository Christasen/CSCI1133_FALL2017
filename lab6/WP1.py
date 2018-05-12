#CSCI1133
#lab6
def matrix(n, init):
    alist = []
    for i in range(n):
        blist = []
        for j in range(n): #m = [row]*init
           blist.append(init)
        alist.append(blist)
    return(alist)
"""
alist = []
blist = []
blist = blist.append(init) (2x) --> blist = [init,init]
alist.apppend(blist) --> alist = [[init,init]]

"""

def order(m):

    order1 = len(m)
    order2 = len(m[order1])

    return(order1,order2)
