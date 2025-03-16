import requests
from celery import shared_task
from django.utils.timezone import now
from .models import Organization, CryptoPrice
from decimal import Decimal
def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return {
        "BTC": data.get("bitcoin", {}).get("usd"),
        "ETH": data.get("ethereum", {}).get("usd")
    }





@shared_task(name="crypto_app.tasks.update_crypto_prices")
def update_crypto_prices():
    """Update crypto prices for all organizations."""
    try:
        prices = fetch_crypto_prices()
        print("Fetched Prices:", prices)  # Debugging print
    
        if not prices:
            raise ValueError("Fetched prices are empty")

        organizations = Organization.objects.all()
    
        for org in organizations:
            if "BTC" in prices and prices["BTC"] is not None:
                CryptoPrice.objects.create(
                    org=org,
                    symbol="BTC",
                    price=Decimal(str(prices["BTC"]))
                )

            if "ETH" in prices and prices["ETH"] is not None:
                CryptoPrice.objects.create(
                    org=org,
                    symbol="ETH",
                    price=Decimal(str(prices["ETH"]))
                )

        return f"Updated crypto prices for {organizations.count()} organizations"
    
    except Exception as e:
        print(f"Error updating crypto prices: {str(e)}")
        return f"Error updating crypto prices: {str(e)}"
