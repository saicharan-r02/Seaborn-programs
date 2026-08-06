import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

plt.style.use("seaborn-v0_8")
d=sn.load_dataset("penguins")

print(d.head())

sn.catplot(x="species", y="body_mass_g", kind="strip", data=d)
sn.catplot(x="species", y="body_mass_g", kind="strip", jitter=0.4, data=d)
sn.catplot(x="species", y="body_mass_g", kind="strip", jitter=True, data=d)
sn.catplot(x="species", y="body_mass_g", kind="swarm", data=d)
sn.catplot(x="species", y="body_mass_g", kind="swarm",hue="sex" ,data=d)
sn.catplot(x="species", y="body_mass_g", kind="box", data=d)
sn.catplot(x="species", y="body_mass_g", kind="box",hue="sex" ,data=d)
sn.catplot(x="species", y="body_mass_g", kind="violin", data=d)
sn.catplot(x="species", y="body_mass_g", kind="violin",hue="sex",data=d)
sn.catplot(x="species", y="body_mass_g", kind="violin",hue="sex",split=True,data=d)
sn.catplot(x="species", y="body_mass_g", kind="bar",data=d)
sn.catplot(x="species", y="body_mass_g", kind="bar",hue="sex",data=d)
sn.catplot(x="species", y="body_mass_g",estimator=np.median, kind="bar",hue="sex",data=d)
sn.catplot(x="species", hue="sex", kind="count", data=d)
plt.show()
