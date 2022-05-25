#!/bin/bash
ID="17"
TOKEN="f3feb05678b69156ba24a9ff4ef6713efdc9a9e8"
TYPE="REPAIR"
DATE="2006-10-25 14:35:00"
COST="100.00"
NOTES="repair in dayton"

curl "http://localhost:8000/vehicles/${ID}/maintenances/" \
  --include \
  --request POST \
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
