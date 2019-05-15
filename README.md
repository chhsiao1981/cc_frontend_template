cc_frontend_template
==========
This is the frontend development template based on cookie-cutter and create-react-app.

    npx create-react-app .; git clone https://github.com/chhsiao1981/cc_frontend_template.git cc; ./cc/scripts/init_dev.sh; . __/bin/activate; ./cc/scripts/init_proj.sh

* create module: ./scripts/dev_module.sh
* create container: ./scripts/dev_container.sh
* create subcontainer: ./scripts/dev_subcontainer.sh
* create component: ./scripts/dev_component.sh

Updating:

    npm install--save --save-exact react-scripts@3.0.1
    cd node_modules/react-scripts/config; rm webpack.config.js; ln ../../../config/webpack.config.js ./; cd ../../../;

Introduction
-----
This template intends to efficiently develop with the following libraries:

* cookiecutter

All are welcome to improve this template.
