# 1. GitHub to GCS
# Deployment
prefect deployment build ./src/github_to_gcs/github_to_gcs.py:etl_parent_flow -n "GitHub to GCS ETL Pipeline" \
--params '{"color": "green", "year": 2019, "month_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}' \
-q 'github_to_gcs' 

# Run the deployment
prefect deployment apply etl_parent_flow-deployment.yaml
prefect deployment run "etl-parent-flow/GitHub to GCS ETL Pipeline"

# Start the agent
prefect agent start -q 'github_to_gcs'

# 2. GCS to BQ
# Deployment
prefect deployment build ./src/gcs_to_bq/gcs_to_bq.py:etl_parent_flow_bq -n "GCS to BQ ETL Pipeline" \
--params '{"color": "green", "year": 2019, "month_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}' \
-q 'gcs_to_bq' 

# Run the deployment
prefect deployment apply etl_parent_flow_bq-deployment.yaml
prefect deployment run "etl-parent-flow-bq/GCS to BQ ETL Pipeline"

# Start the agent
prefect agent start -q 'gcs_to_bq'