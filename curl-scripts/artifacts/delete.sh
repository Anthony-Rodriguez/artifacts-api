#!/bin/bash

curl "http://localhost:8000/artifacts/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
