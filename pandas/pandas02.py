#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#print("https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html")

plt.close("all")

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
#plt.show()

df = pd.DataFrame(
np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"])
df = df.cumsum()
#plt.figure()
df.plot()
plt.legend(loc='best')

plt.show()

