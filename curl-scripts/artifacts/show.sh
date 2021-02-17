#!/bin/bash

curl "http://localhost:8000/artifacts/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
