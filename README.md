# 🧾 Receipt Bot

A Discord bot that generates realistic receipt images instantly with one command. No inputs needed — just type `/receipt` and it auto generates everything.

---

## ✨ Features

- 🧾 **One command** — just type `/receipt` and boom, done
- 🏪 **Random stores** — Best Buy, Walmart, Target, Home Depot, CVS, Costco, Walgreens, Rite Aid
- 🛒 **Random items** — pulls realistic items and prices for each store
- 💳 **Random payment** — VISA, Mastercard, AMEX, Discover with random card numbers
- 🔢 **Random transaction IDs** — unique TRANS and MCC codes every time
- 📅 **Real date and time** — always shows the current date and time
- 🖼️ **Image output** — sends a clean PNG receipt image directly in Discord

---

## 🚀 How to install

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/receipt-bot.git
cd receipt-bot
```

**2. Install dependencies**
```bash
python -m pip install discord.py Pillow python-dotenv
```

**3. Create a `.env` file**
```
TOKEN=your_bot_token_here
CLIENT_ID=your_client_id_here
```

**4. Run the bot**
```bash
python bot.py
```

---

## 🔑 How to get your bot token

1. Go to 👉 [discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **New Application** → give it a name
3. Go to **Bot** tab → click **Reset Token** → copy it
4. Go to **OAuth2** → **URL Generator** → check `bot` and `applications.commands`
5. Check `Send Messages` and `Attach Files` permissions
6. Open the generated URL and invite the bot to your server

---

## 💬 How to use

Just type `/receipt` in any channel the bot has access to and it instantly generates a random realistic receipt!

---

## 🏪 Stores included

| Store | Items |
|-------|-------|
| Best Buy | Electronics, cables, accessories |
| Walmart | Groceries, household items |
| Target | Personal care, cleaning supplies |
| Home Depot | Tools, hardware, supplies |
| CVS Pharmacy | Medicine, health products |
| Costco | Bulk groceries, household |
| Walgreens | Medicine, beauty products |
| Rite Aid | Medicine, first aid |

---

## 🛠️ Tech Stack

- Python 3.12
- discord.py
- Pillow (image generation)
- python-dotenv

---

## ⚠️ Note

Keep your bot token private and never share it publicly. If it gets leaked, reset it immediately at the Discord Developer Portal.
