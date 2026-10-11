import pandas as pd
import numpy as np
from tabulate import tabulate

print("Environment setup verified!")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(tabulate(df, headers='keys', tablefmt='pipe'))