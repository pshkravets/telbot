FROM python:3-slim
WORKDIR /bot
COPY . .

RUN apt-get update
RUN apt-get install -y cron vim-tiny
RUN pip install -r requirements.txt

COPY crontab /etc/cron.d/crontab
RUN sed -i 's/\r$//' /etc/cron.d/crontab
RUN echo "" >> /etc/cron.d/crontab
RUN chmod 0777 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

RUN touch /var/log/cron.log

CMD ["cron", "-f"]

ENV API_ID=you_api_id
ENV API_HASH=your_api_hash
ENV PHONE=your_phone_number
ENV DB_URL=postgresql://user:qwe123@postgre:5432/messagesdb
