{{cookiecutter.project_name}}
==========

This is based on https://github.com/chhsiao1981/cc_frontend_template.git

Install
----------

    git clone [repo] .; ./scripts/clone_proj.sh

Development
----------

* create module: ./scripts/dev_module.sh [module_name]
* create container: ./scripts/dev_container.sh [container_name_page]
* create subcontainer: ./scripts/dev_subcontainer.sh [subcontainer_name]
* create component: ./scripts/dev_component.sh [component_name]

* remember to add reducers to src/reducers/index.js
* remember to add container-page to src/Routes.js
