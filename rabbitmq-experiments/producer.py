import pika
import time
import json

# create a connection with the rabbit Mq running locally
credentials = pika.PlainCredentials("guest" , "guest")
params = pika.ConnectionParameters(host="localhost" , port= 5672 , credentials=credentials)
connection = pika.BlockingConnection(params)
# Create a channel to perform RabbitMQ operations (publish/consume messages).
channel = connection.channel()
# i didn't know we need to create a queue from a channel , i thought i had to make it from the connection
queue = channel.queue_declare(queue="demo_queue" , durable= True)
# for now i am creating a demo message to be sent
message = {
    "status" : 200,
    "message" : "packet pushed successfully",
    "time" : str(time.localtime())
}

print(message)

# to push the message we will call basic_publish on the channel
channel.basic_publish(exchange= "" , routing_key="demo_queue" , body= json.dumps(message))

connection.close()