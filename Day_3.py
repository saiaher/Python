

import numpy as np
from numpy.random import randint as ri
import random


hide_number=ri(1,100)
print(hide_number)

guess_number=int(input("enter yoour number:"))

if hide_number == guess_number:
    print("same")

elif hide_number < guess_number:
    print("too high")

elif hide_number > guess_number:
    print("too low")








