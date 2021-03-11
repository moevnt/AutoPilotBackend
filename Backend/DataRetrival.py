from pandas_datareader import data as wb
import datetime
import statistics as stats

today = datetime.date.today().isoformat()
previous20 = datetime.date.today() - datetime.timedelta(days=40)
print(previous20)


def getTickerInfo(ticker):
	return wb.DataReader(ticker, data_source='yahoo', start=previous20, end='2021-03-10')


# return wb.DataReader(ticker, data_source='yahoo', start=previous20, end='2021-03-10')

class DataRetrieval:
	pass
	
	def getTP(self, ticker):
		date_frame = getTickerInfo(ticker)
		TP = {}
		for i in range(20, 0, -1):
			high = date_frame.iloc[i][0]
			low = date_frame.iloc[i][1]
			close = date_frame.iloc[i][5]
			tp = (high + low + close) / 3.0
			TP[i] = tp
			print(TP[i])
			
	
	def calculateMovingAverage(self, ticker):
		date_frame = getTickerInfo(ticker)
		# Get moving average = MA(TP,n) where TP = (high+low+close)/3 && n = number of days
		sum = 0.0
		TP = self.getTP(self, ticker=ticker)
		TP.sort()
		for i in range(0, 20):
			sum += TP[i]
		
		MA = sum / 20
		return MA
	
# 2 * standard deviation of MA
	def calculateUpperBand(self, ticker):
		ma = self.calculateMovingAverage(ticker)
		upper = ma + (2*stats.stdev(self.getTP(ticker)))
		return upper
		
	def calculateLowerBand(self, ticker):
		ma = self.calculateMovingAverage(ticker)
		lower = ma - (2*stats.stdev(self.getTP(ticker)))
		return lower

df = getTickerInfo('GOOGL')
#print(df.iloc[20])

data = DataRetrieval
ma = data.calculateMovingAverage(data, ticker='AAPL')
print(ma)
#data.getTP(data, 'AAPL')
