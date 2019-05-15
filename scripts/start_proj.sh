#!/bin/bash

npm install
ln -s ../config.js node_modules/config.js
rm node_modules/react-scripts/config/webpack.config.js
cd node_modules/react-scripts/config
ln ../../../config/webpack.config.js ./
cd ../../../
npm start
