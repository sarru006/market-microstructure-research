# Overview

Dollar imbalance bars extend the concept of dollar bars by incorporating trade direction imbalance into the sampling process.

Instead of sampling purely by traded dollar volume, imbalance bars account for buying and selling pressure.

This produces bars that react dynamically to market order flow.


# Trade Sign

Trade direction is estimated using price changes:

b_t = +1 if price increases
b_t = -1 if price decreases


# Imbalance Formula

Theta_t = Sum(b_t × volume_t)

A new bar is generated when cumulative imbalance exceeds a threshold.


Dollar imbalance bars:

- adapt to order flow
- reduce market noise
- improve stationarity
- capture informed trading activity
- produce better ML-ready datasets


# Applications

- Order Flow Analysis
- Market Microstructure
- Alpha Research
- Statistical Arbitrage
- Financial Machine Learning


# Reference

Advances in Financial Machine Learning
by Marcos López de Prado
