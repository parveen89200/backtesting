import backtrader as bt
import datetime

# Create a custom strategy
class MyStrategy(bt.Strategy):
    params = (
        ("sma_period", 20),
    )

    def __init__(self):
        self.data_close = self.data.close
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=self.params.sma_period
        )

    def next(self):
        if self.data_close[0] > self.sma[0]:
            # Buy signal
            self.buy()
        elif self.data_close[0] < self.sma[0]:
            # Sell signal
            self.sell()

# Create a cerebro engine
cerebro = bt.Cerebro()

# Add data feed for the last three years
data = bt.feeds.YahooFinanceData(
    dataname="
    #there is the comments
    #Predicting future stock prices
    import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample historical stock price data (replace with your data)
data = {
    'Date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
    'Close': np.random.rand(100) * 100 + 100
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the number of days in the future for prediction
days_in_future = 30

# Create a new column for the target (future price)
df['FuturePrice'] = df['Close'].shift(-days_in_future)

# Drop rows with NaN values (corresponding to the last 30 rows)
df.dropna(inplace=True)

# Features and target variable
X = df[['Close']]
y = df['FuturePrice']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the future stock price
future_price = model.predict(X_test[-1].values.reshape(1, -1))[0]

print("Predicted Future Price:", future_price)

# Plot the historical and predicted prices
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Historical Price')
plt.axvline(df['Date'].values[-1], color='r', linestyle='--', label='Last Historical Data')
plt.plot(df['Date'].values[-1] + np.array([0, days_in_future]), [df['Close'].values[-1], future_price], 'g--', label='Predicted Future Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

