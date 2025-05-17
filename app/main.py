from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Datos de la banda (versión simplificada)
band_info = {
    "name": "The Smashing Pumpkins",
    "year_formed": 1988,
    "hometown": "Chicago, Illinois",
    "fun_facts": [
        "El nombre de la banda viene de una fantasía infantil de Billy Corgan",
        "Su álbum 'Mellon Collie and the Infinite Sadness' fue nominado a 7 Grammys",
        "Billy Corgan escribió la mayoría de las canciones y tocó muchos instrumentos",
        "Han vendido más de 30 millones de álbumes mundialmente",
        "El bajista original D'arcy Wretzky dejó la banda en 1999"
    ],
    "current_members": [
        {
            "name": "Billy Corgan",
            "role": "Vocals, Guitar",
            "years": "1988-present",
            "image_url": "https://i.pinimg.com/originals/68/34/91/683491680984319527.jpg"  # Nueva imagen de Pinterest
        },
        {
            "name": "James Iha",
            "role": "Guitar",
            "years": "1988–2000, 2018–present",
            "image_url": "https://i.pinimg.com/originals/53/63/50/536350636882119722.jpg"  # Nueva imagen de Pinterest
        },
        {
            "name": "Jimmy Chamberlin",
            "role": "Drums",
            "years": "1988–1996, 1999–2009, 2015–present",
            "image_url": "https://www.thedrummersjournal.com/wp-content/uploads/2021/02/Jimmy-Chamberlin-Interview-Featured-Image.jpg"  # Imagen del Drummer's Journal
        }
    ],
    "albums": [
        {
            "name": "Siamese Dream",
            "year": 1993,
            "cover_url": "https://tierraadentro.fondodeculturaeconomica.com/wp-content/uploads/2023/07/Smashing-Pumpkins-Siamese-Dream-1993.jpg",  # Imagen del artículo
            "highlights": ["Today", "Disarm", "Cherub Rock", "Mayonaise", "Rocket"]
        }
    ],
    "background_image": "https://live.staticflickr.com/65535/51102823438_8a0c1a8f4b_b.jpg"
}

@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html',
                         band=band_info,
                         current_year=current_year)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
