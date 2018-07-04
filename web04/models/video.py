from mongoengine import *

class Video(Document):
    title = StringField()
    thumblbail = StringField()
    link = StringField()
    views = IntField()
    youtube_id = StringField()
