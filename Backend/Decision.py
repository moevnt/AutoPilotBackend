from Backend import DataRetrival, Trading
from pandas_datareader import data as wb
import datetime

retrieval = DataRetrival
trade = Trading
today = datetime.date
print(today)

class Decision:
	
	def makeDecision(self, ticker):
		wb.DataReader(ticker, data_source='yahoo', start=today)
