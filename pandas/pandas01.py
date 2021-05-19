#!/usr/bin/python

import numpy as np
import pandas as pd

### Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

### series - listdates
dates = pd.date_range("20130101", periods=6)
print(dates)

### daframe
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )

    
print(df2)

print("\n.dtypes :")
print(df2.dtypes)


### dataframe manipulation
print("\n.head :")
print(df.head())

print("\n.tail :")
print(df.tail(3))

print("\n.index :")
print(df.index)
print("\n.columns :")
print(df.columns)

print("\n.to_numpy - conversion to numpy:")
print(df.to_numpy())
print(df2.to_numpy())

print("\n.describe() - shows a quick statistic summary of your data:")
print(df.describe())

print("\n.T :")
print(df.T)

print('\n.sort_values(by="B") :')
print(df.sort_values(by="B"))

print('\n["A"] - selection by column name, dictionary like:')
print(df["A"])

print('\n[["A","C"]] - selection by column name, dictionary like, more columns:')
print(df[["A","C"]])

print('\n[0:3] - selection by column name, dictionary like, by line numbers:')
print(df[0:3])

print('\n.loc[dates[0]] - selection by loc, line:')
print(df.loc[dates[0]])

print('\n.loc[:, ["A", "B"]] - selection by loc, submatrix:')
print(df.loc[:, ["A", "B"]])

print('\n.loc["20130102":"20130104", ["A", "B"]] - selection by loc, submatrix, date range:')
print(df.loc["20130102":"20130104", ["A", "B"]])

print('\n.loc["20130102", ["A", "B"]] - selection by loc, submatrix, date:')
print(df.loc["20130102", ["A", "B"]])

print('\n.iloc[3] - selection by iloc, numbers only allowed, line:')
print(df.iloc[3])

print('\n.iloc[0:3,0:2] - selection by iloc, numbers only allowed, submatrix:')
print(df.iloc[0:3,0:2])

print('\n[df["A"] > 0] - get lines A > 0:')
print(df[df["A"] > 0])





