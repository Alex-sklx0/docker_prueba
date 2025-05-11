# app/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Servicio telemático funcionando!"

@app.route('/api/data')
def get_data():
    return {"message": "Datos del servicio", "status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
