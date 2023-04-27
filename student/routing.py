from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/leaderboard/(?P<gamepin>\w+)/$', consumers.LeaderboardConsumer.as_asgi()),
]
