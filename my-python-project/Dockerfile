# Project: my-python-project
# Author/s: Carlos Grande
# -----------------------------------------------------


# Select the base image
FROM python:3.8-slim

# Copy the files to run the app
COPY src /My Python Project/src/my_python_project
COPY data /My Python Project/data
COPY requirements.txt /My Python Project

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
    pip3 install -r /My Python Project/requirements.txt &&\
    pip3 install --upgrade pip

# Select the working directory
WORKDIR /My Python Project

# Add this comand to avoid the container to close after the execution
#CMD tail -f /dev/null

# Execute the script
CMD [ "python", "src/main.py", "-l", "debug" ]
