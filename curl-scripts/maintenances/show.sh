#!/bin/bash
VEHICLE_ID="17"
ID="3"
TOKEN="592ef76a39095673982c6b9edc98ff175bb0201c"

curl "http://localhost:8000/vehicles/${VEHICLE_ID}/maintenances/${ID}/" \
  --include \
  --request GET \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \

echo
