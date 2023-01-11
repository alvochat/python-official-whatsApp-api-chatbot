import json
import requests
import datetime


class alvochatChatBot():
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.event_type = json['event_type']
        self.alvochatAPIUrl = 'https://api.alvochat.com/{{instanceId}}/'
        self.token = '{{token}}'

    def send_requests(self, type, data):
        url = f"{self.alvochatAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"to": chatID,
                "body": text}
        answer = self.send_requests('messages/chat', data)
        return answer

    def send_image(self, chatID):
        data = {"to": chatID,
                "image": "https://alvochat-example.s3-accelerate.amazonaws.com/image/1.jpeg"}
        answer = self.send_requests('messages/image', data)
        return answer

    def send_video(self, chatID):
        data = {"to": chatID,
                "video": "https://alvochat-example.s3-accelerate.amazonaws.com/video/1.mp4"}
        answer = self.send_requests('messages/video', data)
        return answer

    def send_audio(self, chatID):
        data = {"to": chatID,
                "audio": "https://alvochat-example.s3-accelerate.amazonaws.com/audio/1.mp3"}
        answer = self.send_requests('messages/audio', data)
        return answer

    def send_document(self, chatID):
        data = {"to": chatID,
                "document": "https://alvochat-example.s3-accelerate.amazonaws.com/document/1.pdf",
                "filename": "example_file.pdf",
                "caption": "caption "
                }
        answer = self.send_requests('messages/document', data)
        return answer

    def send_sticker(self, chatID):
        data = {"to": chatID,
                "sticker": "https://alvochat-example.s3-accelerate.amazonaws.com/sticker/2.webp"
                }
        answer = self.send_requests('messages/sticker', data)
        return answer

    def send_location(self, chatID):
        data = {
            "to": chatID,
            "lat": "37.484296",
            "lng": "-122.148703",
            "address": "Menlo Park, California, United States",
            "name": "Meta Headquarters"
        }
        answer = self.send_requests('messages/location', data)
        return answer

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

    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%Y-%m-%d %H:%M:%S')
        return self.send_message(chatID, time)

    def welcome(self, chatID, noWelcome=False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = "Hi , welcome to WhatsApp chatbot using Python\n"
        else:
            welcome_string = """wrong command
Please type one of these commands:
*hi* : Saluting - text message
*time* : show server time
*image* : I will send you a picture
*video* : I will send you a Video
*audio* : I will send you a audio file
*contact* : I will send you a contact
*document* : I will send you a document
*sticker* : I will send you a sticker
*location* : I will send you a location
*list* : I will send you a list
*button* : I will send you a buttons
"""
        return self.send_message(chatID, welcome_string)

    def Processingـincomingـmessages(self):
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