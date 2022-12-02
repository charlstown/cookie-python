# Project: Python Project
# Author/s: Carlos Grande
# -----------------------------------------------------


# Select the base image
FROM python:3.8-slim

# Copy the files to run the app
COPY code /Python Project/code
COPY data /Python Project/data
COPY requirements.txt /Python Project

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
    pip3 install -r /Python Project/requirements.txt &&\
    pip3 install --upgrade pip

# Select the working directory
WORKDIR /Python Project

# Add this comand to avoid the container to close after the execution
#CMD tail -f /dev/null

# Execute the script
CMD [ "python", "code/main.py", "-l", "debug" ]
