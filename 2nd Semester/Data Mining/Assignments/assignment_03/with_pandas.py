import pandas as pd
from pandas import DataFrame, Index, Series

""" reading """
df: DataFrame = pd.read_csv('dlbcl-fl.csv')

""" showing the values """
print(df)

""" no. of rows """
number_of_rows: int = df.shape[0]
print(number_of_rows)

""" first row (colum label) """
column_index: Index = df.columns
column_names: list[str] = column_index.values.tolist()
print(column_names)

""" first of (without column label) """
first_row = df.iloc[[0]]
print(first_row)

""" print the last column label """
column_index: Index = df.columns
column_names: list[str] = column_index.values.tolist()
print(column_names[-1])

""" print the last column values """
column_index: Index = df.columns
column_names: list[str] = column_index.values.tolist()
last_col: str = column_names[-1]
print(df[last_col])

""" unique class labels """
column_index: Index = df.columns
column_names: list[str] = column_index.values.tolist()
last_col: str = column_names[-1]
last_col_values: Series = df[last_col]
unique_classes: list = last_col_values.unique().tolist()
print(unique_classes)

""" split the dataset according to the class label """
dfs = {}

for elem in df['class'].unique():
    dfs.setdefault(elem, df[:][df['class'] == elem])

print(dfs)
