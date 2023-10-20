<!DOCTYPE html>
<html>
<head>
    <title>Stock Price Prediction</title>
</head>
<body>
    <h1>Stock Price Prediction</h1>

    <script>
        // Sample historical stock price data (replace with your data)
        const historicalData = [
            { date: '2020-01-01', price: 100 },
            { date: '2020-01-02', price: 105 },
            // Add more historical data
        ];

        // Simple linear regression for prediction
        function predictFuturePrice(historicalData, daysInFuture) {
            const lastPrice = historicalData[historicalData.length - 1].price;
            const dailyReturn = (lastPrice - historicalData[0].price) / historicalData.length;
            const futurePrice = lastPrice + dailyReturn * daysInFuture;
            return futurePrice;
        }

        // Predict the future price
        const daysInFuture = 30; // Change this to predict a different number of days ahead
        const futurePrice = predictFuturePrice(historicalData, daysInFuture);

        // Display the prediction
        document.write(`<p>Predicted price ${daysInFuture} days in the future: $${futurePrice.toFixed(2)}</p>`);
    </script>
</body>
</html>
