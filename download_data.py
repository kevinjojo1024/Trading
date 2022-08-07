import pandas_datareader as pdr
from datetime import datetime
import pickle

start=datetime(2000, 1, 1)
end=datetime(2022, 8, 1)
data = pdr.get_data_yahoo(symbols='INFY.NS', start=start, end=end, pause=0.1, chunksize=1, adjust_price=True)

now = datetime.now()
dt_str = now.strftime("%d-%m-%Y_%H-%M-%S")
foldername = "yahoo_data\\"
filename = foldername + "infy_" + dt_str + ".pickle"
with open(filename, 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

print("Stock data downloaded. Filename is :")
print(filename)