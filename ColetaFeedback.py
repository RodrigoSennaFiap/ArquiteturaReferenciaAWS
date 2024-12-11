import boto3
import os
import json
import uuid
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # Registrar Feedback
        body = json.loads(event['body'])
        feedback_id = str(uuid.uuid4())
        feedback = {
            "feedback_id": feedback_id,
            "user": body.get('user', 'Anonymous'),
            "message": body.get('message', '')
        }
        try:
            table.put_item(Item=feedback)
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Feedback registrado com sucesso!", "id": feedback_id})
            }
        except ClientError as e:
            return {"statusCode": 500, "body": str(e)}
    elif event['httpMethod'] == 'GET':
        # Listar Feedbacks
        try:
            response = table.scan()
            feedbacks = response.get('Items', [])
            return {
                "statusCode": 200,
                "body": json.dumps(feedbacks)
            }
        except ClientError as e:
            return {"statusCode": 500, "body": str(e)}
