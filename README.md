# PyTemplate

[![python](https://img.shields.io/pypi/pyversions/cookiecutter.svg)](https://pypi.org/project/cookiecutter/)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

:cookie: A cookiecutter template for general projects in python (DevOps & Data Science).
</br>

![Logo](docs/assets/logo.png)

# Table of Contents
1. [What is PyTemplate](#1-what-is-pytemplate)
2. [Installation](#2-installation)
3. [Usage](#3-usage)
4. [Troubleshooting](#4-troubleshooting)
5. [Disclaimer](#5-disclaimer)
6. [Help wanted](#6-help-wanted)
7. [Other links](#7-other-links)

  

# 1. What is PyTemplate

A Cookiecutter template for general python developers. Reommended for DevOps & Data Science projects. The template follows a customizable project structure using cookiecutter as the template generator.

## 1.1 What is cookiecutter
A command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

Visit these links to learn more about cookiecutter.
Documentation: https://cookiecutter.readthedocs.io/
GitHub: https://github.com/cookiecutter/cookiecutter

## 1.2 Repository contents

```
PyTemplate                              -> Project directory.
├── cookiecutter.json                   -> Cookiecutter values.
├── {{cookiecutter.repository_name}}    -> Coockiecutter template.
│   └── ...
├── mkdocs.yml                          -> mkdocs configuration file.
├── docs                                -> Project documentation.
│   └── ...
├── README.md                           -> README file.
├── code_of_conduct.md                  -> Code of conduct file.
├── contributing.md                     -> Contributing file.
├── LICENSE                             -> LICENSE file.
└── requirements.txt                    -> Requirements to run the project.
```

</br>

# 2. Installation

To create the project from the template you need to install cookiecutter and follow these instructions.

## 2.1 Cookiecutter installation

Installing cookiecutter package on Ubuntu is very easy, you can simply run the next command to install it.
```
pip install cookiecutter
```

Visit the link to the cookiecutter documentation to learn more about the installation:  
[Install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter)


## 2.2 PyTemplate installation
To generate a custom project from the template, follow these steps:
- 1. Navigate to the path where you desire to generate the project folder.
- 2. Run the cookiecutter command followed by the repository URL.
  ```
  python -m cookiecutter https://github.com/charlstown/py-template.git
  ```
- 3. Fill out the form in the console and the project will be generated at the end.

</br>

# 3. Usage

## 3.1 Test run
After generating your first project, you can do a test run.

(optional) Execute in the console this command to see the possible arguments.
```
python code/main.py -h
```

Run the code by the next command.
```
python code/main.py
```

The output should be something like this:
```
2022-11-02 19:51:36 [INFO] main.py - run (L101): [Initializing MyAwesomeProject]
2022-11-02 19:51:36 [INFO] exampleclass.py - public_method (L41): This "public_method" is a method from ExampleClass.
2022-11-02 19:51:36 [INFO] exampleclass.py - _private_method (L34): This "_private_method" is a method from ExampleClass.
2022-11-02 19:51:36 [INFO] exampleclass.py - public_method (L43): This "Hello World" is a global variable.
2022-11-02 19:51:36 [INFO] main.py - run (L110): [Exiting MyAwesomeProject app.Total elapsed time: 00:00:00.]
```

## 3.2 Starting to code your project

We recommend starting coding your project with these tips:

You can start creating your custom classes using the class "exampleclass.py" as the template.
```
class ExampleClass:
"""
Example class as a template for other classes. Explain the use of this class here.
"""
```

You can instance your custom classes in the "main.py" file the same way we instanced ExampleClass.
```
# Global instances
self.example_class = ExampleClass(logger=logger, config=config)
```


You can start orchestrating your methods from the "run" method from the App class in the "main.py" file.
```
# >>> Start your code here <<<
self.example_class.public_method()
```

</br>

# 4. Troubleshooting

The main branch has been tested and before any push, we make sure everything is working fine.
Feel fre to open a new issue if you see the archetype is no working correctly or any additional requirement is needed.

</br>

# 5. Disclaimer

This is an archetype template done in Python using the library cookiecutter. This template is intended to help coding in python.

Do not use this template for any commercial nor redistribution purpose. Actually, the use of such tool might be allowed for open-source or private projects.

</br>

# 6. Help Wanted

This repository does provide the required installation instructions to install it by your own.
Feel free to contact me on https://carlosgrande.me/contact-me-carlos-grande/

</br>

# 7. Other links

This project is based on the Python project structure from this post:
- [My-pythons-project-cheatsheet](https://carlosgrande.me/my-pythons-project-cheatsheet/)
- [Repo here](https://github.com/charlstown/Python-Project-Structure)

Interested links:
- [carlosgrande.me](https://carlosgrande.me/)
- [Cookiecutter documentation]( https://cookiecutter.readthedocs.io/)
- [Coockiecutter official repository](https://github.com/cookiecutter/cookiecutter)
