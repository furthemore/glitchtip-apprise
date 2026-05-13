# Use the Python base image
FROM python:3-alpine

# Set a working directory
WORKDIR /func

# Copy all the files from the local directory into the container
COPY . .

# Install the Functions Framework
RUN pip install --upgrade pip
RUN pip install functions-framework

# Install any dependencies of the function
RUN pip install -r requirements.txt

EXPOSE 8080

ENV PYTHONUNBUFFERED=1

# Run the function
CMD ["functions-framework", "--target=main"]
