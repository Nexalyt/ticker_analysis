import yfinance as yf
import logging

logger = logging.getLogger(__name__)


def fetch_earnings_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    logger.info(f"Fetching earnings data for {ticker_symbol}")
    
    return ticker.earnings, ticker.quarterly_earnings


def fetch_financial_ratios(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    logger.info(f"Fetching financial ratios for {ticker_symbol}")
    return {
        "P/E Ratio": ticker.info.get('trailingPE'),
        "P/B Ratio": ticker.info.get('priceToBook'),
        "PEG Ratio": ticker.info.get('pegRatio'),
        "Debt to Equity Ratio": ticker.info.get('debtToEquity'),
        "Return on Equity (ROE)": ticker.info.get('returnOnEquity')
    }


def fetch_revenue_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    income_statement = ticker.financials
    quarterly_income_statement = ticker.quarterly_financials

    return {
        "revenue": income_statement.loc['Total Revenue'],
        "net_income": income_statement.loc['Net Income'],
        "quarterly_revenue" : quarterly_income_statement.loc['Total Revenue'],
        "quarterly_net_income": quarterly_income_statement.loc['Net Income']
    }


def compare_peers(peers):
    return {
        peers: yf.Ticker(ticker_symbol).info.get('trailingPE')
        for ticker_symbol in peers
        }
