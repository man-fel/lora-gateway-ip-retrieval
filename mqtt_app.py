import time
import paho.mqtt.client as mqtt
import subprocess

# MQTT Broker configuration
broker_address = "broker.emqx.io"
broker_port = 1883
topic = "ip_address"

# Function to get the current IP address
def get_ip_address():
    try:
        result = subprocess.check_output(["hostname", "-I"]).decode("utf-8")
        ip_address = result.split()[0]
        return ip_address
    except Exception as e:
        print("Error getting IP address:", e)
        return None

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to the desired topic upon successful connection
        client.subscribe(topic)
    else:
        print(f"Failed to connect to MQTT broker. Retrying in 5 seconds... (Error Code: {rc})")
        time.sleep(5)
        client.reconnect()

# Callback when message is received on MQTT topic
def on_message(client, userdata, msg):
    if msg.topic == topic:
        # Print the IP address
        ip_address = msg.payload.decode("utf-8")
        print(f"Received IP address from MQTT: {ip_address}")

# Main MQTT application
def mqtt_application():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    while True:
        try:
            client.connect(broker_address, broker_port, 60)
            break
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)

    ip_address = get_ip_address()
    if ip_address:
        client.publish(topic, ip_address)
        print(f"IP address published: {ip_address}")

    client.loop_forever()

if __name__ == "__main__":
    mqtt_application()
