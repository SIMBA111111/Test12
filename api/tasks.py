from celery import shared_task
import requests
from config.celery import celery_app

@celery_app.task(bind=True)
def get_api_data(self):
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=ETH&market=USD&interval=60min&apikey=demo'
    response = requests.get(url)
    r = response.json()
    return r
