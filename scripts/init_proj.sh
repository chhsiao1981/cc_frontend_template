#!/bin/bash

project=`basename \`pwd\``

python cc/gen.py project "${project}"

cp config.js.tmpl config.js
npm install
ln -s ../config.js node_modules/config.js
mkdir -p config
mv node_modules/react-scripts/config/webpack.config.js config
cd node_modules/react-scripts/config
ln ../../../config/webpack.config.js ./
cd ../../../
npm start
