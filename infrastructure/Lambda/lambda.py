import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')
def lambda_handler(event, context):
    # TODO implement
    response = table.get_item(Key={
        'id':'1'
    })
    Views = response['Item']['Views']
    Views = Views + 1
    print(Views)
    response = table.put_item(Item={
        'id':'1',
        'Views': Views
    })
    return Views