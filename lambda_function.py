import boto3
import json
from datetime import datetime


def lambda_handler(event, context):
    sns = boto3.client('sns')

    health_status = {
        'timestamp': datetime.now().isoformat(),
        'service': 'Business Health Monitor',
        'status': 'ALERT',
        'message': 'Monitoring system active - threshold exceeded',
        'metric': 'Error Rate',
        'value': '6 errors/min',
        'threshold': '5 errors/min'
    }

    topic_arn = 'arn:aws:sns:us-east-1:YOUR_ACCOUNT_ID:Business-monitoring-alerts'

    sns.publish(
        TopicArn=topic_arn,
        Subject='⚠️ Business Alert: Threshold Exceeded',
        Message=json.dumps(health_status, indent=2)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Monitor executed successfully')
    }
