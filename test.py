# try 1 minute charts
# save dict to file using pickle

import pandas_datareader as pdr
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

start=datetime(2000, 1, 1)
end=datetime(2022, 8, 1)
data = pdr.get_data_yahoo(symbols='INFY.NS', start=start, end=end, pause=0.1, chunksize=1, adjust_price=True)


tcs['Open'].plot(label = 'TCS', figsize = (15,7))
infy['Open'].plot(label = "Infosys")
wipro['Open'].plot(label = 'Wipro')
plt.title('Stock Prices of TCS, Infosys and Wipro')