# Performance Comparison: Axum vs. Elysia

This project aims to compare the performance of web APIs built using [Axum](https://github.com/tokio-rs/axum) from the [Rust](https://www.rust-lang.org/) ecosystem and [Elysia](https://github.com/elysiajs/elysia) from the [Bun](https://bun.sh/) runtime. We'll measure various metrics such as average latency, requests per second, and data transfer rates.

## Prerequisites

- Docker
- `wrk` (e.g., you can install it using `brew install wrk` on macOS)

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/thanet-s/rust-axum-vs-bun-elysia.git
    cd rust-axum-vs-bun-elysia
    ```

2. **Run the Performance Tests**

    ```bash
    chmod +x loadtest.sh
    ./loadtest.sh
    ```

3. **Generate the Performance Graphs**

    After the tests are completed, the performance comparison graphs will be generated and saved to the `performance_graphs` directory.

## Viewing Results

Navigate to the `performance_graphs` directory to view the generated performance comparison graphs.

## Contributing

If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is under the MIT License. See [LICENSE](LICENSE) for more information.

# Acknowledgements

- The Axum team for their robust Rust framework.
- The Elysia team for their outstanding framework tailored for the Bun runtime.
