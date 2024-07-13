from pycoingecko import CoinGeckoAPI
from config.config import Config

cg = CoinGeckoAPI(api_key=Config.COINGECKO_API_KEY)

def get_real_time_price(coin_id):
    try:
        price = cg.get_price(ids=coin_id, vs_currencies='usd')[coin_id]['usd']
        return price
    except Exception as e:
        print(f"Error fetching price for {coin_id}: {e}")
        return None