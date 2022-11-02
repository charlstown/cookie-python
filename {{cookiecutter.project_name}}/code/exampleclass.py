#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Configuration file for the project {{cookiecutter.project_name}}
# Author/s: {{cookiecutter.author}}
# -----------------------------------------------------
# Date: {% now 'local', '%d/%m/%Y' %}
# License: {{cookiecutter.license}}
# Version: {{cookiecutter.version}}
# Maintainer: {{cookiecutter.maintainer}}
# Contact: {{cookiecutter.contact}}
# -----------------------------------------------------

# Libraries
import logging


class ExampleClass:
    """
    Explain here the usage of this class.
    """
    def __init__(self, logger: logging.Logger, config: dict):
        """
        Constructor method to create an instance from the class with initial arguments and global variables.
        :param logger: logger defined in the main file.
        :param config: configuration parameters
        """
        # Global variables
        self.logger = logger
        self.config = config
        self.example_global_variable = "Hello World"

    def _private_method(self):
        """
        Explain here the usage of this method.
        :return: None
        """
        self.logger.info(f'This "{self._private_method.__name__}" is a method from {ExampleClass.__name__}.')

    def public_method(self):
        """
        Explain here the usage of this method.
        :return: None
        """
        self.logger.info(f'This "{self.public_method.__name__}" is a method from {ExampleClass.__name__}.')
        self._private_method()
        self.logger.info(f'This "{self.example_global_variable}" is a global variable.')
