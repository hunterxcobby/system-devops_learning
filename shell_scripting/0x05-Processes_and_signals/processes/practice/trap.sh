#!/bin/bash

cleanup() {
  echo "Cleaning up..."
  # Additional cleanup commands
}

trap cleanup EXIT  # Execute cleanup function when the script exits

echo "Hello, World!"

# Rest of your script...


