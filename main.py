import os
import json
from time import sleep
import datetime
import faker
from azure.storage.blob import BlobServiceClient, ContentSettings
from dotenv import load_dotenv

load_dotenv()
fake = faker.Faker()


# env variables
container_name = os.environ['CONTAINER_NAME']
connection_string = os.environ['BLOB_CONNECTION_STRING']


# create a fake order
def create_order():
    orders =  {
        "order_id": fake.ean(length=8),
        'customer_id': fake.uuid4(),
        'item_name': fake.random_element(elements=('apple', 'banana', 'orange', 'grape', 'watermelon', 'pineapple')),
        'order_amount': fake.random_int(min=1, max=1000),
        'item_price': fake.random_int(min=1, max=1000),
        'payment_provider': fake.random_element(elements=('paypal', 'klarna', 'cc'))
        }

    return orders


# save json to file
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


# create timestamp
def create_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S%f")
    return timestamp


# upload json to azure blob storage container named 'orders'
def upload_blob(file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=file_name)

    content_settings = ContentSettings(content_type='application/json')

    with open(file_name, "rb") as data:
        blob_client.upload_blob(data, content_settings=content_settings)

    os.remove(file_name)


if __name__ == '__main__':
    counter = 0
    while counter < 1:
        file = create_timestamp() + '.json'
        save_json(create_order(), file)
        upload_blob(file)
        sleep(1)
        counter += 1

