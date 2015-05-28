#!/bin/sh
# counts the number of records in archive
# useful to check if some records are missing during editing

openssl enc -d -aes-256-cbc -in archive.protected | grep '^---' | wc -l
