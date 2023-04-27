import json

from channels.generic.websocket import AsyncWebsocketConsumer

from authentication.models import User, user_type
from questions.models import Quiz_settings


class LeaderboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "leaderboard",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "leaderboard",
            self.channel_name
        )

    # async def receive(self, text_data):
    #     data = json.loads(text_data)
    #     print(data)
    #     username = data['username']
    #     score = data['score']
    #     question = data['question']
    #     await self.channel_layer.group_send(
    #         'leaderboard',
    #         {
    #             'type': 'leaderboard.update',
    #             'username': username,
    #             'score': score,
    #             'question': question,
    #         }
    #     )
    #
    # async def leaderboard_update(self, event):
    #     username = event["username"]
    #     score = event['score']
    #     question = event['question']
    #     await self.send(text_data=json.dumps({
    #         'username': username,
    #         'score': score,
    #         'question': question,
    #     }))

    async def leaderboard_update(self, event):
        data = json.dumps(event['data'])

        await self.channel_layer.group_send(
            'leaderboard',
            {
                'type': 'websocket.send',
                'text': data,
            }
        )

    async def websocket_send(self, event):
        await self.send(text_data=event['text'])



