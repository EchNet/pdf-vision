#!/bin/sh
source ./.env
FILE=$1

echo "http://${S3_BUCKET}.s3.amazonaws.com/${S3_FOLDER}/${FILE}"
