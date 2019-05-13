#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# By: Brian Salinas
#     https://github.com/Brian77077/Latest_Car
# Purpose: Python 3.x code testbed, NOT compatible with Python 2.x.
# Initial Release Date: May 12, 2019
# --------------------------------------------------------------------
#

# Simple file to convert the contents of the car_controller folder into a
# single, callable module.

# Algorithm: Functionality
# 	While __init__.py is not required in Python 3.3+, having this file in
#   the folder directory rolls-up all of the files in the directory into a
#   single callable method.  This functionality is described in detail at:
#   https://stackoverflow.com/questions/448271/what-is-init-py-for/29509611#29509611

# The status function will be phased out in the future, currently it just
# confirms that the module was rolled up into one correctly.
def status():
    return "The module car_controller call was successful"
