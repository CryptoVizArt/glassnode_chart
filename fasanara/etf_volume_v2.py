import pandas as pd
import numpy as np
import requests
import yfinance as yf
from datetime import date, datetime, time, timedelta

today = datetime.combine(date.today(), time())


def stock_ticker(ticker):
    response = yf.download(ticker, start="2018-01-01", end=today)
    response['date'] = pd.to_datetime(response.index, utc=True)
    response = response.set_index('date', drop=False)
    response.index.name = ''
    return response


def btc_etf_tickers():
    assets = [
        'GBTC', 'BTC', 'IBIT', 'FBTC', 'ARKB',
        'BITB', 'BTCO', 'HODL', 'BRRR',
        'EZBC', 'BTCW'
    ]

    # Get Bitcoin price data first
    btc_data = stock_ticker('BTC-USD')
    response = pd.DataFrame()
    response['date'] = btc_data['date']
    response['BTC_USD_Price'] = btc_data['Close']
    response['AGG_Volume'] = 0

    # Process ETF data
    for i in assets:
        etf = stock_ticker(i)
        vol_name = i + '_Volume'
        price_name = i + '_Price'
        response[price_name] = etf['Close']
        response[vol_name] = etf['Volume'] * etf['Close']
        response[vol_name] = response[vol_name].fillna(0)
        response['AGG_Volume'] = response['AGG_Volume'] + response[vol_name]

    filepath = ''
    response.to_csv(filepath + 'etf_volume_v2.csv')

    return response


df = btc_etf_tickers()