import json
import numpy

def lambda_handler(event, context):
    body_data = event['body']
    dict_body_data = json.loads(body_data)

    left = dict_body_data["left_value"]
    right = dict_body_data["right_value"]
    summation = left * 2 + right * 3
    return {
        'statusCode': 200,
        'body': json.dumps({"left":left, "right":right, "result": summation}),
    }
