#Acá voy a poner las anotaciones importantes de los videos codigo andando
import wget as w
import pandas as pd
import math as m
from math import sin, cos
from os import path as pth
import random as n

import requests

datin = {
    "usuario": ["pato", "nato", "gato"],
    "pass": ["abc123", "contra", "casdcas"],
    "random": []
}

for i in range(3):
    datin["random"].append (n.randint (1,30))

#print (datin)
df = pd.DataFrame(datin)
#print (df)

pi = 3.14
name = "pi"
print("Valor de pi:", globals()[3.14])