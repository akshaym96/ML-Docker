# ML Flask Application with Docker

This repository contains a Dockerfile and instructions for creating a Docker image and container for running a Flask application that serves machine learning models for predictions. The Docker pipeline is designed to be extendable, allowing you to add more machine learning models to serve through the same Flask application.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Dockerfile Details](#dockerfile-details)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Adding More Models](#adding-more-models)
- [Interact with the API](#interact-with-the-API)

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- [Docker](https://www.docker.com/get-started)

## Getting Started
- Follow these instructions to build and run the Docker container for the Flask ML application.

## Dockerfile Details
- The Dockerfile included in this repository specifies the environment and dependencies required to run the Flask application and serve the machine learning model. It uses a Python base image and installs the necessary packages from the `requirements.txt` file.

```dockerfile
# Use a suitable base image
# 'FROM' This Dockerfile command is used to set the base image for the subsequent instructions. Every valid Dockerfile must start with a FROM command. 
# 'python:3.9-slim' This is the name and tag of the base image that you want to use. In this case, it refers to an official Python image hosted on Docker Hub.
FROM python:3.9-slim

# Set the working directory
#'WORKDIR': This is the Dockerfile command that sets the working directory.
#'/app': This is the path to the directory inside the container where you want subsequent commands to be executed. If the specified directory doesn't exist, Docker will create it.
#the 'WORKDIR /app' instruction means that all the following instructions in the Dockerfile will be run inside the /app directory in the container.
WORKDIR /app

# This command use to copy the necessary files into the container
# './': This is the destination path inside the image where the files will be copied. 
# The . refers to the current working directory inside the container, which was previously set to /app by the WORKDIR instruction. So the files will be copied to the /app directory inside the image.
COPY api.py churn_prediction_v1.pkl requirements.txt ./

# Install the required dependencies
# '--no-cache-dir': This option tells pip not to store the build cache from the installation of the packages. Using this option can make the resulting image smaller because unnecessary cache files are not saved.
#The -r option tells pip to install packages based on a requirements file. 
RUN pip install --no-cache-dir -r requirements.txt

#'EXPOSE': This Dockerfile command is used to tell Docker that the container will have a service running on the specified port.
# '5000': This is the port number that the container is expected to use for a specific service. In the context of a Flask application, it is common to run the app on port 5000.
# Expose the API port
EXPOSE 5000

# Run the API
CMD ["python", "api.py"]
```

## Building the Docker image

- Clone this repository to your local machine:
```
git clone https://github.com/your-username/ml-docker.git
```

- Navigate to the project directory:

```
cd ml-docker
```
- Build the Docker image using the provided Dockerfile:

```
docker build -t flask-ml-app .
```

This will create a Docker image named "flask-ml-app"

## Running the Docker Container
- After building the Docker image, you can run a container from it.

```
docker run -p 8080:5000 flask-ml-app
```

This command maps port 8080 on your host to port 5000 inside the container, where your application is running. Since the EXPOSE instruction in the Dockerfile indicated that the application inside the container will listen on port 5000, this mapping allows you to access the application by visiting http://localhost:8080 on the host machine.

## Adding More Models
- To extend this pipeline with additional machine learning models, follow these steps:

    - Add your new model code and related files to the project directory.

    - Modify the Flask application (app.py) to incorporate your new model and define the appropriate API endpoints.

    - Update the requirements.txt file with any additional Python packages required for your new model.

    - Rebuild the Docker image as explained in the "Building the Docker Image" section.

Now, you have a Docker container running a Flask application that serves multiple machine learning models through different API endpoints. You can access these endpoints by following the respective routes defined in your Flask application.

## Interact with the API

- With the docker container running you can send POST requests to http://localhost:8080/predict or anything similar to what you have mentioned in the flask code (api.py)
- You can use Postman to send POST request along with the raw JSON that is required by the api.