import requests

def get_sol_balance(address: str):
    response = requests.get(f"https://api.mainnet-beta.solana.com/account/{address}")
    return response.json().get("balance")