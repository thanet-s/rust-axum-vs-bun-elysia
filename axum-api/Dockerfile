FROM rust:1.73-slim-bullseye as builder

WORKDIR /usr/src/axum-api

COPY Cargo.toml Cargo.lock ./
RUN mkdir src && echo "fn main() {}" > src/main.rs
RUN cargo build --release
COPY ./src ./src
RUN cargo install --path .

# Start a new stage for a smaller final image
FROM rust:1.73-slim-bullseye

WORKDIR /app

COPY --from=builder /usr/local/cargo/bin/axum-api .

CMD ["./axum-api"]

EXPOSE 3000