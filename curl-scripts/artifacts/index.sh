#!/bin/bash

curl "http://localhost:8000/artifacts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
