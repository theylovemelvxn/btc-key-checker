# 🔐 BTC Key Checker (Google Sheets Edition)

This Python tool checks Bitcoin private keys (WIF format) directly from a **Google Sheet** (auto-filled via n8n), verifies their balance, and logs positive results in a **second Google Sheet**.

---

## 🧰 Features

- ✅ Automatically reads WIF keys from a source Google Sheet (e.g. populated by `n8n`)
- 🔄 Converts WIF to Bitcoin addresses
- 💰 Checks balances using `blockchain.info`
- 📝 Logs only **positive balances** to a separate Google Sheet
- 🔐 Uses OAuth2 with a `credentials.json` file for Google Sheets API access

---

## ⚙️ Installation

1. **Clone this repository**:
```bash
git clone https://github.com/theylovemelvxn/btc-key-checker.git
cd btc-key-checker

	2.	Install dependencies:

pip3 install -r requirements.txt

🧪 Usage
	1.	In Google Cloud Console:
	•	Create a service account and download the credentials file as credentials.json
	•	Share both Google Sheets with the service account email (as Editor)
	2.	In Google Sheets:
	•	Use one sheet (e.g. Bitcoin_WIF_Keys) where n8n or other automation tools paste WIF keys into column A
	•	Prepare another sheet (e.g. BTC Positive Balances) where positive results will be logged

3.	Launch the checker:
python3 btc_checker.py


📂 Output Format (in BTC Positive Balances)

WIF Key
Bitcoin Address
Balance (in satoshis)
5J…
1A…
123456


⚠️ Legal Disclaimer

This tool is strictly for educational, research, or auditing purposes.
Never use this tool on addresses or keys you don’t own.

Misuse of this tool is your sole responsibility and may constitute a criminal offense.

⸻

📜 Legal References
	•	French Penal Code, Article 323-1 – Unauthorized access to IT systems
	•	CFAA (U.S. Code § 1030) – Criminalizes unauthorized system access
	•	GDPR (EU) – Applies to processing personal or sensitive data
	•	Budapest Convention (2001) – International law on cybercrime

⸻

💸 Tip Jar (BTC ADRESS)

If this helped you or saved you time:

bc1qvl3792dw0rza9l9lrj37n654azrxfj8jth4694

🙏 Thanks for your support!

