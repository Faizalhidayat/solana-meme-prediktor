from app.predictor import SolanaMemePredictor
from app.utils import get_real_time_price
import time

def print_prediction_result(pred):
    print(f"\nPrediction Result for {pred['coin_id']}:")
    print(f"Start price: ${pred['start_price']:.6f}")
    print(f"End price: ${pred['end_price']:.6f}")
    print(f"Prediction: {pred['prediction']}")
    print(f"Actual: {pred['result']}")
    print(f"Outcome: {pred['outcome']}")

def main():
    predictor = SolanaMemePredictor()

    while True:
        print("\n--- Solana Meme Coin Price Predictor ---")
        coin_id = input("Enter the CoinGecko ID of the Solana meme coin (e.g., 'bonk', 'samoyedcoin'): ").strip().lower()
        
        current_price = get_real_time_price(coin_id)
        if not current_price:
            print(f"Could not find coin with ID '{coin_id}'. Please try again.")
            continue

        print(f"Current price of {coin_id}: ${current_price:.6f}")

        prediction = input("Do you think the price will be 'higher' or 'lower' in the future? ").strip().lower()
        if prediction not in ['higher', 'lower']:
            print("Invalid prediction. Please enter 'higher' or 'lower'.")
            continue

        try:
            timeframe = int(input("Enter the prediction timeframe in minutes: "))
        except ValueError:
            print("Invalid timeframe. Please enter a number.")
            continue

        if predictor.make_prediction(coin_id, prediction, timeframe):
            print("Prediction added successfully!")
        else:
            print("Failed to add prediction. Please try again.")

        choice = input("\nDo you want to make another prediction? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

    print("\nWaiting for predictions to resolve...")
    while predictor.predictions:
        resolved = predictor.resolve_predictions()
        for pred in resolved:
            print_prediction_result(pred)
        time.sleep(60)  # Check every minute

    print("\nAll predictions have been resolved. Thank you for using Solana Meme Coin Price Predictor!")

if __name__ == "__main__":
    main()