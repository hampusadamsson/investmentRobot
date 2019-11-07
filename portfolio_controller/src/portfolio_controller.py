import json

from flask import Flask

from src.Datamanager import Datamanager

app = Flask(__name__)
dm = Datamanager()


@app.route('/health')
def health():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/p/<portfolio_name>')
def get_portfolio(portfolio_name):
    return dm.get_portfolio(portfolio_name)

@app.route('/pnames')
def get_prtfolio_names():
    return dm.get_portfolio_names()

@app.route('/')
def hello_world():
    return dm.find()


app.run(host="0.0.0.0", port=5003)
