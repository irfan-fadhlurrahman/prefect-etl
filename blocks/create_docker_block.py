from prefect.infrastructure.docker import DockerContainer

BLOCK_NAME = "de-docker"
DOCKER_USERNAME = "irfanfadh43"
DOCKER_IMAGE_TAG = "prefect:web_to_gcs"

# Create Docker Block
docker_block = DockerContainer(
    image=f"{DOCKER_USERNAME}/{DOCKER_IMAGE_TAG}",
    image_pull_policy="ALWAYS",
    auto_remove=True
)

docker_block.save(BLOCK_NAME, overwrite=True)