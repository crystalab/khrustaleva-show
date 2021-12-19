#!/bin/bash

gunicorn khrustaleva_show.wsgi:application \
  --name khrustaleva_show \
  --bind '127.0.0.1:8000' \
  --workers 3

