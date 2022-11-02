# Table of Contents
1. [What is PyTemplate](#1-what-is-pytemplate)
2. [Installation](#2-installation)
3. [Usage](#3-usage)
4. [Troubleshooting](#4-troubleshooting)
5. [Disclaimer](#5-disclaimer)
6. [Help wanted](#6-help-wanted)
7. [Other links](#7-other-links)

</br>

# 1. What is PyTemplate

A Python archetype to help me and others begin developing a coding project. The archetype follows a customizable project structure using cookiecutter as a template generator.

## 1.1 What is cookiecutter
A command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

Visit these links to learn more about cookiecutter.
Documentation: https://cookiecutter.readthedocs.io/
GitHub: https://github.com/cookiecutter/cookiecutter


# 2. Installation

## 2.1 Cookiecutter installation

Installing cookiecutter package on Ubuntu is very easy, visit the link to the cookiecutter documentation to learn how to install it.
[Install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter)


## 2.2 PyTemplate installation
To generate a custom project from the template, follow these steps:
- 1. Navigate to the path where you desire to generate the project folder.
- 2. Run the cookiecutter command followed by the repository URL.
  ```
  cookiecutter https://github.com/charlstown/py-template.git
  ```
- 3. Fill out the form in the console and the project will be generated at the end.


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


# 4. Troubleshooting

Errors, future updates, or beta configurations. Explain why and how it could break.


# 5. Disclaimer

Explain the dos and don'ts of your app, what you take responsibility for, and where is the limit of its purpose.


# 6. Help Wanted

Some extra help or clarification about the whole process. What you don't provide.


# 7. Other links

References, contact, or related repositories go here.

