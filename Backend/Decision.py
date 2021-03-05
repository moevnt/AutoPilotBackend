from Backend import DataRetrival, Trading

retrieval = DataRetrival
trade = Trading

class Decision:
	
	def makeDecision(self, ticker):
		retrieval.getTickerInfo()
