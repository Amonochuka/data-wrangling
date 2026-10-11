import pandas as pd

df1_dict = {
    'id': ['1', '2', '3', '4', '5'],
    'Feature1': ['A', 'C', 'E', 'G', 'I'],
    'Feature2': ['B', 'D', 'F', 'H', 'J']
}
df1 = pd.DataFrame(df1_dict, columns=['id', 'Feature1', 'Feature2'])

df2_dict = {
    'id': ['1', '2', '6', '7', '8'],
    'Feature1': ['K', 'M', 'O', 'Q', 'S'],
    'Feature2': ['L', 'N', 'P', 'R', 'T']
}
df2 = pd.DataFrame(df2_dict, columns=['id', 'Feature1', 'Feature2'])

# Merge 1: Inner merge (default suffixes _x, _y)
merge1 = pd.merge(df1, df2, on='id', how='inner')
print("Merge 1 (inner):")
print(merge1)
print()

# Merge 2: Outer merge with custom suffixes
merge2 = pd.merge(df1, df2, on='id', how='outer', suffixes=('_df1', '_df2'))
print("Merge 2 (outer with custom suffixes):")
print(merge2)