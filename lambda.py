import json
import boto3
import uuid

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('gateway_table')  # Ensure the table name is correct

def lambda_handler(event, context):
    try:
        # Debugging: Print the event structure
        print("Received event:", json.dumps(event))

        # Check if the event contains 'body'
        if 'body' not in event:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing body in request"})
            }

        # Parse JSON body
        body = json.loads(event['body'])

        # Ensure required fields are present
        if 'name' not in body or 'email' not in body:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields: name, email"})
            }

        # Create item for DynamoDB
        item = {
            "id": str(uuid.uuid4()),  # Unique ID
            "name": body['name'],
            "email": body['email']
        }

        # Store in DynamoDB
        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Data stored successfully!", "data": item})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
