import pika , sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello" , durable= True , arguments= {'x-queue-type': 'quorum'})
message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange="" , routing_key="hello" , body=message)
print(" [x] Sent 'Hello World!'")
connection.close()