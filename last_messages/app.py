import os

from telethon import TelegramClient, events
from sqlalchemy import asc

from models import Message, session


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = f"{os.getenv('BOT_TOKEN')}"
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi there! Input /new_messages to show list of new messages')


@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    help_text = (
        "Here are the commands you can use:\n"
        "/new_messages - list of new messages \n"
    )
    await event.respond(help_text)


@client.on(events.NewMessage(pattern='/new_messages'))
async def message_list(event):
    messages = session.query(Message).order_by(asc(Message.date))
    for message in messages:
        await event.respond(
                f'first name: {message.first_name}\n'
                f'text: {message.text}\n'
                f'datetime: {message.date}\n'
                f'last name: {message.last_name}\n'
                f'username: {message.username}\n'
                f'message id: {message.message_id}\n'
        )


client.start()
client.run_until_disconnected()