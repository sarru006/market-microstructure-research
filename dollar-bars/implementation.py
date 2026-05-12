import pandas as pd

df = pd.read_csv("ticks.csv")

threshold = 1_000_000

bars = []

cum_dollar = 0
start = 0

for i in range(len(df)):

    dollar_value = (
        df.loc[i, 'price']
        * df.loc[i, 'volume']
    )

    cum_dollar += dollar_value

    if cum_dollar >= threshold:

        bar = {
            'open': df.loc[start, 'price'],
            'high': df.loc[start:i, 'price'].max(),
            'low': df.loc[start:i, 'price'].min(),
            'close': df.loc[i, 'price'],
            'volume': df.loc[start:i, 'volume'].sum()
        }

        bars.append(bar)

        start = i + 1
        cum_dollar = 0

dollar_bars = pd.DataFrame(bars)

print(dollar_bars.head())
