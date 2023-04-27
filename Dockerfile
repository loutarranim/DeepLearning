FROM python:3.10.10

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx 
    

RUN pip install Cython==0.29.32
RUN pip install numpy==1.23.5
RUN pip install -r requirements.txt
RUN pip install gunicorn


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
#cloud run avec gunicorn