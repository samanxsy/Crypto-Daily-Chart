from flask import Flask, request, redirect
import cryptoChart

app = Flask("Crypto Daily Charts", static_folder="./app/static")

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
  
  try:
    calculate = cryptoChart.crypto_chart(coin, days)
    calculate = calculate
  except ValueError:
    return redirect('/error')
  
  return page

@app.route('/error')
def error():
  
  page = ""
  f = open("app/templates/errors.html", "r")
  page = f.read()
  f.close()
  
  return page
  
if __name__ == '__main__':
  app.run(debug=True)
