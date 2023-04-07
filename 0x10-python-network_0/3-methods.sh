#!/bin/bash
# Bash script that takes in a URL, sends a request to a URL
curl -sI "$1" | grep -oP "Allow\K.*"
