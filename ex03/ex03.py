import pandas as pd
import numpy as np

# Generate days
all_dates = pd.date_range('2021-01-01', '2021-12-15')
business_dates = pd.bdate_range('2021-01-01', '2021-12-31')

# Generate tickers
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']

# Create indexes
index_alt = pd.MultiIndex.from_product([all_dates, tickers], names=['Date', 'Ticker'])
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])

# Create DataFrames
market_data = pd.DataFrame(index=index,
                           data=np.random.randn(len(index), 3),
                           columns=['Open', 'Close', 'Close_Adjusted'])

alternative_data = pd.DataFrame(index=index_alt,
                                data=np.random.randn(len(index_alt), 2),
                                columns=['Twitter', 'Reddit'])

# Merge using market_data as reference (left join)
merged = market_data.join(alternative_data, how='left')

# Fill missing values with 0
merged = merged.fillna(0)

print(merged.head(10))
print(f"\nShape: {merged.shape}")