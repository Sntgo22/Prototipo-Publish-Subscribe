# suscriptor_python_2.py
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Conectado con código de resultado {rc}")
    client.subscribe("topic/ejemplo")

def on_message(client, userdata, msg):
    print(f"Segundo suscriptor: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("tu_direccion_ip_broker", 1883, 60)

client.loop_forever()
