# data for multipl stocks
import pandas as pd
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']
# Fetch the data
import yfinance as yf
data = yf.download(tickers_list,'2015-1-1')['Adj Close']
# Print first 5 rows of the data
print(data.head())


import pandas_datareader as pdr
# Request data via Yahoo public API
data = pdr.get_data_yahoo('NVDA')
# Display Info
print(data.info())
# https://towardsdatascience.com/obtaining-historical-and-real-time-crypto-data-with-very-simple-web-programming-7b481f153630
# yfinance


# pip install pandas-datareader
import pandas_datareader as pdr
from datetime import datetime
# Pause : Time, in seconds, to pause between consecutive queries of chunks, to avoid penalty.
# If single value given for symbol, represents the pause between retries.
# Chunksize : Number of symbols to download consecutively before intiating pause.
# adjust_price alters all the prices to remove the effects of corporate actions like
# class pandas_datareader.yahoo.daily.YahooDailyReader(symbols=None, start=None, end=None, 
#   retry_count=3, pause=0.1, session=None, adjust_price=False, ret_index=False, chunksize=1, 
#   interval='d', get_actions=False, adjust_dividends=True)
data = pdr.get_data_yahoo(symbols='INFY.NS', start=datetime(2000, 1, 1), end=datetime(2022, 8, 1), pause=0.1, chunksize=1, adjust_price=True)
# datetime() takes year, month, day
start=datetime(2000, 1, 1)
end=datetime(2022, 8, 1)
data = pdr.get_data_yahoo(symbols='INFY.NS', start=start, end=end)
#print(ibm['Adj Close'])
print(data.info())
print(data.iloc[2]) # for printing rows
# data.iterrows() also can be used
print(data["Low"]) # prints a column. data.Low also works
print(data["index"]) # prints date column
# each column name is the key. 
# we get the whole column in list format
# also try 'series' instead of 'list'
# also try 'split' or 'records' or 'index'. It creates in row format instead of column
# you can convert the clubbed dict to json or directly as a file using pickle
x = data.to_dict('list') 

