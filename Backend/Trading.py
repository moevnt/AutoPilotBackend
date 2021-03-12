import uuid
import mysql.connector as db
import alpaca_trade_api as tradeapi
import datetime  as dt

API_KEY = 'PK2PXLRSTXMG8Y5MQQNJ'
API_SECRET = 'GowufeeyrCEv4prwUkDoE4Ib6vOCQ7CxQXU0dyAF'
APCA_API_BASE_URL='https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2')
account = api.get_account()

mydb = db.connect(
	host="199.204.104.202",
	port="9886",
	user="root",
	password="P@55w0rd!",
	database="AutoPilot"
)

class Trading:
	
	def sell(self, ID):
		mycursor = mydb.cursor()
		SQL = "SELECT Ticker FROM Stock WHERE StockID= " + ID
		mycursor.execute(SQL)
		myresult = mycursor.fetchall()
		print(myresult)
		
		if (len(myresult) > 0):
			ticker = myresult.pop()
			print(ticker)
			
			api.submit_order(symbol=ticker,
			                 qty=1,
			                 side='sell',
			                 type='market',
			                 time_in_force='gtc')
			SQL = "DELETE FROM AutoPilot.Stock WHERE StockID = " + ID
			mycursor.execute(SQL)
	
	#			mydb.commit()
	# print('Successfully sold ' + ticker)
	
	def getTicker(self, stockID):
		mycursor = mydb.cursor()
		SQL = 'SELECT Ticker FROM Stock WHERE stockID=' + stockID
		mycursor.execute(SQL)
		myresult = mycursor.fetchall()
		ticker = myresult.pop(0)
		print(ticker.get(0))
		
	def sellAll(self, tradingID):
		mycursor = mydb.cursor()
		ticker = "AAPL"
		SQL = 'SELECT * FROM Stock '
		mycursor.execute(SQL)
		myresult = mycursor.fetchall()
		for i in range(0,len(myresult)):
			api.submit_order(symbol= ticker,
		                     qty=1,
		                     side='sell',
		                      type='market',
		                     time_in_force='gtc')
		print('Successfully sold ' + ticker)
		

	def buy(ticker, quantity, salePrice, tradingID):
		api.submit_order(symbol=ticker,
		                 qty=quantity,
		                 side='buy',
		                 type='market',
		                 time_in_force='gtc')
		today = dt.datetime.now()
		mycursor = mydb.cursor()
		SQL = "INSERT INTO AutoPilot.Stock (Ticker, PriceBought, DateBought, PriceSold, DateSold, TradingID)" \
		      "VALUES (%s, %s, %s, %s, %s, %s)"
		
		for i in range(0, quantity):
			val = (ticker, salePrice, today, None, None, tradingID)
			mycursor.execute(SQL, val)
		mydb.commit()
		print('Successfully bought '+str(quantity)+' shares of '+ticker)
		
