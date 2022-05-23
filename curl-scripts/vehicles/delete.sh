#!/bin/bash

curl "http://localhost:8000/vehicles/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
