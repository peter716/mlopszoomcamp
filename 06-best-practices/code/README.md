To install pytest `pipenv install --dev pytest`

```bash
docker build -t stream-model-duration:v2 .
```

```bash
   docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="95182c88ec8040888af37b5f0259e733" \
    -e TEST_RUN="True" \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    stream-model-duration:v2
```

```bash
pipenv install --dev deepdiff
```

```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="Test123" \
    -e MODEL_LOCATION="/app/model" \
    -e TEST_RUN="True" \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="eu-north-1" \
    -v $(pwd)/model:/app/model \
    stream-model-duration:v2
```

To download files from S3 to local model directory 
```bash
aws s3 cp --recursive s3://mlflows-artifacts-remote/1/run_id/artifacts/model/ model
```
```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="Test123" \
    -e TEST_RUN="True" \
    -e AWS_DEFAULT_REGION="eu-north-1" \
    -v $(pwd)/model:/app/model \
    stream-model-duration:v2
```

To make run.sh executable
```bash
chmod +x integration-tests/run.sh
```

To check aws credentials
```bash
 nano ~/.aws/credentials
```

To check list of streams
```bash
aws kinesis list-streams
```
To check list of streams in localstack
```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis list-streams
```

To create stream in localstack
```bash
aws --endpoint-url=http://localhost:4566 \
    kinesis create-stream \
    --stream-name ride_predictions \
    --shard-count 1
```

To get shard iterator from kinesis
```bash
export PREDICTIONS_STREAM_NAME="ride_predictions"
export SHARD='shardId-000000000000'
aws  --endpoint-url=http://localhost:4566 \
    kinesis     get-shard-iterator \
    --shard-id ${SHARD} \
    --shard-iterator-type TRIM_HORIZON \
    --stream-name ${PREDICTIONS_STREAM_NAME} \
    --query 'ShardIterator'
```

To get records
```bash
aws  --endpoint-url=http://localhost:4566 \
    kinesis     get-records \
    --shard-iterator "AAAAAAAAAAHebXZfJF+ip5pICTTimTJrH3nDHrcq2uvIwSBoiSV6mbmJGs7l7eHF6YjuDWcd83eV93YnlwBGhdDkNwFGVa6qibalZBwWhh3pPJUwlk/njd1c3tHhpXnBCLhkCLxFN0u6pi9xEGDdgNL16iOeGml6YvhxInhhEhJwgSi2kAG7XTqMZoDcl/4RUCzDRWGGmCwCSwzzbCJQJEV60vuGKVeV" 
```

Get the data and run
```bash
echo data | base64 -d
```