# Guangyu Yan yanxx630
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.
import math
class Complex:
    def __init__(self, r = 0.0, im = 0.0):
        self.__real = float(r)
        self.__imag = float(im)

    def getValue(self):
        a = self.__real
        b = self.__imag
        return Complex(a,b)

    def setValues(self, rhs):
        self.__real = rhs.__real
        self.__imag = rhs.__imag

    def __repr__(self):
        if self.__imag == 0:
            if self.__real == 0:
                return str(0)
            else:
                return str(self.__real)

        elif self.__imag == 1:
            if self.__real == 0:
                return "i"
            else:
                return str(self.__real) + " + " + "i"

        elif self.__imag < 0 and self.__imag != -1:
            if self.__real == 0:
                return str(self.__imag) + "i"
            else:
                return str(self.__real) + " - " + str(-self.__imag) + "i"

        elif self.__imag == -1:
            if self.__real == 0:
                return "-i"
            else:
                return str(self.__real) +" - " + "i"

        else:
            if self.__real == 0:
                return str(self.__imag) + "i"
            else:
                return str(self.__real) + " + " + str(self.__imag) + "i"

    def __add__(self,rhs):

        r1 = self.__real + rhs.__real
        b1 = self.__imag + rhs.__imag
        b = Complex(r1,b1)
        return b

    def __mul__(self,rhs):

        rj = self.__real*rhs.__real - self.__imag*rhs.__imag
        ia = self.__real*rhs.__imag + self.__imag*rhs.__real
        b = Complex(rj,ia)
        return b

    def __abs__(self):
        a = math.sqrt(self.__real*self.__real + self.__imag*self.__imag)
        return a

a = Complex(1,1)
b = Complex(2,2)
C= a*b
