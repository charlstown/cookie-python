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
import argparse
import yaml
import logging

# Classes
from test import Test


class App:
    """
    Class description: Explain the main class.
    Name the public methods from this class:
    """

    def __init__(self, logger: logging, dir_config: str):
        """
        Class constructor: Here you should read the config file, generate
        the instances from modules and declare global variables.
        :param logger:
        :param dir_config: Explain the dir_config parameter.
        """
        # Reading the config json file
        yaml_file = open(dir_config, 'r')
        config = yaml.safe_load(yaml_file)

        # Global variables
        self.config = config
        self.log = logger

        # Global instances
        self.test = Test(logger=logger, config=config)

    def run(self):
        """
        This method runs the whole app and manage all calls.
        :return:
        """
        # Initializing the app
        self.log.info("--- Initializing the app ---")

        # Run example module method
        self.test.example_method()


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c",
                        default="data/config.yaml",
                        help="Add the config file path after this flag")
    parser.add_argument("--test", "-t",
                        default=False,
                        action='store_true',
                        help="This argument is a switcher, by default is false")
    args = parser.parse_args()

    # Argument variables
    arg_config = args.config
    arg_test = args.test

    # Setting up the logger and output level
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(filename)s (L%(lineno)s) - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',)
    my_logger = logging.getLogger(__name__)

    # Create file handler
    file_handler = logging.FileHandler('data/logs/file.log')
    file_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s.%(msecs)00d [%(levelname)s] %(filename)s (L%(lineno)s) - %(funcName)s: %(message)s')
    file_handler.setFormatter(f_format)

    # Add handlers to the logger
    my_logger.addHandler(file_handler)

    my_logger.info("Initial args:")

    # Logging argument variables
    for k, v in vars(args).items():
        my_logger.info(f"- {k}: {v}")
    my_logger.info("\n")

    # App execution
    my_app = App(logger=my_logger, dir_config=arg_config)
    my_app.run()
