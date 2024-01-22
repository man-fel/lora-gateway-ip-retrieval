1. Prerequisites

Python 3.x
Pip (Python package installer)

2. Installation
Clone the Repository:
git clone https://github.com/man-fel/lora-gateway-ip-retrieval.git
cd lora-gateway-ip-retrieval

3. Install Python Dependencies:
pip install -r requirements.txt

4.Run the MQTT Application:
python3 mqtt_application.py
This script connects to an MQTT broker, retrieves the local IP address, and publishes it to a specified topic.

5. Run the Flask Server:
python3 flask_server.py
This script sets up a Flask server, ready to respond with the local IP address when requested.

6. Open the HTML Page:
Open index.html in a web browser.

7. Click the "Get IP Address" button to request the local IP address from the Flask server.