from .utils import load_dataset as _load_dataset


# Load FOREX datasets
FOREX_EURUSD_1H_ASK = _load_dataset('FOREX_EURUSD_1H_ASK', 'Time')

# Load Stocks datasets
STOCKS_GOOGL = _load_dataset('STOCKS_GOOGL', 'Date')
STOCKS_AAPL_1m_2011 = _load_dataset('STOCKS_AAPL_1m_2011', "Date")
