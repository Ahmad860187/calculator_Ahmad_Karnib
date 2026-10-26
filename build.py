#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")


name = "calculator_Ahmad_Karnib"
version = "0.1"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Ahmad_Karnib")
    # pyb looks for *_tests.py by default, our test file starts with test_
    project.set_property("unittest_module_glob", "test_*")
