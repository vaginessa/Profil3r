#!/bin/bash

# This script is used to run unit tests during the development of profil3r
# usage : ./scripts/tests.sh

echo "[+] Testing the different services"
poetry run pytest tests/test_services.py