TAG=$(echo "${BRANCH_NAME}" | sed -e "s/\//_/g")
echo "Running for ${TAG}"
docker build -t tenbagger:${TAG} .
