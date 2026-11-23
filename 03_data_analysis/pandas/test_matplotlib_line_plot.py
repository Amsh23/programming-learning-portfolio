import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# a=np.array([1,"12", "13.5", "mft", 17, 215])
# s=pd.Series(a)
# s
# # pd.to_numeric(s,errors="raise")
# pd.to_numeric(s,errors="ignore")
# pd.to_numeric(s,errors="coerce")
# np.max(df, axis=0, out=None, keepdims=False)
# maxpop =df["total"].max()
# maxpop
# df["total"][df["total"]==maxpop]
# df.drop("World", axis=0, inplace=True)

# from sklearn.impute import SimpleImputer
# i=SimpleImputer(missing_values=np.nan, strategy="mean")
# i.fit(df)
# new=i.transform(df)
# new
# newdf=pd.DataFrame(new,index=df.index, columns=df.columns)
# newdf
plt.plot(x,y,"CN", ms=20,mec="g", mfc="y",lw=3)
plt.title("chart1",loc="left")
plt.xlabel("axis x", fontdict=font1)
plt.ylabel("axis y", fontdict=font2)
plt.show