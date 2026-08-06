import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

plt.style.use("seaborn-v0_8")
a=sn.load_dataset("titanic")
print(a.head())

sn.jointplot(x="age",y="fare",data=a)
sn.jointplot(x="age",y="fare",hue="survived",data=a)
sn.jointplot(x="age",y="fare",kind="kde",data=a)
sn.jointplot(x="age",y="fare",kind="hex",data=a)
sn.jointplot(x="age",y="fare",kind="reg",data=a)

dt= a.dropna(subset=["age","fare"])
sn.jointplot(x="age",y="fare",data=dt)
plt.show()
