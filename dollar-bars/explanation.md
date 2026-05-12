# Overview

Traditional time bars sample market data at fixed time intervals. However, financial markets are event-driven and trading activity varies significantly throughout the day.

Dollar bars are constructed by sampling data whenever a fixed amount of traded dollar value is reached.

This approach adapts to market activity and captures periods of high liquidity and volatility more effectively than time bars.


Dollar Value = Price × Volume

A new bar is created whenever cumulative traded dollar value exceeds a predefined threshold.

Dollar bars:

- reduce heteroskedasticity
- reduce serial correlation
- normalize information arrival
- improve statistical properties of financial data
- provide cleaner inputs for machine learning models


# Applications

- Financial Machine Learning
- Market Microstructure Analysis
- Statistical Arbitrage
- Transaction Cost Analytics
- High Frequency Trading Research


# Reference

Advances in Financial Machine Learning
by Marcos López de Prado
