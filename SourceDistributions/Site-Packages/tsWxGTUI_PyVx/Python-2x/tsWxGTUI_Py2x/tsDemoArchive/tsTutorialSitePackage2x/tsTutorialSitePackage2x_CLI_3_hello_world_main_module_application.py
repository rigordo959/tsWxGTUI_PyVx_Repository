#!/usr/bin/env python
# "Time-stamp: <04/12/2014  2:53:03 PM rsg>"
#################################################################
#
# File: Tutorial_CLI_3_hello_world_main_module_application.py
#
# Purpose:
#
#     Demonstrates Python language syntax for defining the
#     "main" application and a "utility" function within source
#     code for Python 2.7.0-2.7.6 and Python 3.0.0-3.4.0.
#
# Usage (example):
#
#    # Execute
#
#    python Tutorial_CLI_3_hello_world_main_module_application.py
#
#################################################################

def utility_method(text):
    print(text)
 
if __name__ == '__main__':
 
    utility_method("Hello World via Python Application")
