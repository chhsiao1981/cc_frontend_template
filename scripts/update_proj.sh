#!/bin/bash

if [ $# -ne 1 ]
then
	echo "usage: update_proj.sh [version]"
	exit 255
fi
version=$1

echo "version: ${version}"

npm install --save --save-exact react-scripts@${version}
./scripts/start_proj.sh
