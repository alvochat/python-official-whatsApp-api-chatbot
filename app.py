from flask import Flask, request, jsonify
from alvochatbot import alvochatChatBot
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = alvochatChatBot(request.json)
        return bot.Processingـincomingـmessages()

if(__name__) == '__main__':
    app.run()
