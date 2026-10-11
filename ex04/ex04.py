import pandas as pd
import numpy as np

def winsorize(df, quantiles):
    """
    df: pd.DataFrame
    quantiles: list
        ex: [0.05, 0.95]
    """
    lower = df.quantile(quantiles[0])
    upper = df.quantile(quantiles[1])
    return df.clip(lower, upper, axis=1)

# Test 1: Simple winsorize
df = pd.DataFrame(range(1, 11), columns=['sequence'])
result = winsorize(df, [0.20, 0.80])
print("Test 1 - Simple winsorize:")
print(result.to_markdown())
print()

# Test 2: Groupby winsorize
groups = np.concatenate([np.ones(10), np.ones(10)+1, np.ones(10)+2, np.ones(10)+3, np.ones(10)+4])
df = pd.DataFrame(data=zip(groups, range(1, 51)), columns=["group", "sequence"])

result = df.groupby('group')['sequence'].apply(lambda x: winsorize(x.to_frame(), [0.05, 0.95])).reset_index(drop=True)
print("Test 2 - Groupby winsorize (first 15 rows):")
print(result.head(15).to_markdown())