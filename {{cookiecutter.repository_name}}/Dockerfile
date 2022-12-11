# Project: {{cookiecutter.repository_name}}
# Author/s: {{cookiecutter.author}}
# -----------------------------------------------------


# Select the base image
FROM python:3.8-slim

# Copy the files to run the app
COPY src /{{cookiecutter.project_name}}/src/{{cookiecutter.package_name}}
COPY data /{{cookiecutter.project_name}}/data
COPY requirements.txt /{{cookiecutter.project_name}}

# Install python and other common libraries
RUN apt-get update -y && \
    apt-get -y install \
    ca-certificates \
    openssh-client \
    gcc \
    libc-dev \
    tdsodbc \
    g++ \
    libffi-dev \
    libxml2 \
    unixodbc-dev \
    python3-pip \
    nano && \
    pip3 install -r /{{cookiecutter.project_name}}/requirements.txt &&\
    pip3 install --upgrade pip

# Select the working directory
WORKDIR /{{cookiecutter.project_name}}

# Add this comand to avoid the container to close after the execution
#CMD tail -f /dev/null

# Execute the script
CMD [ "python", "src/main.py", "-l", "debug" ]
