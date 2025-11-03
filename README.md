# TelegraMsg

Easily send messages to your friends or colleagues on Telegram using this simple Python script powered by Telethon.

## Features

- Sends a message to a specified Telegram user
- Saves receiver information to a file
- Checks if user info already exists before saving

## Getting Started

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Get your Telegram API credentials:**

   - Go to [my.telegram.org](https://my.telegram.org).
   - Log in with your Telegram account.
   - Click on 'API Development Tools'.
   - Fill in the form to create a new application.
   - Copy your `api_id` and `api_hash`.

3. **Configure the script:**

   - Open `TelegraMsg.py` and update these values:
     - `api_id`: Your Telegram API ID
     - `api_hash`: Your Telegram API hash
     - `token`: Your bot token
     - `phone_number`: Your phone number
     - `user_name`: Telegram username of the receiver
     - `message`: Message to send

4. **Run the script:**
   ```bash
   python TelegraMsg.py
   ```

## Requirements

See `requirements.txt` for required packages.

---

Made with ❤️ by Praashon Gautam
