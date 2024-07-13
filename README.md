# Solana Meme Coin Price Predictor

This project allows users to make price predictions for Solana meme coins using real-time data from CoinGecko.

## Setup

1. Clone the repository
2. Install dependencies:
pip install -r requirements.txt

3. (Optional) Create a `.env` file in the root directory and add your CoinGecko API key:
COINGECKO_API_KEY=your_api_key_here

Note: This is optional for the free tier of CoinGecko API.

## Usage

Run the application:
python main.py

Follow the on-screen instructions to:
1. Enter a Solana meme coin's CoinGecko ID
2. Predict whether the price will be higher or lower
3. Set a timeframe for your prediction

The program will wait for the prediction timeframe to end and then show the results.

## Note

This is a basic implementation for educational purposes. It does not involve real money or trading. Always do your own research before making any financial decisions.