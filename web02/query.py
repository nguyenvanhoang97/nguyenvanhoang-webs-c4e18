from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# print(first_service.name)#.to_mongo())

id_to_find = "5b2ba3ed25dff81ef80c8d62"
service = Service.objects.with_id(id_to_find)

if service is not None:
    print(service.yob)
    service.update(set__yob = 2000)
    service.reload()
    print(service.yob)
    # fQ.delete()
else:
    print("not found")