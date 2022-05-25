#!/bin/bash
VEHICLE_ID='17'
ID="3"
TOKEN="592ef76a39095673982c6b9edc98ff175bb0201c"
TYPE="OIL CHANGE"
DATE="2006-10-25 12:00:00"
COST="25.00"
NOTES="oil change at oreilly's in dayton"

curl "http://localhost:8000/vehicles/${VEHICLE_ID}/maintenances/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "maintenance": {
      "type": "'"${TYPE}"'",
      "date": "'"${DATE}"'",
      "cost": "'"${COST}"'",
      "notes": "'"${NOTES}"'"
    }
  }'

echo
