from mongoengine import *
#1. desgin database
class River(Document):
    name = StringField()
    continent = StringField()
    lenght = IntField()