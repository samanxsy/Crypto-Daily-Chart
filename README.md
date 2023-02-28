# Crypto-Daily-Chart
This application that fetches the market data of a specified cryptocurrency and plots the candlestick chart using the CoinGecko API.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


#### Prerequisites
- Python 3.x
- CoinGecko API key
- pandas
- plotly
- numpy


#### Installing 

1. clone the repository to your local machine:
```
git clone https://github.com/samanxsy/Crypto-Daily-Chart.git
```

2. install the requirements
```
pip install -r requirements.txt
```

3. There is no API Key required to run this program. All you need to do is: 
  - from pycoingecko import CoinGeckoAPI

4. Run the tests with pytest
```
pytest
```

5. Run the program on your localhost
```
gunicorn app.server:app
```

#### Usage
The application has a simple interface requiring the "Ecosystem" name, and the number of "Previous Candles" you want to see. Once you enter the valid inputs, the program will display the candlestick chart in a new window.

Make sure you enter the "Ecosystem" name. e.g "Cardano" not "Ada", and "Polkadot" not "Dot"

### App view

![Ethereum](https://user-images.githubusercontent.com/118216325/213879043-04a73739-e6d8-4d5c-84f2-6a69f8629a22.png)
![chart](https://user-images.githubusercontent.com/118216325/213879052-f5ac1ca8-5f20-4547-8bdc-160525a1fb05.png)

#### Built With 
- Python - Programming Language
- CoinGecko API - Cryptocurrency Market Data
- pandas - Data Manipulation
- plotly - Data Visualization

#### Author 
- Saman Saybani (Samanxsy)

#### Acknowledgments
- CoinGecko API
- This was an extra work as a part of my DevOps & Software Engineer course
