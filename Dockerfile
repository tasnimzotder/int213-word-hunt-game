FROM python:3.7-slim

# copy the project files
COPY int213-word-hunt-game /app

# set the working directory
WORKDIR /app

# install tkinter
RUN apt-get update && apt-get install -y python3-tk

# install the dependencies
RUN pip install -r requirements.txt

# run the project
CMD ["python", "main.py"]
