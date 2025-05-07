from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/pokemon', methods=['POST'])
def pokemon():
    nombre = request.form['nombre'].lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        imagen = data['sprites']['front_default']
        habilidades = [h['ability']['name'] for h in data['abilities']]
        peso = data['weight'] / 10  # convertir a kg
        altura = data['height'] / 10  # convertir a metros
        return render_template('result.html', nombre=nombre.capitalize(), imagen=imagen, habilidades=habilidades, peso=peso, altura=altura)
    else:
        return f"Pokémon '{nombre}' no encontrado. <a href='/'>Intentar otro</a>", 404

if __name__ == '__main__':
    app.run(debug=True, port= '0.0.0.0')
