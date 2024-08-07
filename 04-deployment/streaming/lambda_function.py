import json
import os
import json
import boto3
import base64

import mlflow

import tracemalloc
tracemalloc.start()


kinesis_client = boto3.client('kinesis')

PREDICTIONS_STREAM_NAME = os.getenv('PREDICTIONS_STREAM_NAME', 'ride_predictions')

RUN_ID = os.getenv('RUN_ID')
# RUN_ID = '95182c88ec8040888af37b5f0259e733'

TEST_RUN = os.getenv('TEST_RUN', 'False') == 'True'

# logged_model = f's3://mlflows-artifacts-remote/1/{RUN_ID}/artifacts/model'

logged_model = f's3://mlflows-artifacts-remote/1/{RUN_ID}/artifacts/model'
# logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features
    
def predict(features):
    pred = model.predict(features)
    return float(pred[0])
    # return 10

def lambda_handler(event, context):
    # TODO implement
    # ride = event['ride']
    # ride_id = event['ride_id']
    
    predictions_events = []
    predictions = []
    
    for record in event['Records']:
        encoded_data = record['kinesis']['data']
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        # print(decoded_data)
        
        ride_event = json.loads(decoded_data)

        print(ride_event)
        ride = ride_event['ride']
        ride_id = ride_event['ride_id']
    
        features = prepare_features(ride)
        prediction = predict(features)
        predictions.append({
            'ride_duration': prediction,
            'ride_id': ride_id} )
        
        prediction_event = {
            'model': 'ride_duration_prediction_model',
            'version': '123',
            'prediction': {
                'ride_duration': prediction,
                'ride_id': ride_id   
            }
        }
        
        # kinesis_client.put_record(
        #     StreamName=PREDICTIONS_STREAM_NAME,
        #     Data=json.dumps(prediction_event),
        #     PartitionKey=str(ride_id)
        #     )
        if not TEST_RUN:
            kinesis_client.put_record(
                StreamName=PREDICTIONS_STREAM_NAME,
                Data=json.dumps(prediction_event),
                PartitionKey=str(ride_id)
            )
            
        predictions_events.append(prediction_event)
    # print(json.dumps(event))
    # prediction = 10
    # ride_id = 123
    
    # features = prepare_features(ride)
    # prediction = predict(features)
    return {
        'predictions': predictions_events
    }
