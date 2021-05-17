#! /bin/sh
export $(cat .env | xargs)
docker-compose -f docker-compose.yml up -d --build