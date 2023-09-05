#!/usr/bin/env bash
# A Bash script that transfers a file from our client to a server

if [ "$#" -lt 3 ]; then
       echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"   
elif [ "$#" -lt 4 ]; then
        scp -o StrictHostKeyChecking=no "$1" "$3@$2":~/
else
        scp -i "$4" -o StrictHostKeyChecking=no "$1" "$3@$2":~/
fi
