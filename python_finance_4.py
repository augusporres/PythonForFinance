import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd 
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('apple.csv', parse_dates=True, index_col=0)
#df['100ma'] = df['Adj Close'].rolling(window=100).mean()  #creo nueva columna y la llamo 100ma, media movil de 100

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #pongo la fecha en formato q entiende matplotlib

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)      # params: grid_size, starting_point,..
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) 
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g') #viejo
#mpf.plot(df_ohlc.values, type='candlestick', no_xgaps=True) #nuevo, no anda todavia
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()


#plt.show()