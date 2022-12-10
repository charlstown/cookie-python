# Set Up

## Project customization

During the template installation, you will be asked for some variables to customize your project. You can read more about about these parameters in the next table.

| Input parameter | Default value | Description |
| --- | --- | --- |
| project_name | `"My Python Project"` | The name of the project as String (you can add spaces and dashes). |
| project_description | `"Description in less than 20 words."` | Description of the project in less than 20 words if possible. |
| author | `"Carlos Grande"` | Name of the author of the project. |
| github_user | `"charlstown"` | The Github username of the author. |
| repository_name | `"{{ project_name }}"` | It's by default the name of the project in lowercase and dashed. |
| package_name | `"{{ project_name }}"` | It's by default the name of the project in lowercase and underscored. |
| repository_url | `"https://github.com/{{ github_user }}/{{ repository_name }}"` | The github url of the future repository. |
| maintainer | `"{{author}}"` | The maintainer of the project. |
| license | `["MIT", "Apache 2.0", "GNU General Public License", "Custom"]` | The name of the license |
| version | `"0.1.0"` | Version of the project to be created. |
| env_name | `"{{ repository_name }}"` | Name of the virtual environment path of the project. |
| python_version | `"3.10"` | Python version you ar working on. |


## Project contents

After the template installation you will have a directory with your customization and files ready to start coding.

The Project directory will have the next structure following the [packaging.python.org](https://packaging.python.org/en/latest/tutorials/packaging-projects/?highlight=src#a-simple-project) rules.

```
# Project initial contents
repository_name
├── src/package_name            <- Folder with the package code files
│   ├── __init__.py             <- Constructor file
│   ├── main.py                 <- File with the source code
│   └── helpers.py              <- Example class with helpers methods
├── data                        <- Data used for the project 
│   ├── config.yaml             <- Configuration file
│   └── logs                    <- Logs folder
│       └── file.log            <- Logs file from the project
├── docs                        <- Documentation folder
│   └── assets                  <- Folder for images and media
├── tests
│   ├── __init__.py
│   └── test_run.py   
├── Dockerfile
├── code_of_conduct.md
├── LICENSE
├── README.md
└── requirements.txt
```

