from channels.generic.websocket import AsyncWebsocketConsumer
import json

class WbChannels(AsyncWebsocketConsumer):
    async def connect(self):
        self.token = self.scope["url_route"]["kwargs"]["token"]
        self.chat_group_name = self.token
        # 收到连接时候处理，
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 关闭channel时候处理
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    # 收到消息
    async def receive(self, text_data=None, bytes_data=None):
        data = text_data or bytes_data
        print('write: {!r}'.format(data))
        if data:
            if isinstance(data, str):
                data = json.loads(data)
            message = data['message']
            type = data["type"]
            print("收到消息--》",message)
            # 发送消息到组
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'client.message',
                    'message': message
                }
            )

    # 处理客户端发来的消息
    async def send_to_wb(self, event):
        message = event['message']
        print("发送消息。。。",message)
        # 发送消息到 WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

