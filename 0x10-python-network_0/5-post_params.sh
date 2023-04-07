#!/bin/bash
# Bash script that takes in a URL, sends a request to a URL
curl -d "email=test@gmail.com&subject=I will always be here for PLD"-sL -X POST "$1"
