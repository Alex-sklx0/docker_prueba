from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Datos completos de la banda
band_info = {
    "name": "The Smashing Pumpkins",
    "year_formed": 1988,
    "hometown": "Chicago, Illinois",
    "genres": ["Alternative rock", "Dream pop", "Shoegaze", "Electronic rock"],
    "fun_facts": [
        "The band's name comes from a childhood fantasy Billy Corgan had about 'a smashed pumpkin'",
        "Their 1995 album 'Mellon Collie and the Infinite Sadness' was nominated for 7 Grammy Awards",
        "Billy Corgan wrote most of the band's songs and played most instruments on early albums",
        "The band has sold over 30 million albums worldwide",
        "Original bassist D'arcy Wretzky left the band in 1999"
    ],
    "current_members": [
        {
            "name": "Billy Corgan",
            "role": "Vocals, Guitar",
            "years": "1988-present",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Billy_Corgan_2014.jpg/800px-Billy_Corgan_2014.jpg"
        },
        {
            "name": "James Iha",
            "role": "Guitar",
            "years": "1988–2000, 2018–present",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/James_Iha_2018.jpg/800px-James_Iha_2018.jpg"
        },
        {
            "name": "Jeff Schroeder",
            "role": "Guitar",
            "years": "2007–present",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Jeff_Schroeder_2012.jpg/800px-Jeff_Schroeder_2012.jpg"
        },
        {
            "name": "Jack Bates",
            "role": "Bass",
            "years": "2015–present",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Jack_Bates_2019.jpg/800px-Jack_Bates_2019.jpg"
        },
        {
            "name": "Jimmy Chamberlin",
            "role": "Drums",
            "years": "1988–1996, 1999–2009, 2015–present",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jimmy_Chamberlin_2010.jpg/800px-Jimmy_Chamberlin_2010.jpg"
        }
    ],
    "former_members": [
        {
            "name": "D'arcy Wretzky",
            "role": "Bass",
            "years": "1988–1999",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/D%27arcy_Wretzky_1996.jpg/800px-D%27arcy_Wretzky_1996.jpg"
        },
        {
            "name": "Melissa Auf der Maur",
            "role": "Bass",
            "years": "1999–2000",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Melissa_Auf_der_Maur_2010.jpg/800px-Melissa_Auf_der_Maur_2010.jpg"
        }
    ],
    "albums": [
        {
            "name": "Gish",
            "year": 1991,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/1/12/SmashingPumpkinsGish.jpg",
            "highlights": ["I Am One", "Rhinoceros", "Bury Me", "Siva", "Crush"]
        },
        {
            "name": "Siamese Dream",
            "year": 1993,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/6/6b/SmashingPumpkinsSiameseDream.png",
            "highlights": ["Today", "Disarm", "Cherub Rock", "Mayonaise", "Rocket"]
        },
        {
            "name": "Mellon Collie and the Infinite Sadness",
            "year": 1995,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/0/00/Mellon_Collie_%26_the_Infinite_Sadness_cover.png",
            "highlights": ["Bullet with Butterfly Wings", "1979", "Tonight, Tonight", "Zero", "Thirty-Three"]
        },
        {
            "name": "Adore",
            "year": 1998,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/4/4f/Smashing_Pumpkins_-_Adore.png",
            "highlights": ["Ava Adore", "Perfect", "Daphne Descends", "To Sheila", "Pug"]
        },
        {
            "name": "Machina/The Machines of God",
            "year": 2000,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/4/4e/Machina_the_machines_of_god.jpg",
            "highlights": ["The Everlasting Gaze", "Stand Inside Your Love", "Try, Try, Try", "I of the Mourning", "This Time"]
        },
        {
            "name": "Oceania",
            "year": 2012,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/5/5e/Smashing_Pumpkins_-_Oceania.jpg",
            "highlights": ["Quasar", "Panopticon", "The Celestials", "Violet Rays", "One Diamond, One Heart"]
        },
        {
            "name": "Shiny and Oh So Bright, Vol. 1 / LP: No Past. No Future. No Sun.",
            "year": 2018,
            "cover_url": "https://upload.wikimedia.org/wikipedia/en/3/3c/Smashing_Pumpkins_-_Shiny_and_Oh_So_Bright.jpg",
            "highlights": ["Silvery Sometimes (Ghosts)", "Knights of Malta", "Solara", "Travels", "With Sympathy"]
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
