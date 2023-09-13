import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author = self.scope['user'].username

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'author': author
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        author = event["author"]
        message_with_username = f"{author}: {message}"

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message_with_username}))
