import yfinance as yf
import pandas as pd
import datetime
import re
from datetime import date

#Today Date&Time
past = datetime.datetime.now() - datetime.timedelta(days=5*365)
today = date.today()

#Downloads Data from YahooFinance
dadosPETR4 = yf.download('PETR4.SA',start=past, end=today, actions=True)
dadosBBAS3 = yf.download('BBAS3.SA',start=past, end=today, actions=True)
dadosCXSE3 = yf.download('CXSE3.SA',start=past, end=today, actions=True)
dadosBMGB4 = yf.download('BMGB4.SA',start=past, end=today, actions=True)
dadosSANB4 = yf.download('SANB4.SA',start=past, end=today, actions=True)

#Data Array
DividendosPETR4 = dadosPETR4.loc[dadosPETR4.Dividends != 0]
DividendosBBAS3 = dadosBBAS3.loc[dadosBBAS3.Dividends != 0]
DividendosCXSE3 = dadosCXSE3.loc[dadosCXSE3.Dividends != 0]
DividendosBMGB4 = dadosBMGB4.loc[dadosBMGB4.Dividends != 0]
DividendosSANB4 = dadosSANB4.loc[dadosSANB4.Dividends != 0]

#Regex Replace Filter
result = re.sub(r'\d{4}-\d{2}-\d{2}', r'\g<0>'+'       R$', str((DividendosPETR4['Dividends']))) 
result2 = re.sub(r'\d{4}-\d{2}-\d{2}', r'\g<0>'+'       R$', str((DividendosBBAS3['Dividends'])))
result3 = re.sub(r'\d{4}-\d{2}-\d{2}', r'\g<0>'+'       R$', str((DividendosCXSE3['Dividends'])))
result4 = re.sub(r'\d{4}-\d{2}-\d{2}', r'\g<0>'+'       R$', str((DividendosBMGB4['Dividends'])))
result5 = re.sub(r'\d{4}-\d{2}-\d{2}', r'\g<0>'+'       R$', str((DividendosSANB4['Dividends'])))

#Print the result:
#print(DividendosBBAS3['Dividends'])
print("PETR4:")
print(result)
print("BBAS3:")
print(result2)
print("CXSE3:")
print(result3)
print("BMGB4:")
print(result4)
print("SANB4:")
print(result5)