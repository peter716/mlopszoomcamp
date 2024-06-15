`KINESIS_STREAM_INPUT=ride_events
aws kinesis put-record \
    --stream-name ${KINESIS_STREAM_INPUT} \
    --partition-key 1 \
    --data "Hello, this is a test." \
    --cli-binary-format raw-in-base64-out`


`aws kinesis put-record \
    --stream-name ${KINESIS_STREAM_INPUT} \
    --partition-key 1 \
    --data '{
        "ride": {
            "PULocationID": 130,
            "DOLocationID": 205,
            "trip_distance": 3.66
        }, 
        "ride_id": 156
    }'\
     --cli-binary-format raw-in-base64-out`


     `KINESIS_STREAM_OUTPUT='ride_predictions'
SHARD='shardId-000000000000'

SHARD_ITERATOR=$(aws kinesis \
    get-shard-iterator \
        --shard-id ${SHARD} \
        --shard-iterator-type TRIM_HORIZON \
        --stream-name ${KINESIS_STREAM_OUTPUT} \
        --query 'ShardIterator' \
)`

`RESULT=$(aws kinesis get-records --shard-iterator $SHARD_ITERATOR)`

`echo ${RESULT} | jq -r '.Records[0].Data' | base64 --decode`

```bash
export PREDICTIONS_STREAM_NAME="ride_predictions"
export RUN_ID="95182c88ec8040888af37b5f0259e733"
export TEST_RUN="True"

python test.py
```

`docker build -t stream-model-duration:v1 .



```bash
docker run -it --rm \
    -p 8080:8080 \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e RUN_ID="95182c88ec8040888af37b5f0259e733" \
    -e TEST_RUN="True" \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    stream-model-duration:v1
```

To create elastic container registry for docker container
`aws ecr create-repository --repository-name duration-model`

Logging in
`$(aws ecr get-login --no-include-email)`

Pushing
```bash
REMOTE_URI="387546586013.dkr.ecr.eu-west-1.amazonaws.com/duration-model"
REMOTE_TAG="v1"
REMOTE_IMAGE=${REMOTE_URI}:${REMOTE_TAG}

LOCAL_IMAGE="stream-model-duration:v1"
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE}
docker push ${REMOTE_IMAGE}
```
# Remove all stopped containers
docker container prune -f

# Remove all unused images
docker image prune -a -f

# Remove all unused networks
docker network prune -f

# Remove all unused volumes
docker volume prune -f

# Remove all dangling images (intermediate images that are not used by any containers)
docker image prune -f

docker system prune -a
docker volume prune

