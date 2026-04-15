"""Fast, open-source data analysis and manipulation library"""
import pandas as pd

dict1 = {
    "Name" : [
        "Mr Brown",
        "Mr Chaddha",
        "Mrs Malhotra"
    ],
    "Age" : [50, 40, 24],
    "Sex" : ["male", "male", "female"]
}

# A "DataFrame" is a 2-dimensional data structure that can store data of different types
def create_df():
    df = pd.DataFrame(dict1)
    print(df)
    print(df["Age"][0])
    print(f"Describe numerical col data : {df.describe()}")    #describe() method provides quick overview of the "numerical" data in a DataFrame
    print(f"Datatypes of col : {df.dtypes}")
create_df()

# Each column of a dataframe is a "Series"
def create_series():
    ds = pd.Series([50, 40, 24], name="Age")
    print(ds)
    print(ds.max())
create_series()

# Merging dataframes together
df1 = pd.DataFrame(
    {
    "A" : [1, 2, 3, 4],
    "B" : [5,6,7,8],
    "C" : [9,10,11,12],
    },
    index=[1, 2, 3,4]
)
df2 = pd.DataFrame(
    {
    "A" : [10, 20, 30, 40],
    "B" : [50,60,70,80],
    "C" : [90,100,110,120],
    },
    index=[5,6,7,8]
)

frames = [df1, df2]
result = pd.concat(frames)
print(result)