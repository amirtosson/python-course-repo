  
import pandas as pd
import matplotlib as mtp 
from matplotlib import pyplot as plt
data = pd.read_csv("/Users/marialompe/Desktop/countries_python_test.csv")
data
us = data[data.country == "United States"]
china = data[data.country == "China"]
plt.plot(us.year, us.population)
plt.plot(china.year, china.population)
plt.legend(["united states", "china"])
plt.xlabel ("year")
plt.xlabel ("population")
plt.show()
