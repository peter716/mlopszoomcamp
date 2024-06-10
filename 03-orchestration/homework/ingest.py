import requests
from io import BytesIO
from typing import List

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    dfs: List[pd.DataFrame] = []

    # for year, months in [(2024, (1, 3))]:
    #     for i in range(*months):
    # year = 2023
    # i = 3
    # response = requests.get(
    #     'https://github.com/mage-ai/datasets/raw/master/taxi/yellow'
    #     f'/{year}/{i:02d}.parquet'
    # )

    response = requests.get('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet')

    if response.status_code != 200:
        raise Exception(response.text)

    df = pd.read_parquet(BytesIO(response.content))
    dfs.append(df)

    return pd.concat(dfs)