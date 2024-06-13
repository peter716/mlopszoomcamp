import pickle
import mlflow
import os

from mlflow.tracking import MlflowClient


from flask import Flask, request, jsonify


# MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
# mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

RUN_ID = os.getenv('RUN_ID')
# RUN_ID = '95182c88ec8040888af37b5f0259e733'


# logged_model = f's3://mlflows-artifacts-remote/1/{RUN_ID}/artifacts/model'

logged_model = f's3://mlflows-artifacts-remote/1/{RUN_ID}/artifacts/model'
# logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)

#To get environment dependencies
# dependencies = mlflow.pyfunc.get_model_dependencies(logged_model)
# print(dependencies)

# client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

# path = client.download_artifacts(run_id=RUN_ID, path='dict_vectorizer.bin')
# print(f"downloading the dict vectorizer to {path}")
# with open(path, 'rb') as f_out:
#     dv = pickle.load(f_out)

# with open('lin_reg.bin', 'rb') as f_in:
#     (dv, model) = pickle.load(f_in)


def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features):
    # X = dv.transform(features)
    # preds = model.predict(X)
    preds = model.predict(features)
    return float(preds[0])


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred,
        'model_version' : RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)