import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

#  #  #  API
cg = CoinGeckoAPI()

def crypto_chart(coin, days):
  """
  This functions gets the crypto data from CoinGecko, then calculates and returns the daily candle stick chart against usd
  """
  
  market = cg.get_coin_market_chart_by_id(id=coin, vs_currency='usd', days=days)
  market_data = market['prices']
  data = pd.DataFrame(market_data, columns=['TimeStamp', 'Price'])

  #  Making the TimeStamp Readable
  data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

  #  #  #  Printing the candles
  candle_stick_data = data.groupby(data.date, as_index=False).agg({'Price': ['min', 'max', 'first', 'last']})

  fig = go.Figure(data=[go.Candlestick(x=candle_stick_data['date'], open=candle_stick_data['Price']['first'], high=candle_stick_data['Price']['max'], low=candle_stick_data['Price']['min'], close=candle_stick_data['Price']['last'])])
  fig.update_layout(xaxis_rangeslider_visible=False)

  fig.show()

  return crypto_chart
