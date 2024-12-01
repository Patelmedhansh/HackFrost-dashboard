from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Set response headers
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()

            # Load metrics from environment variables
            temperature = os.getenv("WEATHER_TEMPERATURE_CELSIUS", "25")
            humidity = os.getenv("WEATHER_HUMIDITY_PERCENT", "60")

            # Log metrics for debugging
            print(f"Serving metrics: temperature={temperature}, humidity={humidity}")

            # Serve metrics in Prometheus format
            self.wfile.write(f"weather_temperature_celsius {temperature}\n".encode("utf-8"))
            self.wfile.write(f"weather_humidity_percent {humidity}\n".encode("utf-8"))
        except Exception as e:
            print(f"Error while serving metrics: {e}")

if __name__ == "__main__":
    try:
        print("Starting metrics server on port 8081...")
        server = HTTPServer(("0.0.0.0", 8081), MetricsHandler)
        server.serve_forever()
    except Exception as e:
        print(f"Failed to start server: {e}")