# Dockerfile for a simple Flask application

FROM python:3-onbuild

# Optionally set the maintainer
MAINTAINER Andrew T. Baker <andrew.tork.baker@gmail.com>

# Based on instructions for the base image: https://registry.hub.docker.com/u/library/python/

# Expose port 8000 for Gunicorn to serve the app
EXPOSE 8000

# Set the default command for this image 
CMD gunicorn -c gunicorn_config.py flask-example:app
