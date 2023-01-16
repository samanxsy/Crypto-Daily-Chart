import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc
import time, os


#  #  #  API
cg = CoinGeckoAPI()

#  #  #  Menu
while True: 
  
  os.system('clear')
  print("Crypto Daily charts")
  time.sleep(0.5)
  print()
  
  crypto_coin = input("Coin name >> ").lower()
  
  try:
    days = int(input("Number of candles you want to see >> "))
    chart = cg.get_coin_market_chart_by_id(id=f'{crypto_coin}', vs_currency='usd', days=f'{days}')
  
  except ValueError:
    print()
    print("!! Invalid input.\n\n- Please enter the full ecosystem name. e.g 'Cardano'\n\n- Make sure to enter a valid Number")
    print()
    again = input("Press 'enter' to try again ")
    if again == "": 
      os.system('clear')
    else: 
      os.system('clear')

  else: 
    break


#  #  #  Printing after getting the accurate input
os.system("clear")
print("Printing the chart . . .")
time.sleep(1)   


crypto_data = chart['prices']
data = pd.DataFrame(crypto_data, columns=['TimeStamp', 'Price'])

#  Making the TimeStamp Readable
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))


#  #  #  Printing the candles
candle_stick_data = data.groupby(data.date, as_index=False).agg({'Price': ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candle_stick_data['date'], open=candle_stick_data['Price']['first'], high=candle_stick_data['Price']['max'], low=candle_stick_data['Price']['min'], close=candle_stick_data['Price']['last'])])
fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

