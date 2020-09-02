#!/bin/bash

show_help() { 
	echo -e "Script is used for manually copying files to a remote server." 
	echo -e "Usage: $0 [-hv] -i ssh-key-path -s local-source-path -d user@server:/path/dest"
} 

# Initialize our own variables:
ssh_key=""
local_source=""
remote_dest=""

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -i|--identity) ssh_key="$2"; shift ;;
        -v|--verbose) verbose=1 ;;
		-s|--source) local_source="$2"; shift ;;
		-d|--destination) remote_dest="$2"; shift ;; 
        *) echo "Unknown parameter passed: $1"; show_help; exit 1 ;;
    esac
    shift
done

if [[ ( -z "$ssh_key" ) ||  ( -z "$local_source" ) || ( -z "$remote_dest" ) ]];
	then 
		show_help
		exit 1
fi 

scp -Cpr -i $ssh_key $local_source $remote_dest