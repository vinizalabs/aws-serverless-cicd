import boto3
import botocore
import json
import os
import uuid
import logging
#import yaml

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('TABLE_NAME'))

def respond(response):

    print(response)

    return {
        'statusCode': '400' if 'Error' in response.keys() else '200',
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def get(id):
    try:
        response = table.get_item(
            Key={
                'id': id
                }
        )
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return e.response

    return response

def post(payload):
    try:
        response = table.put_item(
           Item=payload
        )
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return e.response

    return response

def delete(id):
    try:
        response = table.delete_item(
            Key={
                'id': id
            }
        )
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return e.response

    return response

def lambda_handler(event, context):

    operation = event['httpMethod']

    id = event['pathParameters']['id']

    if operation == 'POST':
        payload = json.loads(event['body'])
        payload['id'] = id
        return respond(post(payload))
    elif operation == 'GET':
        return respond(get(id))
    elif operation == 'DELETE':
        return respond(delete(id))
