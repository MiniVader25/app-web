from flask import Flask
import random
app = Flask(__name__)

facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos"
"Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones."
"El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna"
"Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo"
"Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"
"Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos"
"Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos"
"Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

passwords_list = ["Contraseña123!", "MiPerroEsGenial2024$", "VacacionesEnLaPlaya#1", "CaféConLeche2024@", "AventurasEnMontaña!2024", "TecnologíaYVida2024%", "ExplorandoElMundo$2024", "SeguridadPrimero!2024"]

@app.route("/")
def hello_world():
    return '''<h1>Hello, World!</h1>
    <a href = "/2">Ir a la página 2</a>
    <br>
    <a href = "/dependencia">Ir a datos random </a>

    '''
@app.route("/dependencia")
def dependencia():
    return f'<h1>{random.choice(facts_list)}</h1>'

@app.route("/contraseña")
def contraseña():
    return f'<h1>{random.choice(passwords_list)}</h1>'

@app.route("/2")
def Página2():
    return '<h1>Hello, desde la página 2 👋!</h1>'

@app.route("/nombre")
def saludar(nombre):
    return f'<h1>Hola, {nombre}!</h1>'


app.run(debug=True)
