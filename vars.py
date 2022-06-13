from tqdm import tqdm
import pandas as pd
from binance.client import Client

BINANCE_API_KEY = r'df78VsoMYywYBGw6Wbx3khlqh0CTHQMxm9emoyhgZSUeSWwYyYrGdfuKR5rfGvbQ'
BINANCE_SECRET_KEY = r'XtmApcUlvJ4lgnxoVuv1iTuHtjvgxnA2KkN3YVI9Alf75mcc2DGg37ydeUkcVqWq'
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
def get_minute_data(symbol, lookback): # lookback = x days in the past
    frame = pd.DataFrame(client.get_historical_klines(symbol, '1m', lookback + ' days ago UTC'))
    return frame
print(get_minute_data('BTCUSDT', '1'))