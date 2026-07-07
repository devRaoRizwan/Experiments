# Learning RabbitMQ

so for learning Rabbit MQ we want to ensure couple of things:

1. Rabbit MQ follows **AMQP** (Advanced Message Queuing Protocol)
2. we need to understand couple of things before going inside it

## What is a Message Broker?

it is used as a **message broker**. what message broker is: it is a software that works like a **postman** — it collects post (message, or data packets) from the sender (**producer**) with address (**routing key**) to the post officer (**exchange**). the post officer reads the address and with the help of his computer he can quickly map it to the mail box (**queue**) that will hold the post. the post stays in the mail box until the receiving person (**consumer**) comes and picks it up.

so this is the basic understanding.

## Technical Terms

| Term | What it does |
|------|--------------|
| **producer** | that sends the data |
| **consumer** | that receives the data |
| **exchange** | the one who receives the message from the producer and routes it to the right queue based on the routing key |
| **queue** | the datastructure where the packets are stored until consumed |

## Deep Dive: producer.py

before this lets understand some technical terms too in concept of producer:

1. **what is connection?**
   so connection help us create a connection (TCP connection) with the running RabbitMQ server so that we can send packets of data
2. **what is channel?**
   channel is a lightweight virtual connection inside the TCP connection, it is the route we follow to send the packets of data to the exchange (one connection can have many channels)

now we will use a client dependency to make these things, so we will use **pika**.

### Steps

**step 1:** install pika

```bash
pip install pika
```

**step 2:** we will make a connection

```python
connection = pika.BlockingConnection(params)
```

**step 3:** we need to put in the parameters so we declare it too — we will provide some things like host, port, credentials to login. in this demo i am using rabbitmq running locally, this will be discussed later

```python
params = pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
```

**step 4:** we will create a channel for transfer of data

```python
channel = connection.channel()
```

**step 5:** we will create a queue (a storage) that will hold our messages until they are consumed
(note: the queue is declared from the channel, not from the connection)

```python
queue = channel.queue_declare(queue="demo_queue", durable=True)
```

**step 6:** prepare a message — in our case we are doing it hardcodedly because it is demo purpose

```python
message = {
    "status": 200,
    "message": "packet pushed successfully",
    "time": str(time.localtime())
}
```

**step 7:** now we will publish the message, our message will pass from local to the exchange.
it requires 3 things:

- **exchange** — there are many types but we will pass the empty string for now which means default
- **routing_key** — will be same as the queue name because the default exchange routes to the queue whose name matches the routing key
- **body** — it will contain the actual packet of data being sent as a string so we use `json.dumps()`

```python
channel.basic_publish(exchange="", routing_key="demo_queue", body=json.dumps(message))
```

**step 8:** we will close the connection

```python
connection.close()
```

## Deep Dive: consumer.py

now we will move into the consumer.py to see:

1. we will again make the connection and channel, also declare the same queue (with the same name and `durable=True`) so we can ensure we are using the same one
2. then we will create a callback function that will be used to process the fetched data
3. we will start the basic consume with `auto_ack=True` so the message is marked as acknowledged automatically once delivered
4. we will call `start_consuming()` which will loop and keep on listening the queue
