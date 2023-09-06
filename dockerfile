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