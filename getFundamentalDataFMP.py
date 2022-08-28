# -*- coding: utf-8 -*-
"""

Get fundamental data
@author: Adam Getbags

Data provided by Financial Modeling Prep
https://site.financialmodelingprep.com/developer/docs/

Python API wrapper by
https://github.com/JerBouma/FundamentalAnalysis

"""

#pip install fundamentalanalysis

#import modules 
import pandas as pd
import fundamentalanalysis as fa
from fmpSecret import fmpSecret as api_key

ticker = "AAPL"

#show the available tickers
allTickers = fa.available_companies(api_key)

#get unique exchange names
allExchanges = allTickers.exchangeShortName.unique()
print(allExchanges)

#get all ticker data on single exhange
tickersOnExchange = allTickers[allTickers.exchangeShortName == 'NASDAQ']
print(tickersOnExchange)

#get all ticker data on multiple exhanges
tickersOnExchanges = allTickers[(
           allTickers.exchangeShortName == 'NASDAQ') | (
           allTickers.exchangeShortName == 'NYSE') | (
           allTickers.exchangeShortName == 'AMEX')]
print(tickersOnExchanges)

#accessing the stock symbols 
symbols = list(tickersOnExchanges.index)
print(symbols)

#collect general company information
profile = fa.profile(ticker, api_key)
print(profile)

#get last dividend 
lastDiv = profile.loc['lastDiv'][0]
print(lastDiv)

#get beta
beta = profile.loc['beta'][0]
print(beta)

#collect recent company quotes // techinical data // earnings date
quotes = fa.quote(ticker, api_key)
print(quotes)

#collect market cap and enterprise value
enterprise_value = fa.enterprise(ticker, api_key)

#get specific year enterprise value
evByYear = enterprise_value['2021'].loc['enterpriseValue']

#show recommendations of Analysts
ratings = fa.rating(ticker, api_key)
print(ratings)

#obtain DCFs over time
dcf_annually = fa.discounted_cash_flow(ticker, api_key, period="annual")
print(dcf_annually)

#collect the Balance Sheet statements // columns are years
balance_sheet_annually = fa.balance_sheet_statement(
                          ticker, api_key, period="annual")

#individual balance sheet items by year
print(list(balance_sheet_annually['2021'].index))

#collect the Income Statements // columns are years
income_statement_annually = fa.income_statement(
                            ticker, api_key, period="annual")

#individual income statement items by year
print(list(income_statement_annually['2021'].index))
print('- - -')
print(income_statement_annually['2021'].loc['netIncomeRatio'])

#collect the Cash Flow Statements // columns are years
cash_flow_statement_annually = fa.cash_flow_statement(
                                ticker, api_key, period="annual")

#individual income statement items by year
print(list(cash_flow_statement_annually['2021'].index))

#free cash flow 
fcf = cash_flow_statement_annually['2021'].loc['freeCashFlow']
print(fcf)

#show Key Metrics // columns are years
key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
print(key_metrics_annually)

#return on invested capital, etc.
roic = key_metrics_annually['2021'].loc['roic']
print(roic)

#show a large set of in-depth ratios // columns are years 
financial_ratios_annually = fa.financial_ratios(
                               ticker, api_key, period="annual")

print(financial_ratios_annually['2021'])

ccc = financial_ratios_annually['2021'].loc['cashConversionCycle']
print(ccc)

#show the growth of the company
growth_annually = fa.financial_statement_growth(
                   ticker, api_key, period="annual")
print(growth_annually)

#download general stock data // YAHOO DATA
stock_data = fa.stock_data(ticker, period="max", interval="1d")

#download detailed stock data // FMP DATA
stock_data_detailed = fa.stock_data_detailed(
                        ticker, api_key, begin="2000-01-01", end="2020-01-01")
print(stock_data_detailed.columns)

# download dividend history // FMP DATA
dividends = fa.stock_dividend(
            ticker, api_key, begin="2000-01-01", end="2020-01-01")
print(dividends.adjDividend)