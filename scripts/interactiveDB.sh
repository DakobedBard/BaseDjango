#! /bin/bash

sudo docker-compose exec -it djangoapp psql -d database1 -U database1_role
psql -d database1 -U database1_role