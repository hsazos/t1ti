from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.


def home(request):

  response1 = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad")
  episodios_bb = response1.json()
  temporadas1 = []
  for episodio in episodios_bb:
    if int(episodio["season"]) not in temporadas1:
      temporadas1.append(int(episodio["season"]))
  response2 = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul")
  episodios_bcs = response2.json()
  temporadas2 = []
  for episodio in episodios_bcs:
    if int(episodio["season"]) not in temporadas2:
      temporadas2.append(int(episodio["season"]))
  return render(request, "main_app/home.html", {"tbb": temporadas1, "tbcs": temporadas2})

def season_bb(request, season_id):
  response = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad")
  todos = response.json()
  episodios = []
  for episodio in todos:
    if int(episodio["season"]) == season_id:
      episodios.append(episodio)
  return render(request, "main_app/season.html", {"episodios": episodios, "temporada":season_id})

def season_bcs(request, season_id):
  response = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul")
  todos = response.json()
  episodios = []
  for episodio in todos:
    if int(episodio["season"]) == season_id:
      episodios.append(episodio)
  return render(request, "main_app/season.html", {"episodios": episodios, "temporada":season_id})


def episode_bb(request, episode_name):
  response = requests.get(f"https://tarea-1-breaking-bad.herokuapp.com/api/episodes")
  episodios = response.json()
  for episodio in episodios:
    if episodio["title"] == episode_name:
      episodio_pedido = episodio
  return render(request, "main_app/episodio.html", {"info":episodio_pedido})


def episode_bcs(request, episode_name):
  response = requests.get(f"https://tarea-1-breaking-bad.herokuapp.com/api/episodes")
  episodios = response.json()
  for episodio in episodios:
    if episodio["title"] == episode_name:
      episodio_pedido = episodio
  return render(request, "main_app/episodio.html", {"info":episodio_pedido})

def characters(request, character_name):
  condicion = True
  offset = 0
  while condicion:
    
    response = requests.get(f"https://tarea-1-breaking-bad.herokuapp.com/api/characters?limit=10&offset={offset}")
    personajes_temp = response.json()
    for personaje in personajes_temp:
      if personaje["name"] == character_name:
        personaje_buscado = personaje
        condicion = False
        break
    offset += 10
  frases = []
  respuesta = requests.get("https://tarea-1-breaking-bad.herokuapp.com/api/quotes")
  frases_final = respuesta.json()
  for frase in frases_final:
    if frase["author"] == personaje_buscado["name"]:
      frases.append(frase)
  return render(request, "main_app/personaje.html",{"personaje": personaje_buscado, "frases":frases})



def buscar(request):

  hola = request.GET["busq"]
  hola = hola.replace(" ", "+")
  offset = 0
  condicion = True
  personajes = []
  
  while condicion:
    response = requests.get(f"https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={hola}&offset={offset}")
    response = response.json()
    for elemento in response:
      personajes.append(elemento)
    offset += 10
    if len(response) < 10:
      condicion = False
      break
  print(len(personajes))
  return render(request, "main_app/cuadro_busqueda.html",{"resultados": personajes})