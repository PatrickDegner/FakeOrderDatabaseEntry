# FakeOrderDatabaseEntry
A Simple Tool to create a json file with fake order data which is uploaded to azure storage

## How it works

This Tool creates a json file with following fake informations:
- order_id
- customer_id
- item_name
- order_amount
- item_price
- payment_provider

After creation of this file it will be uploaded to azure storage.

For event streaming purpose it got a while loop at the end to create 1 file each second.


</br>

# How to use
Clone or download the repository
```sh
https://github.com/PatrickDegner/FakeOrderDatabaseEntry.git
```

Create a .env file and insert your container_name aswell as the storage connection string
```sh
CONTAINER_NAME = "orders"
BLOB_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=XXXXXX;AccountKey=XXXXXXX;EndpointSuffix=core.windows.net"

```
Run the script
```sh
python main.py
```

![image](https://user-images.githubusercontent.com/108484798/205396285-d3613de8-442c-4d56-b237-308a9844a3fc.png)
