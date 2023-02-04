# [alvochat.com](https://alvochat.com/?utm_source=github&utm_medium=python&utm_campaign=chatbot) WhatsApp Bot using official WhatsApp API and alvochat
Demo WhatsApp API ChatBot using [alvochat API](https://alvochat.com/?utm_source=github&utm_medium=python&utm_campaign=chatbot) with python.
# Opportunities and tasks:
- The output of the command list .
- The output of the server time of the bot running on .
- Sending image to phone number or group .
- Sending audio file.
- Sending Video File.
- Sending contact.
- sending document.
- sending sticker.
- sending location.
- sending whatsapp interactive list.
- sending whatsapp interactive buttons.


# Getting Started
- alvochat account is required to run examples. Log in or Create Account if you don't have one [alvochat.com](https://alvochat.com/?utm_source=github&utm_medium=python&utm_campaign=chatbot).
- go to your instance or Create one if you haven't already.

## install flask
the WebHook URL must be provided for the server to trigger our script for incoming messages. we will deployed the server using the FLASK microframework. The FLASK server allows us to conveniently process incoming requests.

> pip install flask

Then clone the repository for yourself.
Then go to the **alvochatbot.py** file and replace the alvochatAPIUrl and instance token.

## install ngrok
for local development purposes, a tunneling service is required. This example uses ngrok , You can download ngrok from here : [ngrok](https://ngrok.com/download) .




# Run a chatbot

## Run FLASK server  
> flask run

## Run ngrok

### Run ngrok For Windows :
> ngrok http 5000

### Run ngrok For Mac :
> ./ngrok http 5000

# Functions
## send_request 
Used to send requests to the alvochat API
```python
    def send_requests(self, type, data):
        url = f"{self.alvochatAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()
```
- **type** determines the type message .
- **data** contains the data required for sending requests.

## send_message
Used to send WhatsApp text messages
```python
    def send_message(self, chatID, text):
        data = {"to": chatID,
                "body": text}
        answer = self.send_requests('messages/chat', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .
- Text – Text of the message .


## time
Sends the current server time .
```python
    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%Y-%m-%d %H:%M:%S')
        return self.send_message(chatID, time)
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

## send_image
Send a image to phone number or group
```python
    def send_image(self, chatID):
        data = {"to": chatID,
                "image": "https://alvochat-example.s3-accelerate.amazonaws.com/image/1.jpeg"}
        answer = self.send_requests('messages/image', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

## send_video
Send a Video to phone number or group
```python
    def send_video(self, chatID):
        data = {"to": chatID,
                "video": "https://alvochat-example.s3-accelerate.amazonaws.com/video/1.mp4"}
        answer = self.send_requests('messages/video', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

## send_audio
Send a audio file to phone number or group
```python
    def send_audio(self, chatID):
        data = {"to": chatID,
                "audio": "https://alvochat-example.s3-accelerate.amazonaws.com/audio/1.mp3"}
        answer = self.send_requests('messages/audio', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .



## send_contact
Sending one contact or contact list to phone number 
```python
    def send_contact(self, chatID):
        data = {"to": chatID,
                'first_name':  'john',
                'last_name': 'doe',
                'phone': '16315555555',
                'company': 'Facebook',
                'email': 'info@facebook.com',
                'website': 'http://wwww.facebook.com'
                }
        answer = self.send_requests('messages/contact', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

## send_list
Sending whatsapp interactive list 
```python
    def send_list(self, chatID):
        data = {
            'to': chatID,
            'header': 'header',
            'body': ' please select one of the following options',
            'footer': 'footer',
            'button': 'options',
            'sections':
                [{"id": 1,    "title": "option_1",    "description": "option 1 description"},  {
                    "id": 2,    "title": "option_2",    "description": "option 2 description"}]
        }
        answer = self.send_requests('messages/list', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

## send_button
Sending whatsapp interactive buttons
```python
    def send_button(self, chatID):
        data = {
            "to": chatID,
            "header": "header",
            "body": " please select one of the following options",
            "footer": "footer",
            "buttons": [
                    {
                        "title": "option_1"
                    },
                        {
                        "title": "option_2"
                    },
                    {
                        "title": "option_3"
                    }
            ]

        }
        answer = self.send_requests('messages/button', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

## send_sticker
Sending whatsapp sticker
```python
        data = {"to": chatID,
                "sticker": "https://alvochat-example.s3-accelerate.amazonaws.com/sticker/2.webp"
                }
        answer = self.send_requests('messages/sticker', data)
        return answer
```
- ChatID – ID of the chat where the message should be sent for him, e.g 14155552671 .

# Incoming message processing
```python
        # print(self.event_type)
        # Handling incoming messages from the user and ignoring the ACK event_type
        if self.event_type != 'message_received':
            exit()
        else:
            if self.dict_messages != []:
                message = self.dict_messages
                text = message['body']
                chatID = message['from']
                if text != '':
                    if text.lower() == 'hi':
                        return self.welcome(chatID)
                    elif text.lower() == 'time':
                        return self.time(chatID)
                    elif text.lower() == 'image':
                        return self.send_image(chatID)
                    elif text.lower() == 'video':
                        return self.send_video(chatID)
                    elif text.lower() == 'audio':
                        return self.send_audio(chatID)
                    elif text.lower() == 'contact':
                        return self.send_contact(chatID)
                    elif text.lower() == 'document':
                        return self.send_document(chatID)
                    elif text.lower() == 'sticker':
                        return self.send_sticker(chatID)
                    elif text.lower() == 'location':
                        return self.send_location(chatID)
                    elif text.lower() == 'list':
                        return self.send_list(chatID)
                    elif text.lower() == 'button':
                        return self.send_button(chatID)
                    else:
                        return self.welcome(chatID, True)
            if  text=="":
                interactive_ = message['interactive']['type']
                print(interactive_)
                if interactive_ == 'list_reply'  :
                    s_option = message['interactive']['list_reply']['title']
                    return self.send_message(chatID, "Thank you 😊 ,  you choice : " + s_option)
                if interactive_ == 'button_reply' :
                    s_option = message['interactive']['button_reply']['title']
                    return self.send_message(chatID, "Thank you 😊 ,  you choice : " + s_option)
            else: return 'NoCommand'
```

# Flask 
To process incoming messages to our server 

```python
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


```

We will write the path app.route('/', methods = ['POST']) for it. This decorator means that our home function will be called every time our FLASK server .

