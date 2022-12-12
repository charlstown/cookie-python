# CI/CD with GitHub Actions


https://github.com/marketplace?category=&query=&type=actions&verification=


# How to use GitHub actions?

Create a `.github/workflows` folder in your repository and add a `.yml` file with the following content:

```sh
mkdir -p .github/workflows
touch .github/workflows/testing.yml
touch .github/workflows/documentation.yml
```


## Components of GitHub actions

The following is a complete GitHub actions for create documentations (check out the comments for each component):

```yml
name: documentation # Name of the workflow
on: # Events that trigger the workflow
push: # Trigger the workflow on push
    branches: # Branches to run the workflow on
    - master # Run the workflow on the master branch
    - main # Run the workflow on the main branch
pull_request: # Trigger the workflow on pull request
    branches: # Branches to run the workflow on
    - master # Run the workflow on the master branch
    - main # Run the workflow on the main branch
jobs: # Jobs to run
build-docs: # Name of the job
    runs-on: ubuntu-latest # Operating system to run the job on
    steps: # Steps to run
    - name: Checkout repo # Name of the step
        uses: actions/checkout@v2 # Action to run
    - name: Set up Python # Name of the step
        uses: actions/setup-python@v2 # Action to run
        with: # Inputs for the action
        python-version: 3.7.13 # Version of Python to use
    - name: Caching # Name of the step
        uses: actions/cache@v2 # Action to run
        with: # Inputs for the action
        path: $/{/{ env.pythonLocation /}/} # Path to cache
        key: $/{/{ env.pythonLocation /}/}-$/{/{ hashFiles('setup.py') /}/}-$/{/{ hashFiles('requirements.txt') /}/} # Key to use for restoring and saving the cache
    - name: Install dependencies # Name of the step
        run: | # Command to run
        python -m pip install -e ".[docs]" --no-cache-dir
    - name: Deploy documentation # Name of the step
        run: mkdocs gh-deploy --force # Command to run
```