#!/bin/bash

set -e

build_image() {
    local dockerfile_path=$1
    local dockerfile_name=$2
    local image_name=$3

    docker build -t $image_name -f $dockerfile_path/$dockerfile_name $dockerfile_path
}

run_container() {
    local image_name=$1
    local container_name=$2
    local port=$3

    docker run -d --name $container_name -p $port:3000 $image_name
}

load_test() {
    local container_name=$1
    local port=$2

    echo "Starting load test for $container_name..."

    # Capture wrk output
    local output=$(wrk -t2 -c400 -d20s -s bmi-post-test.lua http://127.0.0.1:$port/bmi/test)

    # Extract values using awk
    local avg_latency=$(echo "$output" | awk '/Latency/ {gsub("ms","",$2); print $2}')
    local req_sec=$(echo "$output" | awk '/Requests\/sec/ {print $2}')
    local transfer_sec=$(echo "$output" | awk '/Transfer\/sec/ {gsub("MB","",$2); print $2}')

    # Append to CSV
    echo "$container_name,$avg_latency,$req_sec,$transfer_sec" >> results.csv

    echo "Load test for $container_name completed!"
}

# Create or overwrite the CSV file with headers
echo "container_type,avg_latency,requests_sec,transfer_sec" > results.csv

# List of Dockerfile paths, image names, corresponding container names, and ports
dockerfile_paths=("./axum-api" "./axum-api" "./elysia-api" "./elysia-api")
dockerfile_names=("Dockerfile" "Dockerfile.distroless" "Dockerfile" "Dockerfile.distroless")
images=("axum-api" "axum-api-distroless" "elysia-api" "elysia-api-distroless")
containers=("axum-api-container" "axum-api-distroless-container" "elysia-api-container" "elysia-api-distroless-container")
ports=("3001" "3002" "3003" "3004")

# Build images
for index in "${!dockerfile_paths[@]}"; do
    build_image "${dockerfile_paths[$index]}" "${dockerfile_names[$index]}" "${images[$index]}"
done

# Run containers and tests
for index in "${!images[@]}"; do
    run_container "${images[$index]}" "${containers[$index]}" "${ports[$index]}"
    sleep 5  # Give the container some time to initialize
    load_test "${containers[$index]}" "${ports[$index]}"
    docker container rm -f "${containers[$index]}"
done

# Plot the results
docker build -t graph_generator .
docker run --rm -v $(pwd)/performance_graphs:/app/performance_graphs -v $(pwd)/results.csv:/app/results.csv graph_generator
