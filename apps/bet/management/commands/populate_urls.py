from apiclient.discovery import build
from oauth2client.tools import argparser
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.bet.models import Song


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = settings.GOOGLE_API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def populate_urls():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    for song in Song.objects.all():
        if song.youtube_link:
            break
        q = song.name + " " + song.artist.name

        search_response = youtube.search().list(
            part="id,snippet",
            q=q,
        ).execute()

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                url = "https://www.youtube.com/watch?v={}".format(search_result["id"]["videoId"])
                song.youtube_link = url
                song.save()
                break


class Command(BaseCommand):
    populate_urls()

    def handle(self, *args, **options):
        pass
