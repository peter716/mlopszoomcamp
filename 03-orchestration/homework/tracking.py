import mlflow
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(output):
# def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here

    lr,dv = output
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment('homework3')
    # print(mlflow.search_experiments())

    print(lr)
    with mlflow.start_run():
        
        # Log the model
        mlflow.sklearn.log_model(lr, "model")

        # Save the DictVectorizer to a file
        with open("dict_vectorizer.pkl", "wb") as f:
            pickle.dump(dv, f)
        
        # Log the DictVectorizer as an artifact
        mlflow.log_artifact("dict_vectorizer.pkl")

        print("logged successfully")



