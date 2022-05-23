#!/bin/bash

curl "http://localhost:8000/vehicles/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
