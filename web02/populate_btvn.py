from models.service import Service
import mlab

mlab.connect()

new_service = Service(
    name = "FangQing",
    yob = 2000,
    gender = 0,
    height = 160,
    phone = "1234",
    address = "Hà Nội",
    status = False,
    description = "đáng yêu",
    image = "static/image/Fang.jpg" ,
    measurements = [69,69,69],
)
new_service.save()