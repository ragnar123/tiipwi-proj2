#!/bin/bash

PORT=8000

python manage.py runserver $PORT >> logs &
ngrok http $PORT | grep "http"

