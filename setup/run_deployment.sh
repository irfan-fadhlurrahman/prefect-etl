# Export .env variables to shell session
source ./.env

# Activate virtual environment
cd ~/${PROJECT_FOLDER}
pipenv shell

# Run the deployed container
# prefect deployment run etl-parent-flow/docker-flow -p "month_list=[1]" -p "year=2020" -p "color=green"
prefect deployment run etl-parent-flow/docker-flow -p "month_list=[2, 3]" -p "year=2019" -p "color=yellow"

prefect agent start -q 'default'
