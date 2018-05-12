class measure:
    def __init__(self,f=0,i=0):
        self.feet = 0
        self.inches = 0
        if f >12:
            self.feet = f //12
            self.inches = f %12
        else:
            self.feet = f
            self.inches = i

        if i < 0:
            f = self.feet*12 - self.inches
            self.feet = f //12
            self.inches = f%12
        elif i > 12:
            self.feet = i //12 + self.feet
            self.inches = i%12

    def __str__(self): #create a return method
        if self.feet == 0 and self.inches != 0:
            return str(self.inches)+ '"'
        elif self.feet != 0 and self.inches ==0:
            return str(self.feet)+ "'"
        else:
            return str(self.feet) + "'" + str(self.inches) + '"'

    def __add__(self,rhand):
        feet = self.feet + rhand.feet
        inches = self.inches + rhand.inches
        pro = measure(feet,inches)
        return pro

    def __sub__(self,rhand):
        feet = self.feet - rhand.feet
        inches = self.inches - rhand.inches
        pro = measure(feet,inches)
        return pro

m1 = measure()
m2 = measure(4,11)
m3 = measure(6,10)
m4 = measure(48)
print(m1)
print(m2+m3)
print(m4)
print(m3-m2)
