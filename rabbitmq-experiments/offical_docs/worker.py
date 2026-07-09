import pika , sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host= "localhost"))
channel = connection.channel()
channel.queue_declare(queue="task_queue" , durable= True , arguments={'x-queue-type': 'quorum'})
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch , method , properties , body):
    print(f" [x] Received {body.decode()}")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue" , on_message_callback= callback , auto_ack= False)
channel.start_consuming()
    