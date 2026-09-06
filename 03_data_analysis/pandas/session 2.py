# ���� ����� ���� ����� c++ 
# Mr. Ahmadi: C++

# pandas: csv, excel, json, ...
# (anaconda)
# pip install pandas


import numpy as np
import pandas as pd

pd.__version__

arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
df=pd.DataFrame(arr, index=["A", "B", "C"], columns=["col1","col2", "col3", "col4"])


mydict={"col1":[1,5,9],"col2":[2,6,10],"col3":[3,7,11],"col4":[4,8,12]}
df=pd.DataFrame(mydict, index=["A", "B", "C"], columns=["col1","col2", "col3", "col4"])

# old version
df.loc["A"]["col2"]         # locatoin
df.iloc[0][3]               # i location

# new versions
df.loc["A","col2"]         # locatoin
df.iloc[0,3]               # i location

df.iloc[[0,1],3]

df.iloc[:,3]

df["col5"]=[8,88,888]       # ading a new column

df.loc["A","col3"] = 0

df.dtypes

df["col1"]=["{:.2f}".format(float(x)) for x in df.iloc[:,0]]

name=input("enter name")
age=int(input("enter age"))
avg=float(input("enter average"))
print(f"my name is {name}, im{age} years old, my average is {avg}")
print("my name is {}, im {} years old, my average is {}".format(name,age,avg))
print(f"my name is %s, im %d years old, my average is %0.2f"%(name, age, avg))

df.col2=df["col2"].apply(lambda x: "{:.2f}".format(float(x)))

# what i wrote: (not what teacher said)
x = lambda a : "{:.2f}".format(float(a))
df["col2"] = [x(a) for a in df.iloc[:,1]]
df


mydf=df.astype(float).map("{:.2f}".format)      # for new versions
mydf=df.astype(float).applymap("{:.2f}".format)     # for old versions

df.drop("col4", axis=1,inplace=True)
df

df.rename(columns={"col3":"columns3"}, inplace=True)
df
df.replace(8,"arash", inplace=True)
df["col1"].replace(2,"wow", inplace=True)
df.col1.replace(2,"wow", inplace=True)

a = np.array([1,10,25,24,65])
s=pd.Series(a,index=["a","b", "c", "d", "e"])
s



df=pd.read_csv(r"C:\Users\Student\Desktop\data1.csv")

pd.options.display.max_rows=7
pd.set_option("display.max_rows", None)

df.head(3)          # default=5
df.tail(7)          # default=5
df.sample(5)        # random


# kaggle.com        datasets

df.to_string()

df1=pd.read_json(r"C:\Users\Student\Desktop\data.json")


df.iloc[0,3]=np.nan

df.dropna(inplace=True)

df.fillna(1000,inplace=True)    # replace Nan with 1000

df["Weight"].fillna(1000,inplace=True)

df["Weight"].fillna(df["Weight"].mean(),inplace=True)   # put the average

df["Weight"].fillna(round(df["Weight"].mean()),inplace=True)        # round the result value

df["Weight"].fillna(round(df["Weight"].median()),inplace=True)          # میانه

df["Weight"].fillna(df["Weight"].mode(),inplace=True)            # بیشترین تکرار 0 indicates the most used one

df.ffill(inplace=True)      # fill with top value
df.bfill(inplace=True)      # fill with the bottom value

country=pd.read_csv(r"C:\Users\Student\Desktop\country.csv", header=1)

country.drop("1", axis=1, inplace=True)
country.drop("CountryCode", axis=1, inplace=True)

country.drop(columns=["1","CountryCode"], inplace=True)


country.rename(index=country.CountryName, inplace=True)
country.drop("CountryName", axis=1, inplace=True)


country.rename(columns={"population growth":"growth", "Total population":"Total", "Area (sq. km)": "area"}, inplace=True)
country.dtypes
country.describe()
country["growth"]=pd.to_numeric(country["growth"], errors="coerce")
# 


# Pandas
# ------------
# pd.read_csv
# pd.read_json
# pd.read_excel
# -----------
# df.head()
# df.tail()
# df.sample(n)
# df.to_string
# pd.optoins.display.max_rows = n
# -------------
# Nan 
#   dropna
#   fillna
#   fillna
#   ffill
# 


