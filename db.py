import boto3
from time import time
client = boto3.client('dynamodb')

class DynamoDB():
    def dedup():
        client.query()