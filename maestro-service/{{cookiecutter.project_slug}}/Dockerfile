#Download Python from DockerHub and use it
FROM python:3.11.9

#Set the working directory in the Docker container
WORKDIR /code

#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY src/ .

EXPOSE 80

#Run the container
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
