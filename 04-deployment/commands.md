To configure pip environment with packages
`pipenv install scikit-learn==1.2.2 flask --python=3.11`

To launch shell
`pipenv shell`

To copy model
`cp /home/ubuntu/mlopszoomcamp/01-intro/models/lin_reg.bin .`

To install gunicorn for deployment in production server
`pipenv install gunicorn`

To deploy app in production server
`gunicorn --bind=0.0.0.0:9696 predict:app`

To install requests for development
`pipenv install --dev requests`

To build docker image
`docker build -t ride-duration-prediction-service:v1 .`

To run docker container
`docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1`
