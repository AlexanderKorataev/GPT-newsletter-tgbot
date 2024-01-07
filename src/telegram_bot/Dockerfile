# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files into the container
COPY requirements.txt /app/telegram_bot/
COPY main.py /app/telegram_bot/
COPY bot /app/telegram_bot/bot

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r telegram_bot/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Run main.py when the container launches
CMD ["python", "telegram_bot/main.py"]
