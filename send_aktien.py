import requests, json
import pika

url = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
text = url.text
#print(text)
print ("Star rabbit mq")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='aktien')
channel.basic_publish(exchange='',
                      routing_key='aktien',
                      body=text)
print(" [x] Sent 'Hello World!'")
connection.close()
