#!/bin/bash

echo "started at $(date +"%T.%N")"

set -e

OPTS=`getopt -o p: --long profile: -n 'parse-options' -- "$@"`

if [ $? != 0 ] ; then echo "Failed parsing options." >&2 ; exit 1 ; fi

echo "$OPTS"
eval set -- "$OPTS"

PROFILE=''

while true; do
  case "$1" in
    -p | --profile ) PROFILE="$2"; shift; shift ;;
    -- ) shift; break ;;
    * ) break ;;
  esac
done

echo "Start deploying stack"
sam deploy  --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_NAMED_IAM \
    --stack-name open-IELTS-syan --s3-bucket open-IELTS-syan-bucket-us-east-1 \
    --no-confirm-changeset --s3-prefix open-IELTS-syan/Artifacts/Templates \
    --parameter-overrides Project=open-IELTS-syan  Owner=weihengyans@gmail.com Name=open-IELTS-syan \
    BasePath=open-IELTS-syan --guided
  

echo "finished at $(date +"%T.%N")"
echo "All done"
