import os

from telethon import TelegramClient

from utils import evaluate_message_list, update_messages

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')

client = TelegramClient('/bot/my_bot.session', api_id, api_hash)


async def fetch_messages():
    me = await client.get_me()
    my_id = me.id
    new_messages = {}
    dialogs = await client.get_dialogs()
    dialog_counter = 0
    for dialog in dialogs:
        if dialog.is_user and not dialog.is_channel and not dialog.entity.bot:
            messages = await client.get_messages(dialog.id, limit=50)
            messages_counter = 0
            for message in messages:
                if message.sender_id != my_id:
                    new_messages[message.id] = {
                        'date': message.date,
                        'text': message.text,
                        'message_id': message.id,
                        'first_name': message.sender.first_name,
                        'last_name': message.sender.last_name,
                        'username': message.sender.username,
                        'phone_number': message.sender.phone
                    }
                    messages_counter += 1
                if messages_counter >= 11:
                    break
            dialog_counter += 1
            if dialog_counter >= 11:
                break
    sorted_messages = evaluate_message_list(new_messages)
    update_messages(sorted_messages)


async def main():
    await client.connect()
    await fetch_messages()

with client:
    client.loop.run_until_complete(main())