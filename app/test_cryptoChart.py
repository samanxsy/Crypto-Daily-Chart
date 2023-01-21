import unittest
from cryptoChart import crypto_chart

class test_cryptoChart(unittest.TestCase):
  
  def test_crypto_chart(self):
    
    coin = 'bitcoin'
    days = 14
    
    self.assertIsNotNone(crypto_chart(coin, days))

  def test_crypto_chart2(self):
    
    coin = 'ethereum'
    days = 30
    
    self.assertIsNotNone(crypto_chart(coin, days))
    
  def test_crypto_chart3(self):
    
    coin = 'cardano'
    days = 20
    
    self.assertIsNotNone(crypto_chart(coin, days))
    
  def test_crypto_chart4(self):
    
    coin = 'polkadot'
    days = 7
    
    self.assertIsNotNone(crypto_chart(coin, days))
    
if __name__ == '__main__':
  unittest.main()