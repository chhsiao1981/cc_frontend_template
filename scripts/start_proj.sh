#!/bin/bash

npm install
ln -s ../config.js node_modules/config.js

if [ ! -f config/webpack.config.js ]
then
	mkdir -p config
	mv node_modules/react-scripts/config/webpack.config.js config
else
	rm node_modules/react-scripts/config/webpack.config.js
fi

cd node_modules/react-scripts/config
ln ../../../config/webpack.config.js ./
cd ../../../
npm start
