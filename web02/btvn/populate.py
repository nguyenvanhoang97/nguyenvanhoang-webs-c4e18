from models.cus import Service
import mlab
from faker import Faker
from random import randint , choice

mlab.connect()

fake = Faker()

for i in range(50):
    print("saving service" , i + 1)
    new_service = Service(
        name= fake.name(),
        gender= randint(0, 1),
        phone= fake.phone_number(),
        email= fake.email(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True, False])
    )

    new_service.save()