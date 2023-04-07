#!/bin/bash
# Bash script that takes in a URL, sends a request to a URL
curl -sI -H "X-School-User-Id: 98" "$1"
