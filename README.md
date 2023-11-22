# Prototipo-Publish-Subscribe

Pasos para la ejecución:

- Asegúrate de que Mosquitto esté instalado y en ejecución en la máquina donde actuará como broker. Si aún no lo has hecho, puedes seguir las instrucciones en el sitio web de Mosquitto para instalarlo.

- Ejecuta el broker de Mosquitto en la máquina donde lo hayas instalado.

- En la máquina de los publicadores y del primer suscriptor, ejecuta los scripts de Python. Puedes abrir diferentes terminales para ejecutar simultáneamente los scripts de publicadores y suscriptor.

- En la máquina de los suscriptores restantes, ejecuta los scripts de Python para los suscriptores.

- A medida que los scripts se ejecutan, deberías ver mensajes de salida indicando que los suscriptores están conectados y los mensajes que se están recibiendo.
