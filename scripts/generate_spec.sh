set -eu

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
TMP_DIR=$SCRIPT_DIR/../tmp
GOTHAM_MAVEN_REPO_PATH="$GOTHAM_MAVEN_DIST_RELEASE/$(echo "$GOTHAM_MAVEN_CONJURE_GROUP_ID" | sed 's/\./\//g')/${GOTHAM_MAVEN_CONJURE_ARTIFACT_ID}"

echo $GOTHAM_MAVEN_REPO_PATH
mkdir -p $TMP_DIR
GOTHAM_API_GATEWAY_VERSION=$( wget -q -O - "${GOTHAM_MAVEN_REPO_PATH}/maven-metadata.xml" | \
    python scripts/parse_version.py )

echo Downloading $GOTHAM_API_GATEWAY_VERSION...
mkdir -p "${TMP_DIR}"
wget -P "${TMP_DIR}"  "${GOTHAM_MAVEN_REPO_PATH}/${GOTHAM_API_GATEWAY_VERSION}/${GOTHAM_MAVEN_CONJURE_ARTIFACT_ID}-${GOTHAM_API_GATEWAY_VERSION}.sls.tgz" &> /dev/null

tar -xf "${TMP_DIR}/${GOTHAM_MAVEN_CONJURE_ARTIFACT_ID}-${GOTHAM_API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=3 "${GOTHAM_MAVEN_CONJURE_ARTIFACT_ID}-${GOTHAM_API_GATEWAY_VERSION}/asset/ir-v2/openapi-ir.json"
tar -xf "${TMP_DIR}/${GOTHAM_MAVEN_CONJURE_ARTIFACT_ID}-${GOTHAM_API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=2 "${GOTHAM_MAVEN_CONJURE_ARTIFACT_ID}-${GOTHAM_API_GATEWAY_VERSION}/deployment/manifest.yml"

echo Done!
