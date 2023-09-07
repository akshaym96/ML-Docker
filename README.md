# ML Flask Application with Docker

This repository contains a Dockerfile and instructions for creating a Docker image and container for running a Flask application that serves machine learning models for predictions. The Docker pipeline is designed to be extendable, allowing you to add more machine learning models to serve through the same Flask application.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Dockerfile Details](#dockerfile-details)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Adding More Models](#adding-more-models)

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- [Docker](https://www.docker.com/get-started)

## Getting Started
- Follow these instructions to build and run the Docker container for the Flask ML application.

## Dockerfile Details
- The Dockerfile included in this repository specifies the environment and dependencies required to run the Flask application and serve the machine learning model. It uses a Python base image and installs the necessary packages from the `requirements.txt` file.

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## Building the Docker image

- Clone this repository to your local machine:
```
git clone https://github.com/your-username/flask-ml-docker.git
```

- Navigate to the project directory:

```
cd flask-ml-docker
```
- Build the Docker image using the provided Dockerfile:

```
docker build -t flask-ml-app .
```

This will create a Docker image named flask-ml-app.

## Running the Docker Container
- After building the Docker image, you can run a container from it.

```
docker run -p 8080:5000 flask-ml-app
```

This command maps port 8080 on your host to port 5000 inside the container, where your application is running. You can access the Flask application by opening a web browser and navigating to http://localhost:8080.

## Adding More Models
- To extend this pipeline with additional machine learning models, follow these steps:

    - Add your new model code and related files to the project directory.

    - Modify the Flask application (app.py) to incorporate your new model and define the appropriate API endpoints.

    - Update the requirements.txt file with any additional Python packages required for your new model.

    - Rebuild the Docker image as explained in the "Building the Docker Image" section.

Now, you have a Docker container running a Flask application that serves multiple machine learning models through different API endpoints. You can access these endpoints by following the respective routes defined in your Flask application.

