#!/usr/bin/env python

import json
import sys
import logging

from cookiecutter.main import cookiecutter


def underscore_to_uppercase(the_str):
    return the_str.upper()


def underscore_to_camelcase(the_str):
    the_list = the_str.split('_')
    return ''.join([each_str.title() for each_str in the_list])


the_module = sys.argv[1]
full_name = sys.argv[2]

logging.warning('full_name: %s', full_name)

full_name_list = full_name.split('.')
if len(full_name_list) == 1:
    pkg = full_name_list[0]
    module = full_name_list[0]

    pkg_name = pkg
    include_pkg = 'cm' + pkg

    package_dir = '.'
    include_package_dir = "."
    test_package_dir = '.'
else:
    pkg = full_name_list[-1]
    module = full_name_list[-1]

    pkg_name = pkg
    include_pkg = 'cm' + pkg

    package_dir = '/'.join(full_name_list[:-1])
    include_package_dir = '/'.join(['cm' + each_pkg for each_pkg in full_name_list[:-1]])
    test_package_dir = '/'.join(['test_' + each_pkg for each_pkg in full_name_list[:-1]])


the_dict = {
    'pkg': pkg,
    'module': module,

    'pkg_name': pkg,

    'include_pkg': include_pkg,

    'package_dir': package_dir,
    'include_package_dir': include_package_dir,
    'test_package_dir': test_package_dir,

    'PKG': underscore_to_uppercase(pkg),
    'MODULE': underscore_to_uppercase(module),
    'PKG_NAME': underscore_to_uppercase(pkg_name),
    'INCLUDE_PKG': underscore_to_uppercase(include_pkg),
    'PACKAGE_DIR': underscore_to_uppercase(package_dir),
    'INCLUDE_PACKAGE_DIR': underscore_to_uppercase(include_package_dir),
    'TEST_PACKAGE_DIR': underscore_to_uppercase(test_package_dir),

    'Pkg': underscore_to_camelcase(pkg),
    'Module': underscore_to_camelcase(module),
    'PkgName': underscore_to_camelcase(pkg_name),
    'IncludePkg': underscore_to_camelcase(include_pkg),
    'PackageDir': underscore_to_camelcase(package_dir),
    'IncludePackageDir': underscore_to_camelcase(include_package_dir),
    'TestPackageDir': underscore_to_camelcase(test_package_dir),
}

cookiecutter(
    'cc/' + the_module,
    extra_context=the_dict,
    no_input=True,
    overwrite_if_exists=True,
    skip_if_file_exists=True,
)
