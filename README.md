# TelegraMsg

A simple Python script to send messages to a Telegram user using the Telethon library.

## Features

- Sends a message to a specified Telegram user
- Saves receiver information to a file
- Checks if user info already exists before saving

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Update the following variables in `TelegraMsg.py`:
   - `api_id`: Your Telegram API ID
   - `api_hash`: Your Telegram API hash
   - `token`: Your bot token
   - `phone_number`: Your phone number
   - `user_name`: Telegram username of the receiver
   - `message`: Message to send
3. Run the script:
   ```bash
   python TelegraMsg.py
   ```

## Requirements

See `requirements.txt` for required packages.

## Made By

Praashon Gautam
