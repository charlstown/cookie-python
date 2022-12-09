# **PyTemplate Documentation**

A Python archetype to help developers begin developing a coding project. The archetype follows a customizable project structure using cookiecutter as a template generator.

[:simple-github: Visit the repository](https://github.com/charlstown/py-template.git){ .md-button }

</br>

![Project logo](assets/logo.png)


## Quick start

**Step 1 :** Install the cookiecutter package, you can simply run the next command to install it.

``` bash
pip install cookiecutter
```

**Step 2:** Run the cookiecutter command followed by the template repository URL.

```bash
python -m cookiecutter https://github.com/charlstown/py-template.git
```

??? warning "Don't clone this repository"

    You don't need to clone the template repository, cookiecutter will do that for you applying your own customization.


## The user guide

If you want to simply run the project as a user you can visit the [User Guide](https://charlstown.github.io/py-template/user-guide/getting-started/) to learn how to get started, set up and use this code.


## The Developer guide

If you want to contribute to the project or to have a deeply understanding about how the project works, you can visit the [Developer Guide](https://charlstown.github.io/py-template/dev-guide/contribute/).


## Documentation contents

The documentation site has the following pages structure.

```
mkdocs.yml                      # The configuration file.
docs/                           # Documents directory
├── assets                      # Assets directory
├── index.md                    # [page] Home
├── references.md               # [page] References
├── user-guide                  # User guide submenu
│   ├── getting-started.md      # [page] Getting started
│   ├── set-up.md               # [page] Set up
│   ├── usage.md                # [page] Usage             
│   └── ci-cd.md                # [page] CI/CD Github
└── dev-guide                   # Dev guide submenu
    ├── contribute.md           # [page] Contribute
    └── document.md             # [page] Document
```


## Contact and contributors

[Carlos Grande (@charlstown) - maintainer](https://github.com/charlstown)