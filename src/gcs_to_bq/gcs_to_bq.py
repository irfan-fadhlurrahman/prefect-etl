import urllib
import pandas as pd

from pathlib import Path

from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

@task(retries=2)
def extract(color: str, year: int, month: int) -> Path:
    """Download data from Cloud Storage"""
    gcs_path = Path(f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet")
    gcs_block = GcsBucket.load("gcp-bucket")
    
    gcs_block.get_directory(
        from_path=gcs_path, 
        local_path="./"
    )
    
    return gcs_path

@task(log_prints=True)
def transform(path: Path) -> pd.DataFrame:
    """Data cleaning example"""
    df = pd.read_parquet(path)
    # print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
    # df["passenger_count"].fillna(0, inplace=True)
    # print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    return df


@task()
def load(df: pd.DataFrame, color: str) -> None:
    """Write DataFrame to BigQuery"""
    gcp_credentials_block = GcpCredentials.load("gcp-bucket")
    df.to_gbq(
        destination_table=f"trips_data_all.{color}-taxi",
        project_id="dtc-de-course-375301",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists='append'
    )

@flow(log_prints=True)
def etl_gcs_to_bq(color: str, year: int, month: int) -> None:
    """Main ETL flow to load data into BigQuery"""
    # Task starts here
    path = extract(color, year, month)
    df = transform(path)
    
    print(f"Size: {df.shape}")
    print(df.info())
    
    # Task to write to BQ
    load(df, color)
    
@flow()
def etl_parent_flow_bq(color: str, year: int, month_list: list) -> None:
    """Run each etl_gcs_to_bq flow for specific dataset"""
    for month in month_list:
        try:
            etl_gcs_to_bq(color, year, month)
        except (urllib.error.HTTPError, FileNotFoundError):
            continue
        
if __name__ == "__main__":
    color = "yellow"
    year = 2019
    month_list = [2, 3]
    etl_parent_flow_bq(color, year, month_list)