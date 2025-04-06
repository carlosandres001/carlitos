import pandas as pd
from ta.trend import MACD
import MetaTrader5 as mt5

class MACDStrategy:
    def __init__(self, symbol):
        self.symbol = symbol
        
    def get_data(self, timeframe=mt5.TIMEFRAME_H1, num_bars=100):
        rates = mt5.copy_rates_from_pos(self.symbol, timeframe, 0, num_bars)
        return pd.DataFrame(rates)
        
    def generate_signal(self):
        df = self.get_data()
        macd = MACD(df['close'], window_fast=12, window_slow=26, window_sign=9)
        
        df['macd'] = macd.macd()
        df['signal'] = macd.macd_signal()
        
        last_row = df.iloc[-1]
        prev_row = df.iloc[-2]
        
        if last_row['macd'] > last_row['signal'] and prev_row['macd'] <= prev_row['signal']:
            return "BUY"
        elif last_row['macd'] < last_row['signal'] and prev_row['macd'] >= prev_row['signal']:
            return "SELL"
        return "HOLD"