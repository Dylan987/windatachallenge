import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dorchester_data = pd.read_csv("CityOfWindsorData/Count/Dorchester Road and Huron Church Road.csv", header=10, skipfooter=23056)
malden_data = pd.read_csv("CityOfWindsorData/Count/Malden Road and Huron Church Road.csv", header=10, skipfooter=23056)
totten_data = pd.read_csv("CityOfWindsorData/Count/Totten Street and Huron Church Road.csv", header=10, skipfooter=23056)
print(dorchester_data)
