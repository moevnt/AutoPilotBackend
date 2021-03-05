from pandas_datareader import data as wb
import datetime

today = datetime.date.today().isoformat()
previous20 = datetime.date.today() - datetime.timedelta(days=20)

def getTickerInfo(ticker):
	return wb.DataReader(ticker, data_source='yahoo', start=previous20, end=today)


class DataRetrieval:
	pass
	
	def calculateBands(self, ticker):
		date_frame = getTickerInfo(ticker)
		# Get moving average = MA(TP,n) where TP = (high+low+close)/3 && n = number of days
		MA = {}
		for i in 20:
			TP = 0
	# 2 * standard deviation of MA

df = getTickerInfo('AAPL')
print(df.head())
