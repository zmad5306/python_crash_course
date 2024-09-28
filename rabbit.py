import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5673))
channel = connection.channel()

more = True
client_delivery_tags = {}

while more:
    method, properties, body = channel.basic_get("client-id-queue")

    if (method and body):
        delivery_tag = method.delivery_tag
        client_id = int(body)

        if client_id in client_delivery_tags:
            client_delivery_tags[client_id].append(delivery_tag)
        else:
            client_delivery_tags[client_id] = [delivery_tag]
    else:
        more = False

for client_id, delivery_tags in client_delivery_tags.items():
    print(client_id)
    for delivery_tag in delivery_tags:
        channel.basic_ack(delivery_tag)
