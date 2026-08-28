import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

plt.style.use("seaborn-v0_8")
d=sn.load_dataset("fmri")
print(d.head())

f= d.pivot_table(index="timepoint",columns="event",values="signal",aggfunc="mean")
sn.heatmap(f)
plt.show()
sn.heatmap(f,cbar=True,linewidths=0.5,annot=True,fmt=".2f")
plt.show()
sn.heatmap(f,cbar=False,linewidths=0.5,annot=True,fmt=".2f",cmap="magma")
plt.show()
