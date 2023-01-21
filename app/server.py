from flask import Flask, request
import cryptoChart

app = Flask("Crypto Daily Charts")

@app.route('/')
def home():
  
  page = ""
  f = open("app/templates/layout.html", "r")
  page = f.read()
  f.close()
  
  return page

@app.route('/calculate', methods=['GET'])
def chart():
  
  page = ""
  f = open("app/templates/layout.html")
  page = f.read()
  f.close()
  
  coin = request.args.get("market")
  days = request.args.get("days")
  calculate = cryptoChart.crypto_chart(coin, days)
  calculate = calculate
  
  return page
  
if __name__ == '__main__':
  app.run(debug=True)
