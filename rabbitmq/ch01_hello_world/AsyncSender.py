import pika


def on_open(conn):
    conn.channel(on_open_callback=on_channel_open)


def on_channel_open(channel):
    channel.basic_publish(
        exchange='',
        routing_key='default_queue',
        body='message body value',
        properties=pika.BasicProperties(
            content_type='text/plain',
            delivery_mode=1
        )
    )


parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
connection = pika.SelectConnection(
    parameters=parameters,
    on_open_callback=on_open
)
print(connection)
try:
    # ch = connection.channel()
    # ch.queue_declare('default_queue')
    connection.ioloop.start()
except KeyboardInterrupt:
    connection.close()
