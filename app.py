import streamlit as st

from ticker_analysis.data import fetch_earnings_data

def main():
    st.title("Stock Analysis Dashboard")

    # Sidebar inputs
    ticker_symbol = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    analysis_type = st.sidebar.selectbox("Select Analysis Type", 
                                         ["Financial Ratios", "Earnings Reports", "Revenue & Earnings Growth", "Peer Comparison"])
    
    if analysis_type == "Earnings Reports":
        net_income, quarterly_net_income = fetch_earnings_data(ticker_symbol)
        st.write(f"Earnings Data for {ticker_symbol}")
        st.write("Annual Net Income:")
        st.dataframe(net_income)
        st.write("Quarterly Net Income:")
        st.dataframe(quarterly_net_income)

if __name__ == "__main__":
    main()
