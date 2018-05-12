import math
import random
def roundint():
    r = float(input("Enter a float you want to round: "))
    if r > 0:
        r = r+0.5
        r = int(r)
    else:
        r = r - 0.5
        r = int(r)
    return r
