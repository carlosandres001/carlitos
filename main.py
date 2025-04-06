import MetaTrader5 as mt5
from strategy import MACDStrategy
from risk_manager import RiskManager
from news_filter import NewsFilter
import configparser
import time

def initialize_mt5():
    if not mt5.initialize():
        print("Error al conectar con MT5")
        return False
    return True

def run_bot():
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    
    if not initialize_mt5():
        return
    
    risk_manager = RiskManager()
    news_filter = NewsFilter()
    
    print("=== BOT FTMO INICIADO ===")
    
    try:
        while True:
            if news_filter.is_news_time():
                print("🛑 Pausado por noticia importante")
                time.sleep(300)  # Espera 5 minutos
                continue
                
            for pair in config['PAIRS']['allowed'].split(','):
                strategy = MACDStrategy(pair)
                signal = strategy.generate_signal()
                
                if signal != "HOLD":
                    print(f"Señal {signal} en {pair}")
                    # Aquí iría la lógica para ejecutar órdenes
                    
            time.sleep(60)  # Revisa cada minuto
            
    except KeyboardInterrupt:
        print("\n=== BOT DETENIDO ===")
    finally:
        mt5.shutdown()

if __name__ == "__main__":
    run_bot()