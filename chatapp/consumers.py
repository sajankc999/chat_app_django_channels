from channels.generic.websocket import WebsocketConsumer
import json
class ChatwbsConsumer(WebsocketConsumer):
    groups=['XYTBA']
    def connect(self):
        print("connected to ")
        self.accept()
    def receive(self, text_data=None, bytes_data=None):
        print('message recieved :::',text_data)
        print("channel_layer",self.channel_layer)
        print('GroupNmae',self.groups)
        self.send(text_data= json.dumps({'msg':'this is server'}))

        return super().receive(text_data, bytes_data)
    def disconnect(self, code):
        return super().disconnect(code)