import pika

params = pika.ConnectionParameters(host= "localhost" , port= 5672 , credentials= pika.PlainCredentials("guest" , "guest"))
connection = pika.BlockingConnection(params)
channel = connection.channel()
queue = channel.queue_declare(queue="demo_queue", durable=True)

def consumer_callback(channel , method , properties , body):
    print("received message" , body)


channel.basic_consume(queue="demo_queue" , on_message_callback=consumer_callback , auto_ack= True)
print("waiting for messages , press CTRL+C to exit")
channel.start_consuming()
