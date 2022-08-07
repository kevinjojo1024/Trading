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

filename = sys.argv[0]
with open(filename, 'rb') as f:
    data = pickle.load(f)

tcs['Open'].plot(label = 'TCS', figsize = (15,7))
infy['Open'].plot(label = "Infosys")
wipro['Open'].plot(label = 'Wipro')
plt.title('Stock Prices of TCS, Infosys and Wipro')