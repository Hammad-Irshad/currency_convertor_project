import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "currency-converter18.p.rapidapi.com")

API_URL = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

if not RAPIDAPI_KEY:
    raise RuntimeError("RAPIDAPI_KEY not found in .env")

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST,
}

def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    params = {"from": from_currency, "to": to_currency, "amount": amount}
    r = requests.get(API_URL, headers=HEADERS, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()

    if "result" not in data or "convertedAmount" not in data["result"]:
        raise ValueError(f"Unexpected API response: {data}")

    return float(data["result"]["convertedAmount"])
