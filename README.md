<H3>Hello everyone!</H3> 
<p>
Here you can look how to launch this project.
First of all we need to clone repository on our local machine <br> 
<pre><code>git clone https://github.com/pshkravets/telbot.git</code></pre>
Then we need to visit https://my.telegram.org/ and create there app and get their configurations:
api_id, api_hash (Do not show it to anyone!) and put it in our Dockerfiles 
in tellbot/bot , last_messages directions:
<pre><code>ENV API_ID=you_api_id #<-- instead of you_api_id put your actual api_id
ENV API_HASH=your_api_hash #<-- api_hash
ENV PHONE=your_phone_number #<-- your_phone number you are registered in Telegram
</code></pre>Also you should change this values in tellbot/bot/crontab fil:
<pre><code>
* * * * * API_ID='your_api_id' API_HASH='your_api_hash' PHONE='your_phone'
</code></pre>
Our project is ready to launch so lets do it! <br>
In our root repository start command:
<pre><code>docker-compose up
</code></pre>
After our container is started you should you need to start script main.py on 
your own. We need to do it to session file was created so our crontab file could
start script manually.
So, come to our bot image and open a terminal in container (telbot-bot -> Exec -> open in terminal) 
Input 
<pre><code>python3 main.py</code></pre>
It'll asc your to input your phone number:
<pre><code>Please enter your phone (or bot token):
</code></pre>
So just input your number in format: 380********* <br>
Then you'll receive confirmation code to your Telegram account and It'll ask 
you to confirm it:
<pre><code>Please enter the code you received:
</code></pre>
So just input it over there and hit enter ;) <br>
You need to do it only once when you start project so don't worry, 
It won't bother you in future.
Well... Here we are, you can come to bot t.me/tt_last_messages_bot and start work with it (/start /help)
Thanks for your attention and good luck! :) 
</p>
