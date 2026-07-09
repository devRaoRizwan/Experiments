import pika 
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="task_queue" , durable= True , arguments={'x-queue-type': 'quorum'})

message = "Hello world"
channel.basic_publish(
        exchange="" , 
        routing_key="task_queue" , 
        body= message , 
        properties= pika.BasicProperties(delivery_mode= pika.DeliveryMode.Persistent)
    )
print("following message packet is sent : " , message)

channel.close()
