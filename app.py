from flask import Flask, request, jsonify, render_template
from datetime import datetime
from supabase import create_client, Client

app = Flask(__name__)

SUPABASE_URL = "https://wjjyrdeezbonxgmkkwet.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndqanlyZGVlemJvbnhnbWtrd2V0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODM1NDQ1ODgsImV4cCI6MjA5OTEyMDU4OH0.UzHrUFQUTQkN-orUifkoQ2q3zD5cZivy515AHLI1R_A"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

ultimo_dato = {
    "temperatura": "--",
    "humedad": "--",
    "estado": "SIN DATOS",
    "fecha": "--"
}

historial = []

@app.route("/")
def inicio():
    return render_template("index.html", dato=ultimo_dato, historial=historial)

@app.route("/registrar", methods=["POST"])
def registrar():
    global ultimo_dato

    try:
        data = request.get_json()

        temperatura = data.get("temperatura")
        humedad = data.get("humedad")
        estado = data.get("estado")

        fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        nuevo_dato = {
            "temperatura": temperatura,
            "humedad": humedad,
            "estado": estado,
            "fecha": fecha
        }

        ultimo_dato = nuevo_dato
        historial.insert(0, nuevo_dato)

        if len(historial) > 20:
            historial.pop()

        supabase.table("registros_iot").insert({
            "temperatura": temperatura,
            "humedad": humedad,
            "estado": estado
        }).execute()

        print("--------------------------------")
        print("Dato recibido desde ESP32")
        print("Temperatura:", temperatura)
        print("Humedad:", humedad)
        print("Estado:", estado)
        print("Guardado en Supabase correctamente")
        print("--------------------------------")

        return jsonify({"mensaje": "Datos registrados correctamente"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("====================================")
    print(" SERVIDOR IoT INICIADO ")
    print(" http://192.168.1.14:5000")
    print(" Esperando datos desde ESP32...")
    print("====================================")

    app.run(host="0.0.0.0", port=5000, debug=True)