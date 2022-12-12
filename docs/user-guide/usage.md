# Usage

Once the template is applied, the base code directory will have the next structure following the [packaging.python.org](https://packaging.python.org/en/latest/tutorials/packaging-projects/?highlight=src#a-simple-project) rules.

``` title="Base code generated from the template" hl_lines="4 5 6 8 9 10"
my-python-project               <- Custom template project directory
├── src                         <- Folder with the source files and packages.
│   └── my_python_project       <- Folder with the package code files.
│       ├── __init__.py         <- Constructor file.
│       ├── main.py             <- File with the source code.
│       └── helpers.py          <- Example class with helpers methods.
├── data                        <- Data used for the project.
│   ├── config.yaml             <- Configuration file.
│   └── logs                    <- Logs folder.
│       └── file.log            <- Logs file from the project.
├ requirements.txt              <- Requirements file.
...
```

## Running the base code

Before starting to develop your own code you can run the base code by following the next steps.

- **Step 1: Create your virtual environment(optional)**

    This step is optional but recommended, create your virtual environment for this project by the name you typed when generating the custom template. By default is **my-python-project (env_name)**.

- **Step 2: Install the requirements**

    Install the requirements to run the project in the virtual environment by the following command. The only library preconfigured in the requirements is PyYAML, required to read the configuration file.

    ``` bash
    pip install -r requirements.txt
    ```

- **Step 3: run the main.py file**

    Let's start by running the main.py file in debug mode.

    ``` bash
    cd my-python-project
    python src/my_python_project/main.py -l debug 
    ```

    After running the command you should see an output showing the initial arguments and the execution of the public and private methods from the Helpers class.

    ``` title="output"
    2022-12-11 23:49:13 [DEBUG] main.py - __init__ (L50): 
    2022-12-11 23:49:13 [DEBUG] main.py - __init__ (L51): Initial args: 
    2022-12-11 23:49:13 [DEBUG] main.py - __init__ (L53): >> config: data/config.yaml
    2022-12-11 23:49:13 [DEBUG] main.py - __init__ (L53): >> log: ['debug']
    2022-12-11 23:49:13 [DEBUG] main.py - __init__ (L53): >> test: False
    2022-12-11 23:49:13 [DEBUG] main.py - __init__ (L54): 

    2022-12-11 23:49:13 [INFO] main.py - run (L101): [Initializing my-python-project]
    2022-12-11 23:49:13 [INFO] helpers.py - public_method (L40): This "public_method" is a method from Helpers.
    2022-12-11 23:49:13 [INFO] helpers.py - _private_method (L33): This "_private_method" is a method from Helpers.
    2022-12-11 23:49:13 [INFO] helpers.py - public_method (L42): This "Hello World" is a global variable.
    2022-12-11 23:49:13 [INFO] main.py - run (L110): [Exiting my-python-project app.Total elapsed time: 00:00:00.]
    ```


## Understanding the base code

To get a better understanding of the base code from the template, lets review some important files from the project generated.


### 1. The main.py file

**It is the class acting as an orchestrator of the whole code.**

The main.py file is made of one class called **App** and, the following three methods.

| Methods | Description |
| --- | --- |
| `\__init__` | Constructor method to read the configuration parameters, generate the instances from modules and declare the global variables. |
| `_get_logger` | Method to generate the logger used in the project. |
| `run` | Main method to run the whole app and manage all calls. |


#### 1.1 The \__init__ method

The *\__init__* method is in charge to declare the configuration values, define the global variables and, generate the instances from other modules like the helpers class.

``` python
def __init__(self, args: argparse.Namespace):
    """
    Constructor method to read the configuration parameters, generate the instances from modules and declare the global variables
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
    self.helpers = Helpers(logger=logger, config=config)
```


#### 1.2 The run method

The run method acts as the runner of the whole script **here is where everything related with the app happens**. The run method is set to start developing your code in the lines 94 and 95.

``` python linenums="94" hl_lines="10 11"
def run(self):
    """
    Main method to run the whole app and manage all calls.
    :return: None
    """
    # Initializing the app
    start_app = time.time()
    self.log.info(f"\033[1m[Initializing {self.config['project_name']}]\033[0m")

    # >>> Start your code here <<<
    self.helpers.public_method()

    # Exiting the app
    end_app = time.time()
    elapsed_time = end_app - start_app
    str_elapsed_time = time.strftime('%H:%M:%S.', time.gmtime(elapsed_time))
    self.log.info(f"\033[1m[Exiting {self.config['project_name']} app."
                    f"Total elapsed time: {str_elapsed_time}]\033[0m")
    sys.exit(0)
```


### 2. The helpers.py file

Helpers.py file


### 3. The configuration file

The config file.


### 4. The logs file

The logs file

</br>