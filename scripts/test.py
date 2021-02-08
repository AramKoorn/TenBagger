print("Hello world")
import yfinance as yf
from yahoo_earnings_calendar import YahooEarningsCalendar
import pandas as pd
import datetime

print(yf.Ticker('HITIF').history(period="5d"))
print(yf.Ticker('HITIF').info)
# yec = YahooEarningsCalendar()
# report_date = datetime.datetime.now().date() - 2
# earnings_list = yec.earnings_on(report_date)
#
# # saving the data in a pandas DataFrame
# earnings_df = pd.DataFrame(earnings_list)
# earnings_df.head()
#
# #from urllib import urlopen
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# url = 'https://www.marketwatch.com/investing/stock/abbv/financials'
# text_soup = BeautifulSoup(urlopen(url).read()) #read in
#
# titles = text_soup.findAll('td', {'class': 'rowTitle'})
# for title in titles:
#     if 'EPS (Basic)' in title.text:
#         print([td.text for td in title.findNextSiblings(attrs={'class': 'valueCell'}) if td.text])



df_calendar = pd.read_html(r'https://www.marketwatch.com/investing/stock/abbv/financials/income/quarter')

df_all_est = []

for ticker in df_calendar[0]['Symbol'].tolist():
    try:
        print(f'Downloading Estimates for {ticker}')

        df_est = pd.read_html(r'https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}')
        eps_est, rev_est = df_est[0], df_est[1]

        rev_est = rev_est.melt(id_vars=['Revenue Estimate'],var_name='Period')
        rev_est['Ticker'] = ticker
        rev_est['Item'] = "REVENUES"
        rev_est.rename(index=str, columns={"Revenue Estimate": "Statistic"}, inplace=True)
        rev_est['DateTime'] = str(datetime.utcnow())
        df_all_est.append(rev_est)

        eps_est = eps_est.melt(id_vars=['Earnings Estimate'],var_name='Period')
        eps_est['Ticker'] = ticker
        eps_est['Item'] = "EPS"
        eps_est.rename(index=str, columns={"Earnings Estimate": "Statistic"}, inplace=True)
        eps_est['DateTime'] = str(datetime.utcnow())
        df_all_est.append(eps_est)

        print(eps_est.append(rev_est).to_string())

    except Exception as e:
        print(f"Error Downloading {ticker} \n{e}\n")

df_all_merged = pd.concat(df_all_est)
df_all_merged.reset_index(drop=True, inplace=True)
df_all_merged = df_all_merged.T.reindex(['DateTime', 'Ticker', 'Item', 'Statistic', 'Period', 'value']).T
