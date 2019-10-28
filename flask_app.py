
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
import messageHandler
import MySQLdb as my

def toConnect():
    db = my.connect('BotAsh.mysql.pythonanywhere-services.com', 'BotAsh', '3103Bulat', 'BotAsh$BotDatabase')
    return db

token = '6a045760debd699c34a1155dc5b39fd5b0550dd2e84f83d5824d83f1c5855f1ed2d5a86f9666bdb84029d'
confirmation_token = '1029e14c'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'
