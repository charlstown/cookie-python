#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Configuration file for the project {{ project_name }}
# Author/s: {{ author }}
# -----------------------------------------------------
# Date: {{ date }}
# License: {{ license }}
# Version: {{ version }}
# Maintainer: {{ maintainer }}
# email: {{ email }}
# -----------------------------------------------------

# Libraries
import argparse
import yaml
import logging


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

        # Variables
        self.config = config
        self.log = logger

        # Instance

    def run(self):
        """
        This method runs the whole app and manage all calls.
        :return:
        """
        self.log.info("Initializing the app")
        # Run first module method
        self.log.info(self.config)

        # Run second module method


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", default="data/config.yaml",
                        help="Add the config file path after this flag")
    parser.add_argument("--test", "-t", default=False, action='store_true',
                        help="This argument is a switcher, by default is false")
    args = parser.parse_args()

    # Argument variables
    arg_config = args.config
    arg_test = args.test
    logging.basicConfig(level=logging.INFO)
    my_logger = logging.getLogger('APP')
    print("Initial args:")
    print(f"- Config: {arg_config}")
    print(f"- Test: {arg_test}", '\n')

    # App execution
    my_app = App(logger=my_logger, dir_config=arg_config)
    my_app.run()
