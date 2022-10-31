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


class Test:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config

    def example_method(self):
        self.logger.info('This is a test')
        self.logger.info(self.config)