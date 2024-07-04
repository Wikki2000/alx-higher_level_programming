#!/usr/bin/env bash
# sends a request to that URL, and displays the size of the body of the response.

# Check if URL is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <url>"
else
	# Send request to URL and display size of the body in bytes
		response_size=$(curl -s "$1" | wc -c)
	echo "$response_size"
fi
