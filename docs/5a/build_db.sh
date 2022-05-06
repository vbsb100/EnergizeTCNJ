#!/bin/sh

python3 populate.py

dropdb -- if exists "energizeTCNJ"

createdb "energizeTCNJ"

psql -d "energizeTCNJ" -f "stageVa.sql"

psql -d "energizeTCNJ" -f "views.sql"
