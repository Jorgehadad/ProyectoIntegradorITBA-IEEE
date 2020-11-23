import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

print ("Ahora se mostraran la comparativa entre las empresas de Amazon y Google")
#wget ("https://raw.githubusercontent.com/LedesmaFran/python/master/GOOGLE.csv") 
#wget  ("https://raw.githubusercontent.com/LedesmaFran/python/master/AMZN.csv")

googlefile = pd.read_csv("GOOGLE.csv")
amazonfile = pd.read_csv("AMZN.csv")
google2= pd.DataFrame(googlefile)
google = googlefile.to_dict("list")
amazon = amazonfile.to_dict("list")

print (google2["Date"].count())