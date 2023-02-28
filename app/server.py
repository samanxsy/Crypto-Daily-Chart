from flask import Flask, request, redirect
import app.cryptochart as cryptochart


app = Flask("Crypto Daily Charts", static_folder="./app/static")


@app.route('/')
def home():
    """Home page route"""
    page = ""
    with open("./app/templates/layout.html", "r") as f:
        page = f.read()

    return page


@app.route('/calculate', methods=['GET'])
def chart():
    """Calculate route"""
    page = ""
    with open("./app/templates/layout.html", "r") as f:
        page = f.read()

    coin = request.args.get("market")
    days = request.args.get("days")

    try:
        calculate = cryptochart.crypto_chart(coin, days)
        calculate = calculate
    except ValueError:
        return redirect('/error')

    return page


@app.route('/error')
def error():
    """Error route"""
    page = ""
    with open("./app/templates/errors.html", "r") as f:
        page = f.read()

    return page
