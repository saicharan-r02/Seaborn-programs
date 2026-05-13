import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import warnings

warnings.filterwarnings("ignore")
plt.style.use("seaborn-v0_8")

d=sn.load_dataset("penguins")
print(d.head())

sn.pairplot(d)
sn.pairplot(d,hue="species")
sn.pairplot(d,vars=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"],hue="species")
dt = sn.load_dataset("tips")
print(dt.head())
plt.figure()
sn.distplot(dt["total_bill"])
plt.figure()
sn.distplot(dt["total_bill"], kde=True, hist=True)
plt.figure()
sn.distplot(dt["total_bill"], kde=False)
plt.figure()
sn.distplot(dt["total_bill"], hist=False)
plt.figure()
sn.distplot(dt["total_bill"], bins=20)
plt.figure()
sn.distplot(dt["total_bill"], color="green")
plt.show()