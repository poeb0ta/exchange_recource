import os
from dotenv import load_dotenv
import requests

load_dotenv()

key=os.getenv("RATES_API_KEY")


def get_rates():
    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/RUB"
    response = requests.get(url)
    if response.status_code==200:
        data=response.json()
        conversion_rates=data["conversion_rates"]
        return {
            "rub": 1.0,
            "usd" : 1/conversion_rates["USD"],
            "eur" : 1/conversion_rates["EUR"],
            "CNY" : 1/conversion_rates["CNY"]
        }
    else:
        print("ERROR",response.status_code)
        return None

