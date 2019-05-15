#!/bin/bash

project=`basename \`pwd\``

python cc/gen.py project "${project}"

cp config.js.tmpl config.js

./scripts/start_proj.sh
