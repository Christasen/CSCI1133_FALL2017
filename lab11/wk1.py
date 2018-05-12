import math
class Vector:
    def __init__(self,vli = None):
        if vli == None:
            self.vli = [0,0,0]
        else:
            self.vli = vli


    def __str__(self):
        return "[" + str(self.vli[0]) + "," + str(self.vli[1]) + "," + str(self.vli[2])+ "]"

    def vlist(self):

        return self.vli

    def setValues(self, alist):
        self.vli[0] = alist[0]
        self.vli[1] = alist[1]
        self.vli[2] = alist[2]

    def __float__(self):
        for i in range(len(self.vli)):
            pro = math.pow(self.vli[i],2)
        product = math.sqrt(pro)
        return product

    def __add__(self,rhand):
        b = []
        for i in range(len(self.vli)):
            a = self.vli[i] + rhand.vli[i]
            b.append(a)
        return Vector(b)

    def __truediv__(self,s):
        b = Vector()
        for i in range(len(self.vli)):
            b.vli[i] = self.vli[i]/s
        return b

def cal(mass,v1,v2):
    F  = v1+v2
    a = F/mass
    print(a)


force1 = [2,3,4]
force2 = [1,2,3]
v1 = Vector(force1)
v2 = Vector(force2)
mass = 0.5
cal(mass,v1,v2)
