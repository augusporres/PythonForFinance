import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2020, 1, 1)
#end = dt.datetime(2021, 1, 1)

#df = web.DataReader('AAPL', 'yahoo', start, end)
#df.to_csv('appple.csv')

df = pd.read_csv('apple.csv', parse_dates=True, index_col=0)
#print(df.head())


print(df[['Open', 'Close']].head())
df['Adj Close'].plot()
plt.show()
