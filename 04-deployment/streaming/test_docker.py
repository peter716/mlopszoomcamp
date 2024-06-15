
# import lambda_function
import requests 

event = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49653014984944601435417437616308869565118956805763891202",
                "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDE1NgogICAgfQ==",
                "approximateArrivalTimestamp": 1718437394.276
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49653014984944601435417437616308869565118956805763891202",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::511900348839:role/lambda-kinesis-role",
            "awsRegion": "eu-north-1",
            "eventSourceARN": "arn:aws:kinesis:eu-north-1:511900348839:stream/ride_events"
        }
    ]
}


# result = lambda_function.lambda_handler(event, None)
# print(result)

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
response = requests.post(url, json=event)
print(response.json())