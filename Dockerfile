FROM python:3.11-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python libraries
RUN pip install matplotlib pandas

# Set working directory
WORKDIR /app

# Copy the script and data
COPY generate_graphs.py ./

# Command to run the script
CMD ["python", "generate_graphs.py"]
