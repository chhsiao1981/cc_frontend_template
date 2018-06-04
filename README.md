cc_frontend_template
==========
This is the frontend development template based on cookie-cutter and create-react-app.

    create-react-app .; git clone https://github.com/chhsiao1981/cc_frontend_template.git cc; ./cc/scripts/init_dev.sh; . __/bin/activate; ./cc/scripts/init_proj.sh; cp config.js.tmpl config.js; npm install; ln -s ../config.js node_modules/config.js; mkdir -p config; mv node_modules/react-scripts/config/webpack.config.dev.js config; cd node_modules/react-scripts/config; ln ../../../config/webpack.config.dev.js ./; cd ../../../; mv node_modules/react-scripts/config/webpack.config.prod.js config; cd node_modules/react-scripts/config; ln ../../../config/webpack.config.prod.js ./; cd ../../../; npm start

* create module: ./scripts/dev_module.sh
* create container: ./scripts/dev_container.sh
* create subcontainer: ./scripts/dev_subcontainer.sh
* create component: ./scripts/dev_component.sh

Updating:

    npm install--save --save-exact react-scripts@1.1.4
    cd node_modules/react-scripts/config; rm webpack.config.dev.js; ln ../../../config/webpack.config.dev.js ./; rm webpack.config.prod.js; ln ../../../config/webpack.config.prod.js ./; cd ../../../;

Introduction
-----
This template intends to efficiently develop with the following libraries:

* cookiecutter

All are welcometo improve this template.
