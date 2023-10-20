require 'quantlib-rb'

# Sample historical price data (replace with your data)
historical_data = [
  { date: Date.new(2020, 10, 20), close: 100 },
  { date: Date.new(2020, 10, 21), close: 105 },
  # Add more data for the past three years
]

# Calculate moving averages
def calculate_moving_average(data, period)
  data.each_with_index.map do |item, index|
    if index < period - 1
      nil
    else
      sum = data[index - period + 1..index].map { |d| d[:close] }.reduce(:+)
      sum / period.to_f
    end
  end
end

# Simple moving average parameters
fast_sma = 50
slow_sma = 200

# Calculate fast and slow SMAs
fast_sma_data = calculate_moving_average(historical_data, fast_sma)
slow_sma_data = calculate_moving_average(historical_data, slow_sma)

# Backtest: Buy when fast SMA crosses above slow SMA, sell when it crosses below
signals = []
(0..(historical_data.length - 1)).each do |i|
  next if i < slow_sma

  if fast_sma_data[i] > slow_sma_data[i] && fast_sma_data[i - 1] <= slow_sma_data[i - 1]
    signals.push({ date: historical_data[i][:date], signal: 'Buy' })
  elsif fast_sma_data[i] < slow_sma_data[i] && fast_sma_data[i - 1] >= slow_sma_data[i - 1]
    signals.push({ date: historical_data[i][:date], signal: 'Sell' })
  end
end

# Output signals to the console
puts "Signals:"
signals.each { |s| puts "Date: #{s[:date]}, Signal: #{s[:signal]}" }
