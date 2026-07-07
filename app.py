aqui se vera el codigo usado para hacer la conexion entre 
el esp32 y el arduino.

from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

ultimo_dato = {
    "temperatura": "Sin datos",
    "humedad": "Sin datos",
    "estado": "Esperando datos",
    "fecha": "Sin registro"
}

historial = []

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        dato=ultimo_dato,
        historial=historial
    )

@app.route("/registrar", methods=["POST"])
def registrar():
    global ultimo_dato

    data = request.get_json()

    temperatura = data.get("temperatura")
    humedad = data.get("humedad")
    estado = data.get("estado")

    nuevo_dato = {
        "temperatura": temperatura,
        "humedad": humedad,
        "estado": estado,
        "fecha": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    ultimo_dato = nuevo_dato
    historial.insert(0, nuevo_dato)

    if len(historial) > 20:
        historial.pop()

    print("Dato recibido:", nuevo_dato)

    return jsonify({"mensaje": "Dato recibido correctamente"}), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
