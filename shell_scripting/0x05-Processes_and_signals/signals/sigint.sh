#!/bin/bash

# Function to handle the SIGINT signal
function handle_sigint {
    echo "Caught SIGINT signal. Cleaning up and exiting..."
    # Add your cleanup code here
    exit 1
}

# Register the handle_sigint function to be called on SIGINT
trap 'handle_sigint' SIGINT

# Infinite loop to keep the script running
while true; do
    echo "Script is running..."
    sleep 1
done
