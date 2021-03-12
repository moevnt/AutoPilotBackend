from pandas_datareader import data as wb
import datetime
import statistics as stats

today = datetime.date.today().isoformat()
previous20 = datetime.date.today() - datetime.timedelta(days=100)


def getTickerInfo(ticker):
	return wb.DataReader(ticker, data_source='yahoo', start=previous20, end=today)

def getToday(ticker):
	return wb.DataReader(ticker, data_source='yahoo', start=today, end=today)


def getTP(self, ticker):
	date_frame = getTickerInfo(ticker)
	TP = {}
	size = len(TP)
	for i in reversed(range(size-50, size)):
		high = date_frame.iloc[i][0]
		low = date_frame.iloc[i][1]
		close = date_frame.iloc[i][5]
		tp = (high + low + close) / 3.0
		TP[i] = tp
	return TP


def calculateMovingAverage(self, ticker):
	# Get moving average = MA(TP,n) where TP = (high+low+close)/3 && n = number of days
	sum = 0.0
	TP = self.getTP(self, ticker=ticker)
	keys = TP.keys()
	for i in keys:
		sum = sum + TP[i]
	MA = sum / 50
	return MA
	

# 2 * standard deviation of MA
def calculateUpperBand(self, ticker):
	ma = self.calculateMovingAverage(self, ticker)
	upper = ma + (2 * stats.stdev(self.getTP(self, ticker)))
	return upper


def calculateLowerBand(self, ticker):
	ma = self.calculateMovingAverage(self, ticker)
	lower = ma - (2 * stats.stdev(self.getTP(self, ticker)))
	return lower
