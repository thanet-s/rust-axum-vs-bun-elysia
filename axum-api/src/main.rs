use axum::{extract::Path, routing::post, Router, Json};
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    // Define your route
    let app = Router::new()
        .route("/bmi/:username", post(handle_request));

    // Set up the server
    let addr = SocketAddr::from(([0, 0, 0, 0], 3000));
    println!("axum is running at http://{}", addr);

    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}

async fn handle_request(Path(username): Path<String>, Json(data): Json<BmiData>) -> Json<BmiResponse> {
    let bmi = calculate_bmi(data.weight, data.tall);
    Json(BmiResponse { username, bmi })
}

fn calculate_bmi(weight: f64, tall: f64) -> f64 {
    weight / (tall / 100.0).powi(2)  // tall is in cm, so divide by 100 to convert to meters
}

#[derive(serde::Deserialize)]
struct BmiData {
    weight: f64,  // weight in kg
    tall: f64,    // height in cm
}

#[derive(serde::Serialize)]
struct BmiResponse {
    username: String,
    bmi: f64,
}
