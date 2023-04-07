#!/bin/bash
# Bash script that takes in a URL, sends a request to a URL
curl -H "X-School-User-Id: 98" -sfL "$1"
