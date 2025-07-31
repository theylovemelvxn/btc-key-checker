# 🔐 BTC Key Checker

This Python tool checks a list of Bitcoin WIF (Wallet Import Format) private keys to see if any of them have a positive BTC balance. If any are found, they are logged and saved to Google Sheets.

## 🧰 Features

- Validates and converts Bitcoin WIF keys
- Checks balances via Blockstream API
- Logs all results (including positives) to a Google Sheet
- Uses Google Sheets API for storage

---

## ⚙️ Installation

1. **Clone this repository**:
```bash
git clone https://github.com/theylovemelvxn/btc-key-checker.git
cd btc-key-checker

	2.	Install dependencies:

pip3 install -r requirements.txt

🧪 Usage
	1.	Add your WIF keys to the keys.txt file (one per line).
	2.	Download your service account JSON from Google Cloud, rename it to credentials.json, and place it in the project root.
	3.	Share your Google Sheet with the service account email.
	4.	Run the script:

python3 btc_checker.py


⚠️ Legal Disclaimer

This tool is strictly intended for educational, research, and cybersecurity audit purposes only.

Accessing cryptocurrency wallets that do not belong to you — without explicit permission — is strictly illegal in most jurisdictions. This tool must only be used:

- On your **own keys or wallets**
- In **controlled environments** (e.g. security labs or simulations)
- For ethical hacking and academic purposes

---

 📜 Legal References

- Article 323-1 of the French Penal Code** – Unauthorized access to automated data processing systems is punishable by law.
- Computer Fraud and Abuse Act (CFAA - USA, 18 U.S. Code § 1030) – Criminalizes unauthorized access to computer systems.
- General Data Protection Regulation (GDPR - EU) – Applies if sensitive data is collected or processed.
- United Nations Convention on Cybercrime (Budapest Convention, 2001) – International treaty addressing cybercrime and unauthorized access.
---

if you want to tip : bc1qvl3792dw0rza9l9lrj37n654azrxfj8jth4694
