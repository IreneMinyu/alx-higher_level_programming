#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX GET -H "X-Hello School!-User-Id: 98" "$1"