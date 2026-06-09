import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

plt.style.use("seaborn-v0_8")
d=sn.load_dataset("titanic")
print(d.head())

sn.jointplot(x="age",y="fare",data=d)
sn.jointplot(x="age",y="fare",hue="survived",data=d)
sn.jointplot(x="age",y="fare",kind="kde",data=d)
sn.jointplot(x="age",y="fare",kind="hex",data=d)
sn.jointplot(x="age",y="fare",kind="reg",data=d)

dt= d.dropna(subset=["age", "fare"])
sn.jointplot(x="age",y="fare",data=dt)
plt.show()
