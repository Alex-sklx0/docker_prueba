from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Datos ampliados de la banda
band_info = {
    "name": "The Smashing Pumpkins",
    "genres": ["Alternative rock", "Shoegaze", "Dream pop", "Electronica"],
    "year_formed": 1988,
    "hometown": "Chicago, Illinois, U.S.",
    "current_members": [
        {"name": "Billy Corgan", "role": "Vocals, Guitar", "years": "1988-present"},
        {"name": "James Iha", "role": "Guitar", "years": "1988-2000, 2018-present"},
        {"name": "Jimmy Chamberlin", "role": "Drums", "years": "1988-1996, 1999-2009, 2015-present"},
        {"name": "Jeff Schroeder", "role": "Guitar", "years": "2007-2023"}
    ],
    "former_members": [
        {"name": "D'arcy Wretzky", "role": "Bass", "years": "1988-1999"},
        {"name": "Melissa Auf der Maur", "role": "Bass", "years": "1999-2000"}
    ],
    "albums": [
        {"name": "Gish", "year": 1991, "cover": "gish.jpg", "highlights": ["I Am One", "Rhinoceros", "Bury Me"]},
        {"name": "Siamese Dream", "year": 1993, "cover": "siamese-dream.jpg", "highlights": ["Today", "Disarm", "Cherub Rock"]},
        {"name": "Mellon Collie and the Infinite Sadness", "year": 1995, "cover": "mellon-collie.jpg", "highlights": ["Bullet with Butterfly Wings", "1979", "Tonight, Tonight"]},
        {"name": "Adore", "year": 1998, "cover": "adore.jpg", "highlights": ["Ava Adore", "Perfect", "Daphne Descends"]}
    ],
    "fun_facts": [
        "El nombre de la banda viene de un incidente donde Billy Corgan imaginó a unas calabazas aplastándose",
        "El álbum 'Mellon Collie' fue nominado a 7 premios Grammy",
        "Billy Corgan escribió casi todas las canciones de la banda"
    ]
}

@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html',
                         band=band_info,
                         current_year=current_year)

@app.route('/discography')
def discography():
    return render_template('discography.html',
                         band=band_info)

@app.route('/about')
def about():
    return render_template('about.html',
                         band=band_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
