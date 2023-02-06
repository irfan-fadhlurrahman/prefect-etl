# Build an Docker Image
docker build -t irfanfadh43/prefect:web_to_gcs .

# Push to docker hub
docker image push irfanfadh43/prefect:web_to_gcs

# Export .env variables to shell session
source ./.env

# Activate virtual environment
cd ~/${PROJECT_FOLDER}
pipenv shell

# Run
python flows/web_to_gcs_deploy.py
