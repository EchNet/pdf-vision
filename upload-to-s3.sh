#!/bin/sh
source ./.env
FILE=$1

set -e

aws s3 cp sample1.png s3://${S3_BUCKET}/${S3_FOLDER}/${FILE}
