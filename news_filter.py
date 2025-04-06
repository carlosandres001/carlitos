import requests
import configparser
from datetime import datetime, timedelta

class NewsFilter:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/config.ini')
        self.api_url = "https://economic-calendar-api.com/v1/events"
        
    def get_high_impact_events(self):
        today = datetime.utcnow().date()
        params = {
            "date": today.strftime("%Y-%m-%d"),
            "importance": "high",
            "api_key": self.config['NEWS']['api_key']
        }
        response = requests.get(self.api_url, params=params)
        return response.json().get('events', [])
        
    def is_news_time(self):
        events = self.get_high_impact_events()
        now = datetime.utcnow()
        for event in events:
            event_time = datetime.strptime(event['time'], "%Y-%m-%d %H:%M:%S")
            if (event_time - timedelta(minutes=int(self.config['NEWS']['disable_minutes_before']))) <= now <= event_time:
                return True
        return False