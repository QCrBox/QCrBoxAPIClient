# Change to the working directory
cd $GITHUB_WORKSPACE/QCrBox

# Source test environment variables
set -a
source .env.test
set +a

# Wait for a response from the healthz API endpoint (max 30 attempts over 60 seconds)
for i in {1..30}; do
    # Check if the healthz endpoint is responsive
    if curl -s ${QCRBOX_BIND_ADDRESS}:${QCRBOX_REGISTRY_PORT}/api/healthz; then
        echo "QCrBox Registry is alive. Checking for registered applications..."
        # If healthy, query the applications endpoint and exit successfully
        curl -s ${QCRBOX_BIND_ADDRESS}:${QCRBOX_REGISTRY_PORT}/api/applications
        exit 0
    fi
done

# If the loop completes, the registry did not start up in time
echo "QCrBox Registry API is not available after 60 seconds." >&2
exit 1
