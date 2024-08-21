import yfinance as yf
import logging
import os
import pickle

logger = logging.getLogger(__name__)

CACHE_DIR = ".data"

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def cache_data(func):
    """Decorator to cache data in the .data/ directory."""
    def wrapper(self, *args, **kwargs):
        cache_key = f"{func.__name__}_{self.ticker_symbol}.pkl"
        cache_path = os.path.join(CACHE_DIR, cache_key)
        if os.path.exists(cache_path):
            with open(cache_path, "rb") as f:
                data = pickle.load(f)
            logger.info(f"Loaded data from cache: {cache_path}")
        else:
            data = func(self, *args, **kwargs)
            with open(cache_path, "wb") as f:
                pickle.dump(data, f)
            logger.info(f"Saved data to cache: {cache_path}")
        return data
    return wrapper

def compare_peers(peers) -> dict:
    """Compare financial ratios of a stock with its peers"""
    return {
        ticker_symbol: yf.Ticker(ticker_symbol).info.get('trailingPE')
        for ticker_symbol in peers
    }

class FetchStock:
    def __init__(self, ticker_symbol) -> None:
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)
        self.info = self.ticker.info
        self.financials = {}
        if 'Total Revenue' in self.ticker.financials:
            self.financials["Total Revenue"] = self.ticker.financials.loc['Total Revenue']
        if 'Research And Development' in self.ticker.financials:
            self.financials["Research Development"] = self.ticker.financials.loc['Research And Development']
        if 'Operating Expenses' in self.ticker.financials:
            self.financials["Operating Expenses"] = self.ticker.financials.loc['Operating Expenses']
        if 'Operating Income' in self.ticker.financials:
            self.financials["Operating Income"] = self.ticker.financials.loc['Operating Income']
        if 'Net Income' in self.ticker.financials:
            self.financials["Net Income"] = self.ticker.financials.loc['Net Income']
        if 'Gross Profit' in self.ticker.financials:
            self.financials["Gross Profit"] = self.ticker.financials.loc['Gross Profit']
        if 'Cost of Revenue' in self.ticker.financials:
            self.financials["Cost of Revenue"] = self.ticker.financials.loc['Cost of Revenue']

        self.earnings = {
            "annual": self.ticker.financials.loc['Net Income'],
            "quarterly": self.ticker.quarterly_financials.loc['Net Income'],
        }

    @cache_data
    def earnings_data(self) -> tuple:
        """Fetch earnings data for the stock"""
        logger.info(f"Fetching earnings data for {self.ticker_symbol}")
        return self.earnings['annual'], self.earnings['quarterly']

    @cache_data
    def financial_ratios(self) -> dict:
        """Fetch financial ratios for the stock"""
        logger.info(f"Fetching financial ratios for {self.ticker_symbol}")
        return {
            "P/E Ratio": self.info.get('trailingPE'),
            "P/B Ratio": self.info.get('priceToBook'),
            "PEG Ratio": self.info.get('pegRatio'),
            "Debt to Equity Ratio": self.info.get('debtToEquity'),
            "Return on Equity (ROE)": self.info.get('returnOnEquity'),
            "Return on Assets (ROA)": self.info.get('returnOnAssets'),
        }

    @cache_data
    def revenue_data(self) -> dict:
        """Fetch revenue data for the stock"""
        logger.info(f"Fetching revenue data for {self.ticker_symbol}")
        return {
            "annual_revenue": self.financials['Total Revenue'],
            "annual_net_income": self.financials['Net Income'],
            "quarterly_revenue": self.ticker.quarterly_financials.loc['Total Revenue'],
            "quarterly_net_income": self.ticker.quarterly_financials.loc['Net Income']
        }
