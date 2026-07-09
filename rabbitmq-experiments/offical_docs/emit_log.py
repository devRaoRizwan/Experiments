import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="logs" , exchange_type='fanout')
message = "hello world from making the exchange"
channel.basic_publish(exchange="logs", routing_key="" , body=message)
print(f" [x] Sent {message}")
connection.close()