import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json



def get_stock_data(tickers, start_date, end_date):
    """
    Fetches historical stock data for the specified tickers and date range.
    
    Args:
    tickers (list): A list of stock tickers to fetch data for.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD'

    Returns:
    pandas.DataFrame: A DataFrame containing the stock data.
    """
    try:
        data = yf.download(tickers, start=start_date, end=end_date)
        if data.empty:
            raise ValueError("No data recieved. Check the ticker names and date ranges.")
        return data
    except Exception as e:
        print(f"Error while downloading data: {e}")
        return pd.DataFrame()

def get_sp500_tickers():
    """
    Fetches the list of S&P 500 tickers from Wikipedia. Run this function to get the latest list of S&P 500 tickers.

    Returns:
    tickers (list): A list of S&P 500 tickers.
    ticker_to_name (dict): A dictionary mapping tickers to company names.
    """
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})
    tickers = []
    ticker_to_name = {}
    for row in table.findAll('tr')[1:]:
        cells = row.findAll('td')
        ticker = cells[0].text.strip()
        name = cells[1].text.strip()
        tickers.append(ticker)
        ticker_to_name[ticker] = name
    return tickers, ticker_to_name

def generate_stock_sentences(sp500_tickers, start_date, end_date):
    """
    Generates a list of stock tickers sorted by daily percentage change for each trading day in the specified date range.

    Args:
    sp500_tickers (list): A list of S&P 500 stock tickers.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.
    """
    all_ticker_lists = []

    # Get the stock data for all S&P 500 tickers over the specified date range
    stock_data = get_stock_data(sp500_tickers, start_date, end_date)
    if not stock_data.empty:
        for ticker in sp500_tickers:
            stock_data[('percentage_change', ticker)] = (stock_data['Close'][ticker] - stock_data['Open'][ticker]) / stock_data['Open'][ticker]
        for date in stock_data.index:
            data_by_date = stock_data.loc[date]
            sorted_tickers = data_by_date['percentage_change'].sort_values(ascending=False).index.tolist()
            all_ticker_lists.append(sorted_tickers)
    else:
        print("No data to evaluate.")

    # Save the all_ticker_lists to a JSON file
    with open('stock_ticker_lists.json', 'w') as f:
        json.dump(all_ticker_lists, f)

if __name__ == "__main__":
    # Fetch the stock data for the S&P 500 on a specific date
    with open('sp500_tickers.json', 'r') as f:
        sp500_tickers = json.load(f)

    start_date = '2019-01-01'
    end_date = '2024-12-31'

    # Initialize a list to store the ticker lists for each trading day
    generate_stock_sentences(sp500_tickers, start_date, end_date)

