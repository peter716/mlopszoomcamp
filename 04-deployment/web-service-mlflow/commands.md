To launch environment which was created in week 2
`conda activate exp-tracking-env`
To start the mlflow server
`mlflow server \
    --backend-store-uri=sqlite:///mlflow.db \
    --default-artifact-root=s3://mlflows-artifacts-remote/`
To launch pipenv environment
`pipenv shell`
To install dependencies from the requirements.txt
`pipenv install -r requirements.txt`
To set environment variable
`export RUN_ID='run_id'`