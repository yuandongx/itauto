from channels.generic.websocket import AsyncWebsocketConsumer
from task.tasks import ansible_run
import json
from core.ansible.runtask import RunTasks
from core.connection import runserver, to_text
from core.log import log


class WbChannels(AsyncWebsocketConsumer):
    async def connect(self):
        self.token = self.scope["url_route"]["kwargs"]["token"]
        self.chat_group_name = self.token
        # connect time out
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # close connection and to do something.
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    # receive message
    async def receive(self, text_data=None, bytes_data=None):
        data = text_data or bytes_data
        print('write: {!r}'.format(data))
        if data:
            if isinstance(data, str):
                data = json.loads(data)
            message = data['message']
            type = data["type"]
            print("received - >",message)
            # send received message to group
            await self.channel_layer.group_send(
                self.chat_group_name,
                data
            )


    # deal with message and send to client(this is websocket)
    async def ansible_web(self, event):
        print(event)
        message = event['message']
        print("send message -->",message)
        #send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    # to do tasks (this is websocket)
    async def ansible_cli(self, event):
        if event.get("token"):
            ansible_run(event["token"])

