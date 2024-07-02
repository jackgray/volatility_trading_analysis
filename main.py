import requests
import os
# from dotenv import load_dotenv
import json
import numpy as np
import calendar

from pandas_datareader import data as pdr
import matplotlib.pyplot as plt


# load_dotenv()

SYMBOL='GME'


#### METHOD #1 ####
#
#
###################

# API_KEY=os.getenv('API_KEY')

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={SYMBOL}&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

print(json.dumps(data, indent=4))

##########################
#
#      METHOD #2
#
#########################

end = dt.datetime.now()
start = dt.datetime(2000,1,1)

df = pdr.get_data_yahoo([f'^{SYMBOL}'], start, end)
Close = df.Close
Close.head()

log_returns = np.log(df.Close/df.Close.shift(1)).dropna()
log_returns.plot()

TRADING_DAYS = 20
volatility = log_returns.rolling(window=TRADING_DAYS).std()*np.sqrt(252)

volatility.plot()