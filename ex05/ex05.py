import pandas as pd

data = {
    'value': [20.45, 22.89, 32.12, 111.22, 33.22, 100, 99.99],
    'product': ['table', 'chair', 'chair', 'mobile phone', 'table', 'mobile phone', 'table']
}
df = pd.DataFrame(data)

result = df.groupby('product')['value'].agg(['min', 'max', 'mean']).reset_index()
print(result.to_markdown())