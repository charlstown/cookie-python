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
from exampleclass import ExampleClass


class App:
    """
    Class description: Explain the main class.
    Name the public methods from this class:
    """

    def __init__(self, args: argparse.Namespace):
        """
        Class constructor: Here you should read the config file, generate
        the instances from modules and declare global variables.
        :param logger:
        :param dir_config: Explain the dir_config parameter.
        """
        # Argument variables
        dir_config = args.config
        test = args.test
        arg_level = args.log[0]

        # Reading the config json file
        yaml_file = open(dir_config, 'r')
        config = yaml.safe_load(yaml_file)

        # Getting logger
        logger = self._get_logger(level=arg_level)

        # Logging argument variables
        logger.debug('')
        logger.debug("Initial args: ")
        for k, v in vars(args).items():
            logger.debug(f">> {k}: {v}")
        logger.debug("\n")

        # Global variables
        self.config = config
        self.log = logger

        # Global instances
        self.example_class = ExampleClass(logger=logger, config=config)

    def _get_logger(self, level: str):
        # Setting up the output level
        levels = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING}
        set_level = levels[level]

        # Setting up the logger
        set_log_format = '%(asctime)s [%(levelname)s] %(filename)s - %(funcName)s (L%(lineno)s): %(message)s'
        set_date_format = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(level=set_level,
                            format=set_log_format,
                            datefmt=set_date_format)
        my_logger = logging.getLogger(__name__)

        # Create a file log handler
        file_handler = logging.FileHandler('data/logs/file.log')
        file_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter(set_log_format)
        file_handler.setFormatter(f_format)

        # Add handlers to the logger
        my_logger.addHandler(file_handler)
        return my_logger

    def run(self):
        """
        This method runs the whole app and manage all calls.
        :return:
        """
        # Initializing the app
        self.log.info(f"--- Initializing {self.config['project_name']} ---")

        # Run example module method
        self.example_class.public_method()


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c",
                        default="data/config.yaml",
                        help="Add the config file path after this flag")
    parser.add_argument('--log', "-l",
                        choices=['debug', 'info', 'warning'],
                        default=["info"],
                        nargs="+")
    parser.add_argument("--test", "-t",
                        default=False,
                        action='store_true',
                        help="This argument is a switcher, by default is false")
    my_args = parser.parse_args()

    # App execution
    my_app = App(args=my_args)
    my_app.run()
