from mongoengine import *
#1. desgin database

class Service(Document):
    name = StringField()
    gender = IntField() 
    phone = StringField()
    email = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()