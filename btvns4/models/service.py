from mongoengine import *
#1. desgin database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    image = StringField()
    measurements = ListField()

class Order(Document):
    id_nguoidung = StringField()
    id_doitac = StringField()
    thoigian = DateTimeField()
    is_accepted = BooleanField()

class User(Document):
    username = StringField()
    password = StringField()
    email = StringField()
    fullname = StringField()