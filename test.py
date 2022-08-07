# try 1 minute charts
# save dict to file using pickle

import pandas_datareader as pdr
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pickle
import sys

filename = sys.argv[1]
with open(filename, 'rb') as f:
    data = pickle.load(f)

data['Close'].plot(label = 'INFY')
extra = {}
extra['MA50'] = data['Close'].rolling(50).mean()
extra['MA200'] = data['Close'].rolling(200).mean()
extra['MA50'].plot(label = '50 MA')
extra['MA200'].plot(label = '200 MA')
#data['Open'].plot(label = 'INFY', figsize = (15,7))
plt.title('Stock Prices of Infosys')
plt.legend()
plt.show()