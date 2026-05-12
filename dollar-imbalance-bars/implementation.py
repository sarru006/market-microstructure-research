import pandas as pd
import numpy as np

df = pd.read_csv("ticks.csv")

df['price_diff'] = df['price'].diff()


df['b_t'] = np.where(
    df['price_diff'] > 0,
    1,
    -1
)

threshold = 10000

bars = []

cum_theta = 0
start = 0

for i in range(1, len(df)):

    theta = (
        df.loc[i, 'b_t']
        * df.loc[i, 'volume']
    )

    cum_theta += theta

    if abs(cum_theta) >= threshold:

        bar = {
            'open': df.loc[start, 'price'],
            'high': df.loc[start:i, 'price'].max(),
            'low': df.loc[start:i, 'price'].min(),
            'close': df.loc[i, 'price'],
            'volume': df.loc[start:i, 'volume'].sum()
        }

        bars.append(bar)

        start = i + 1
        cum_theta = 0

imbalance_bars = pd.DataFrame(bars)

print(imbalance_bars.head())
