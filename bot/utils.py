from itertools import islice
from models import session, Message


def evaluate_message_list(messages):
    sorted_messages = dict(sorted(messages.items(), key=lambda item: item[1]['date'], reverse=True))
    return dict(islice(sorted_messages.items(), 10))


def update_messages(messages):
    session.query(Message).delete()
    session.commit()
    for message in messages.values():
        new_message = Message(
            message_id=message['message_id'],
            date=message['date'],
            text=message['text'],
            first_name=message['first_name'],
            last_name=message['last_name'],
            username=message['username'],
            phone_number=message['phone_number']
        )
        session.add(new_message)
        session.commit()