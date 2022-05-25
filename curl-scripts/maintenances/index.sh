#!/bin/bash
ID="17"
TOKEN="592ef76a39095673982c6b9edc98ff175bb0201c"

curl "http://localhost:8000/vehicles/${ID}/maintenances/" \
  --include \
  --request GET \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \

echo
