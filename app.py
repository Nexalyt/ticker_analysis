import streamlit as st
from ticker_analysis.data import FetchStock, compare_peers


def main():
    st.title("Stock Analysis Dashboard")

    # Sidebar inputs
    ticker_symbol = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    analysis_type = st.sidebar.selectbox("Select Analysis Type", 
                                         ["Financial Ratios", "Earnings Reports",
                                          "Revenue & Earnings Growth", "Peer Comparison"])
    
    # Fetch stock data
    stock = FetchStock(ticker_symbol)

    if analysis_type == "Earnings Reports":
        try:
            net_income, quarterly_net_income = stock.earnings_data()
            st.write(f"Earnings Data for {ticker_symbol}")
            st.write("Annual Net Income:")
            st.dataframe(net_income)
            st.write("Quarterly Net Income:")
            st.dataframe(quarterly_net_income)
        except Exception as e:
            st.error(f"Error fetching earnings data: {e}")

    elif analysis_type == "Financial Ratios":
        try:
            financial_ratios = stock.financial_ratios()
            st.write(f"Financial Ratios for {ticker_symbol}")
            st.json(financial_ratios)
        except Exception as e:
            st.error(f"Error fetching financial ratios: {e}")

    elif analysis_type == "Revenue & Earnings Growth":
        try:
            revenue_data = stock.revenue_data()
            st.write(f"Revenue Data for {ticker_symbol}")
            st.write("Annual Revenue:")
            st.dataframe(revenue_data['annual_revenue'])
            st.write("Annual Net Income:")
            st.dataframe(revenue_data['annual_net_income'])
            st.write("Quarterly Revenue:")
            st.dataframe(revenue_data['quarterly_revenue'])
            st.write("Quarterly Net Income:")
            st.dataframe(revenue_data['quarterly_net_income'])
        except Exception as e:
            st.error(f"Error fetching revenue data: {e}")

    elif analysis_type == "Peer Comparison":
        try:
            peers = stock.info.get('peers', [])
            if not peers:
                st.warning(f"No peer information available for {ticker_symbol}")
                selected_peers = st.text_input("Enter peer tickers (comma-separated)", "")
                selected_peers = [ticker.strip() for ticker in selected_peers.split(",") if ticker.strip()]
            else:
                selected_peers = st.multiselect("Select peers for comparison", peers, default=peers[:3])

            if selected_peers:
                peers_data = compare_peers(selected_peers)
                st.write(f"Peer Comparison for {ticker_symbol} with {', '.join(selected_peers)}")
                st.json(peers_data)
            else:
                st.warning("No peers selected for comparison.")
                
        except Exception as e:
            st.error(f"Error fetching peer comparison data: {e}")

if __name__ == "__main__":
    main()
