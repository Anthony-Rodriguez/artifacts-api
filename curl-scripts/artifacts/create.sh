#!/bin/bash

curl "http://localhost:8000/artifacts" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "artifact": {
      "name": "'"${NAME}"'",
      "category": "'"${CATEGORY}"'",
      "rarity": "'"${RARITY}"'",
      "attunement": "'"${ATTUNEMENT}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
