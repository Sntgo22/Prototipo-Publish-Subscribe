# publicador_python_2.py
import paho.mqtt.client as mqtt
import time

def on_publish(client, userdata, result):
    print("Tercer publicador: Mensaje publicado con éxito")

client = mqtt.Client()
client.connect("tu_direccion_ip_broker", 1883, 60)

for i in range(3):
    mensaje = f"Tercer publicador: Mensaje {i+1} desde Python"
    topic = "topic/ejemplo"
    client.publish(topic, mensaje)
    time.sleep(1)

client.disconnect()
