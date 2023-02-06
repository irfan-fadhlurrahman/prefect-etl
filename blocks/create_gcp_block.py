import os
import json

from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

# load .env variables to python
from dotenv import load_dotenv
load_dotenv()

CREDS_BLOCK = "gcp-creds"
BUCKET_BLOCK = "gcp-bucket"
BUCKET_NAME = "dtc_data_lake_dtc-de-course-375301"
SERVICE_ACC_PATH = f'{os.path.expanduser("~")}/{os.environ.get("GCP_CREDENTIALS")}'

# Open service account keys
with open(SERVICE_ACC_PATH, 'r') as f:
    gcp_service_acc = json.load(f)

# Create credentials block
credentials_block = GcpCredentials(
    service_account_info=gcp_service_acc
)
credentials_block.save(BUCKET_BLOCK, overwrite=True)

# Create gcs bucket block
bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load(BUCKET_BLOCK),
    bucket=BUCKET_NAME
)

bucket_block.save(BUCKET_BLOCK, overwrite=True)
