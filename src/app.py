import datetime
import os
import boto3

from flask import Flask, jsonify, request


ENV = os.environ['ENV']
SQS_QUEUE_URL = os.environ['SQS_QUEUE_URL']

application = Flask(__name__)
sqs = boto3.client('sqs')


@application.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'up', 'datetime': datetime.datetime.now(),
                    'environment': ENV}), 200


@application.route('/message', methods=['GET'])
def get_message():
    response = sqs.receive_message(
        QueueUrl=SQS_QUEUE_URL,
        AttributeNames=['All'],
        MaxNumberOfMessages=1
    )

    received_message = response['Messages'][0]
    message_id = received_message['MessageId']
    message_body = received_message['Body']
    receipt_handle = received_message['ReceiptHandle']

    sqs.delete_message(QueueUrl=SQS_QUEUE_URL,
                       ReceiptHandle=receipt_handle)

    return jsonify({'message_id': message_id, 'message': message_body}), 200


@application.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    new_message = data['message']

    response = sqs.send_message(QueueUrl=SQS_QUEUE_URL,
                                DelaySeconds=10,
                                MessageBody=('%s' % new_message))

    return jsonify({'message_id': response['MessageId']}), 201


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
