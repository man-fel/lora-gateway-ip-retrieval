from flask import Flask, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

# Function to get the local IP address of the server
def get_local_ip_address():
    try:
        # Create a socket object and connect to an external server (e.g., Google's DNS)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        print("Error getting local IP address:", e)
        return None

@app.route('/get_ip_address', methods=['GET'])
def get_ip_address():
    # Replace the default value with the actual logic to get the local IP address
    ip_address = get_local_ip_address()
    return jsonify({'ip_address': ip_address})

if __name__ == "__main__":
    # Run the Flask server on port 5000
    app.run(debug=True, port=5000)
