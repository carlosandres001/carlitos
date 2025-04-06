import configparser
from datetime import datetime

class RiskManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/config.ini')
        self.reset_daily()
        
    def reset_daily(self):
        self.daily_pnl = 0
        self.drawdown = 0
        
    def calculate_position_size(self, balance, stop_loss_pips):
        risk_amount = (float(self.config['FTMO']['risk_per_day']) / 100) * balance
        return round(risk_amount / (stop_loss_pips * 10), 2)  # Asume $10/pip
        
    def check_limits(self):
        if self.drawdown >= float(self.config['FTMO']['max_drawdown']):
            return "STOP_TRADING"
        return "CONTINUE"