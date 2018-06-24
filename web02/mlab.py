import mongoengine

# mongodb://admin:hn18071997@ds263500.mlab.com:63500/muadongkhonglanh-c4e

host = "ds263500.mlab.com"
port = 63500
db_name = "muadongkhonglanh-c4e"
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