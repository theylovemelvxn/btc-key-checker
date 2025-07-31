import requests
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def wif_to_address(wif):
    from bitcoin import privkey_to_address
    return privkey_to_address(wif)

def check_balance(address):
    try:
        response = requests.get(f"https://blockchain.info/q/addressbalance/{address}")
        if response.status_code == 200:
            return int(response.text)
    except:
        return None
    return None

def send_to_sheet(sheet, row):
    sheet.append_row(row)

def main():
    with open("keys.txt", "r") as f:
        wifs = [line.strip() for line in f.readlines()]

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("BTC Positive Balances").sheet1

    for wif in wifs:
        address = wif_to_address(wif)
        balance = check_balance(address)
        if balance and balance > 0:
            print(f"💰 {address} has balance: {balance} satoshis")
            send_to_sheet(sheet, [wif, address, balance])
        time.sleep(1.5)

if __name__ == "__main__":
    main()
