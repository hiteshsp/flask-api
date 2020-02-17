import boto3
from time import time
client = boto3.client('dynamodb')

class DynamoDB():
    
    def dedup(obj):
        '''
        Returns the short url without generating it afresh.
        '''
        response = client.query(
            TableName=obj.table_name,
            ExpressionAttributeValues= {':url':{
                    'S':obj.long_url,
                    },
            },
            KeyConditionExpression='long_url = :url',
            ProjectionExpression='short_url'
            )
        return response['Items'][0]['short_url']['S']
    


# class Dynamodb(model):
    
#  def insert():
#     '''
#     This method inserts items into the table
#     '''
#     time = int(time.time())
#     item = client.put_item( TableName=model.name,
#         Item={
#             'long_url':{
#                'S': model.long_url
#             },
#             'timestamp':{
#                'N': time
#                 },
#             'short_url':{
#                 'S': model.short_url
#                 }
#             }
#         }