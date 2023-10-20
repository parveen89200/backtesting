<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Backtesting</title>
</head>
<body>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.35/moment-timezone.min.js"></script>
    <script src="https://cdn.rawgit.com/emn178/js-sha256/0.9.0/build/sha256.min.js"></script>

    <script>
        // Sample historical price data (replace with your data)
        const historicalData = [
            { date: '2020-10-20', close: 100 },
            { date: '2020-10-21', close: 105 },
            // Add more data for the past three years
        ];

        // Calculate moving averages
        function calculateMovingAverage(data, period) {
            return data.map((item, index) => {
                if (index < period - 1) {
                    return
