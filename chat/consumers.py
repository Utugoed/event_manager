import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get('user', None)
        if not self.user or not self.user.is_authenticated:
            await self.close()
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope["user"].email

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': sender,
                'message': message
            }
        )
    
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        await self.send(
            text_data=json.dumps(
                {
                    'event': 'Send',
                    'sender': sender,
                    'message': message
                }
            )
        )
