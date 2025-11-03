from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient

api_id = "YOUR_TELEGRAM_API"
api_hash = "YOUR_TELEGRAM_HASH"
token = "bot token"
message = "MESSAGE_TO_SEND"

phone_number = "+977 (YOUR_PHONE_NUMBER)"

client = TelegramClient("session", api_id, api_hash)

client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input("Enter the valid code: "))

try:
    user_name = "COLLEAGUES_TG_USERNAME"
    receiver = client.get_entity(user_name)
    user_id = receiver.id
    access_hash = receiver.access_hash

    user_exists = False
    with open("receiver_info.txt", "r") as f:
        for line in f:
            if f"user_id: {user_id}" in line:
                user_exists = True
                break

    if not user_exists:
        with open("receiver_info.txt", "a") as file:
            file.write(f"---{user_name}---\n")
            file.write(f"user_id: {user_id}\n")
            file.write(f"access_hash: {access_hash}\n\n")
        print("User Information Saved Successfully!")
    else:
        print("User Already Exists!")
except Exception as e:
    print(f"Error getting receiver Information: {e}")

try:
    input_peer = InputPeerUser(user_id, access_hash)
    client.send_message(input_peer, message, parse_mode="html")
    print("Message Sent Successfully!")
except Exception as e:
    print(f"Error Sending Message: {e}")

client.disconnect()
