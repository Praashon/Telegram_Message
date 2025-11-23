# Telegram Message Sender

A Python script for sending automated messages to Telegram users using the Telethon library. This tool simplifies direct messaging on Telegram by storing user information and enabling programmatic message delivery.

## Features

- **Direct Messaging**: Send messages to any Telegram user by username
- **User Information Storage**: Automatically saves receiver details (user_id and access_hash) to a local file
- **Duplicate Prevention**: Checks if user information already exists before saving
- **Session Management**: Maintains persistent session across multiple runs
- **HTML Formatting Support**: Send messages with HTML formatting
- **Authentication Handling**: Supports phone number authentication with verification codes

## Prerequisites

- Python 3.7+
- Active Telegram account
- Telegram API credentials (api_id and api_hash)
- Phone number registered with Telegram

## Installation

1. **Clone or download this project**

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install Telethon directly:
   ```bash
   pip install telethon
   ```

## Configuration

### 1. Get Your Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Log in with your Telegram account (phone number)
3. Click on **'API Development Tools'**
4. Fill in the application details:
   - App title: Any name (e.g., "My Message Sender")
   - Short name: Any short name
   - Platform: Desktop
5. Click **'Create application'**
6. Copy your `api_id` and `api_hash`

### 2. Update Script Configuration

Open `TelegraMsg.py` and update the following variables:

```python
api_id = "YOUR_API_ID"           # Replace with your API ID
api_hash = "YOUR_API_HASH"       # Replace with your API hash
phone_number = "+1234567890"     # Replace with your phone number (with country code)
user_name = "ReceiverUsername"   # Replace with receiver's Telegram username
message = "Your message here"    # Replace with your message
```

**Note**: The `token` variable in the code is currently unused. For bot operations, you would need a bot token from [@BotFather](https://t.me/botfather).

## Usage

1. **Run the script:**
   ```bash
   python TelegraMsg.py
   ```

2. **First-time authentication:**
   - On first run, you'll receive a verification code on your Telegram app
   - Enter the code when prompted in the terminal
   - A `session.session` file will be created for future authentication

3. **Subsequent runs:**
   - The script will use the saved session
   - No verification code needed unless session expires

## How It Works

1. **Connection**: Establishes connection to Telegram using your API credentials
2. **Authentication**: Verifies your identity using phone number and verification code
3. **User Lookup**: Retrieves receiver's user information by username
4. **Information Storage**: Saves user_id and access_hash to `receiver_info.txt`
5. **Message Delivery**: Sends your message to the specified user
6. **Cleanup**: Disconnects from Telegram gracefully

## Project Structure

```
TelegraMsgSender/
├── TelegraMsg.py           # Main script
├── requirements.txt        # Python dependencies
├── session.session         # Session file (auto-generated)
├── receiver_info.txt       # User information storage (auto-generated)
└── README.md              # This file
```

## Output Files

### receiver_info.txt Format
```
---Username---
user_id: 123456789
access_hash: 9876543210987654321

---Another User---
user_id: 987654321
access_hash: 1234567890123456789
```

## Example Output

```
User Information Saved Successfully!
Message Sent Successfully!
```

Or if user already exists:
```
User Already Exists!
Message Sent Successfully!
```

## HTML Formatting

The script supports HTML formatting in messages. You can use:

```python
message = "<b>Bold text</b>"
message = "<i>Italic text</i>"
message = "<code>Code text</code>"
message = "<a href='https://example.com'>Link text</a>"
```

## Security Considerations

⚠️ **Important Security Notes:**

- **Never share your `api_id` and `api_hash`** publicly
- **Never commit credentials to version control** (Git/GitHub)
- Store sensitive data in environment variables or configuration files
- The `session.session` file contains authentication data - keep it secure
- Regularly rotate API credentials if compromised

### Recommended: Use Environment Variables

```python
import os
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **"Invalid phone number"** | Ensure phone number includes country code (e.g., +1 for US) |
| **"User not found"** | Check if username is correct and public |
| **"Flood wait"** | You've sent too many requests. Wait before trying again |
| **"Session expired"** | Delete `session.session` file and re-authenticate |
| **Connection errors** | Check your internet connection and firewall settings |

## Limitations

- Telegram has rate limits on message sending
- Cannot send messages to users who have blocked you
- Cannot send messages to users with strict privacy settings
- Maximum message length: 4096 characters

## Legal & Ethical Considerations

- Use this tool responsibly and ethically
- Respect Telegram's Terms of Service
- Don't spam or send unsolicited messages
- Obtain consent before automating messages to others
- Be aware of anti-spam regulations in your jurisdiction

## Advanced Usage

### Sending to Multiple Users

Modify the script to iterate through a list of usernames:

```python
user_names = ["user1", "user2", "user3"]
for user_name in user_names:
    # Send message to each user
    # Add delay between messages to avoid rate limiting
```

### Custom Delays

Add delays to prevent rate limiting:

```python
import time
time.sleep(5)  # Wait 5 seconds between messages
```

## Contact

**Made by:** Prashon  
**Email:** mr.prashon@gmail.com

## Contributing

Contributions, issues, and feature requests are welcome!

## License

This project is provided as-is for educational purposes.

## Acknowledgments

- Built with [Telethon](https://github.com/LonamiWebs/Telethon) - Python Telegram client library
- Thanks to the Telegram team for their API

---

*Send messages with ease! 📨*
