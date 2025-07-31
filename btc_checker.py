import time
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bitcoin import decode_privkey, privtopub, pubtoaddr

def wif_to_address(wif):
    try:
        priv_key = decode_privkey(wif, 'wif')
        pub_key = privtopub(priv_key)
        return pubtoaddr(pub_key)
    except Exception as e:
        print(f"❌ Conversion failed for {wif}: {e}")
        return None

def check_balance(address):
    try:
        response = requests.get(f"https://blockchain.info/q/addressbalance/{address}")
        if response.status_code == 200:
            return int(response.text)
    except Exception as e:
        print(f"❌ Failed to check balance for {address}: {e}")
    return None

def main():
    # Setup Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Access source and destination spreadsheets
    source_sheet = client.open("Bitcoin_WIF_Keys").sheet1
    dest_sheet = client.open("BTC Positive Balances").sheet1

    wifs = source_sheet.col_values(1)  # Read WIFs from column A

    for wif in wifs:
        if not wif.strip(): continue  # Skip empty lines
        address = wif_to_address(wif)
        if address:
            balance = check_balance(address)
            if balance and balance > 0:
                print(f"✅ Found balance for {address}: {balance} sats")
                dest_sheet.append_row([wif, address, balance])
            else:
                print(f"🪙 No balance for {address}")
        else:
            print(f"⚠️ Skipped invalid WIF: {wif}")
        time.sleep(1.5)

if __name__ == "__main__":
    main()
