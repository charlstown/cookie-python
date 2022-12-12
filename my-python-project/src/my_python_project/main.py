#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: My Python Project
# Author/s: Carlos Grande
# -----------------------------------------------------
# Date: 11/12/2022
# License: MIT
# Version: 0.1.0
# Maintainer/s: Carlos Grande
# Environment: my-python-project
# -----------------------------------------------------

# Libraries
import sys
import time
import argparse
import yaml
import logging

# Classes
from helpers import Helpers


class App:
    """
    Class description: Explain the main class.
    Name the public methods from this class:
    """

    def __init__(self, args: argparse.Namespace):
        """
        Constructor method to read the configuration parameters, generate the instances from modules and declare the
        global variables
        :param args: arguments from the command input flags
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
        self.example_class = Helpers(logger=logger, config=config)

    @staticmethod
    def _get_logger(level: str) -> logging.Logger:
        """
        Method to generate the logger used in the project
        :param level: the level of the logs to output
        :return: the custom logger
        """
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
        Main method to run the whole app and manage all calls.
        :return:
        """
        # Initializing the app
        start_app = time.time()
        self.log.info(f"\033[1m[Initializing {self.config['project_name']}]\033[0m")

        # >>> Start your src here <<<
        self.example_class.public_method()

        # Exiting the app
        end_app = time.time()
        elapsed_time = end_app - start_app
        str_elapsed_time = time.strftime('%H:%M:%S.', time.gmtime(elapsed_time))
        self.log.info(f"\033[1m[Exiting {self.config['project_name']} app."
                      f"Total elapsed time: {str_elapsed_time}]\033[0m")
        sys.exit(0)


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
