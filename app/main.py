from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Datos de la banda
band_info = {
    "name": "The Smashing Pumpkins",
    "genres": ["Alternative rock", "Shoegaze", "Dream pop"],
    "year_formed": 1988,
    "members": [
        {"name": "Billy Corgan", "role": "Vocals, Guitar"},
        {"name": "James Iha", "role": "Guitar"},
        {"name": "Jimmy Chamberlin", "role": "Drums"},
        {"name": "D'arcy Wretzky", "role": "Bass"}
    ],
    "albums": [
        {"name": "Siamese Dream", "year": 1993},
        {"name": "Mellon Collie and the Infinite Sadness", "year": 1995},
        {"name": "Adore", "year": 1998}
    ]
}

@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html', 
                         band=band_info,
                         current_year=current_year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
