from Backend import DataRetrival

data = DataRetrival
ticker = 'AAPL'
ma = data.calculateMovingAverage(data, ticker)
lower = data.calculateLowerBand(data, ticker)
today = data.getToday(ticker)
test = today.iloc[0][5]

if test < ma:
	if test > lower:
		print("BUY")
