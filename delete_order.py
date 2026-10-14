import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('orders')
stepfunctions = boto3.client('stepfunctions')
STATE_MACHINE_ARN = 'arn:aws:states:us-east-1:339713037456:stateMachine:order-delete-process'

def lambda_handler(event, context):
    try:
        path = event.get('pathParameters') or {}
        order_id = path.get('order_id')
        if not order_id:
            return response(400, 'Missing order_id parameter')

        result = table.query(
            KeyConditionExpression=Key('order_id').eq(order_id)
        )
        items = result.get('Items', [])
        if not items:
            return response(404, 'Order not found')

        item = items[0]

        table.delete_item(
            Key={
                'order_id': item['order_id'],
                'creation_date': item['creation_date']
            }
        )

        stepfunctions.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            input=json.dumps({
                'message': json.dumps(item, default=str),
                's3Key': f"deleted-orders/{order_id}.txt"
            })
        )

        return response(200, 'Order deleted successfully and archiving process started.')

    except Exception as e:
        return response(500, f'Internal error: {str(e)}')

def response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(body, default=str)
    }