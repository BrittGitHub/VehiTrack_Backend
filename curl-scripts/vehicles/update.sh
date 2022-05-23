#!/bin/bash

curl "http://localhost:8000/vehicles/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "vehicle": {
      "v_year": "'"${YEAR}"'",
      "v_make": "'"${MAKE}"'",
      "v_model": "'"${MODEL}"'"
    }
  }'

echo
