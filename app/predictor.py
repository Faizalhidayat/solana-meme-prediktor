from datetime import datetime, timedelta
from app.utils import get_real_time_price

class SolanaMemePredictor:
    def __init__(self):
        self.predictions = []

    def make_prediction(self, coin_id, prediction, timeframe_minutes):
        current_price = get_real_time_price(coin_id)
        if not current_price:
            print(f"Unable to fetch current price for {coin_id}.")
            return False

        end_time = datetime.now() + timedelta(minutes=timeframe_minutes)
        
        self.predictions.append({
            "coin_id": coin_id,
            "prediction": prediction,
            "start_price": current_price,
            "end_time": end_time
        })
        
        print(f"Prediction made: {coin_id} will be {prediction} than ${current_price:.6f} at {end_time}")
        return True

    def resolve_predictions(self):
        current_time = datetime.now()
        resolved = []
        for pred in self.predictions[:]:
            if current_time >= pred["end_time"]:
                end_price = get_real_time_price(pred['coin_id'])
                if not end_price:
                    print(f"Unable to fetch end price for {pred['coin_id']}. Skipping resolution.")
                    continue

                result = "higher" if end_price > pred["start_price"] else "lower"
                is_correct = result == pred["prediction"]

                outcome = "Correct" if is_correct else "Incorrect"
                
                resolved.append({
                    "coin_id": pred['coin_id'],
                    "start_price": pred['start_price'],
                    "end_price": end_price,
                    "prediction": pred['prediction'],
                    "result": result,
                    "outcome": outcome
                })
                
                self.predictions.remove(pred)
        
        return resolved