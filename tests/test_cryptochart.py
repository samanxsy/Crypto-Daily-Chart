import unittest
from app.cryptochart import crypto_chart

class test_cryptoChart(unittest.TestCase):
  
    def test_crypto_chart(self):
        """This will test the crypto_chart function for bitcoin"""
        coin = 'bitcoin'
        days = 14
        self.assertIsNotNone(crypto_chart(coin, days))
        
        
    def test_crypto_chart2(self):
        """This will test the crypto_chart function for ethereum"""
        coin = 'ethereum'
        days = 30
        self.assertIsNotNone(crypto_chart(coin, days))


    def test_crypto_chart3(self):
        """This will test the crypto_chart function for cardano"""
        coin = 'cardano'
        days = 20
        self.assertIsNotNone(crypto_chart(coin, days))


    def test_crypto_chart4(self):
        """This will test the crypto_chart function for polkadot"""
        coin = 'polkadot'
        days = 7
        self.assertIsNotNone(crypto_chart(coin, days))


if __name__ == '__main__':
  unittest.main()