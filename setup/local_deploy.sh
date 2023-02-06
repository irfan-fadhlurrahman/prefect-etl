# Deployment Green Taxi November 2020
prefect deployment build ./flows/parameterized_flow.py:etl_parent_flow -n "GitHub to GCS ETL Pipeline Apr 2019" \
--params '{"color": "green", "year": 2019, "month_list": [4]}'

# Run the deployment
prefect deployment run "etl-parent-flow/GitHub to GCS ETL Pipeline"

# Start the agent
prefect agent start -q 'default'
