# Guangyu Yan yanxx630
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.
from complex import Complex
class Mandelbrot:

    def __init__(self,c,limit=50):
        self.__limit = int(limit)
        self.__colormap = ["red","orangered","orange","greenyellow","mediumseagreen","cyan","blue","purple"]
        i = 0
        z0 = c
        self.__car = 0
        self.__max1 = 500
        while i < self.__limit:
            z1 = z0*z0 + c
            if abs(z1) <= 2:
                self.__car = self.__car + 1
            z0 = z1
            if abs(z0) > self.__max1:
                i = 50
            else:
                i = i + 1
    def get_color(self):
        if self.__car == self.__limit:
            return "black"
        elif self.__car < 3 and self.__car >= 0:
            return self.__colormap[0]
        elif self.__car < 5 and self.__car >= 3:
            return self.__colormap[1]
        elif self.__car < 7 and self.__car >= 5:
            return self.__colormap[2]
        elif self.__car < 10 and self.__car >= 7:
            return self.__colormap[3]
        elif self.__car < 20 and self.__car >= 10:
            return self.__colormap[4]
        elif self.__car < 30 and self.__car >= 20:
            return self.__colormap[5]
        elif self.__car < 40 and self.__car >= 30:
            return self.__colormap[6]
        elif self.__car < 50 and self.__car >= 40:
            return self.__colormap[7]

limit = 50
c1 = Complex(0.2,-0.564)

M1 = Mandelbrot(c1,limit=50)
a = M1.get_color()
