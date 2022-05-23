#!/bin/bash

curl "http://localhost:8000/vehicles/" \
  --include \
  --request POST \
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
