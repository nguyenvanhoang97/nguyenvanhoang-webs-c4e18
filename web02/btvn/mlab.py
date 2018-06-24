import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds117061.mlab.com:17061/customer-c4e

host = "@ds117061.mlab.com"
port = 17061
db_name = "customer-c4e"
user_name = "admin"
password = "hn18071997"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())