#! /bin/bash

sudo docker exec -it basedjango_db_1 psql -d database1 -U database1_role
