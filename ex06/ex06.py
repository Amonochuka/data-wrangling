import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

business_dates = pd.bdate_range('2021-01-01', '2021-12-31')
tickers = ['AAPL', 'FB', 'GE', 'AMZN', 'DAI']
index = pd.MultiIndex.from_product([business_dates, tickers], names=['Date', 'Ticker'])
market_data = pd.DataFrame(index=index,
                           data=np.random.randn(len(index), 1),
                           columns=['Prediction'])

unstacked = market_data.unstack(level='Ticker')
print(unstacked.head(3).to_markdown())

# Plot
unstacked.plot(title='Daily Predictions by Ticker', figsize=(12, 6))
plt.xlabel('Date')
plt.ylabel('Prediction')
plt.legend(title='Ticker')
plt.tight_layout()
plt.savefig('/home/amonoff/Projects/data-wrangling/ex06/predictions_plot.png')
print("\nPlot saved to predictions_plot.png")