import boto3
import csv
import json

sqs = boto3.resource('sqs')
client = boto3.client('sqs')

def send_messages_to_sqs(name, message):
    queue = 'url fila'
    client.send_message(QueueUrl=queue, MessageBody=message)

def make_json():
    with open('avengers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            send_messages_to_sqs('avengers-queu', json.dumps(row))

make_json()
