cola = [
    {'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'},
    {'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'},
    {'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'},
    {'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'},
    {'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'},
    {'personaje': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'}
]

nombre_personaje_capitana_marvel = next(item['personaje'] for item in cola if item['superheroe'] == 'Capitana Marvel')
print("Personaje de la superhéroe Capitana Marvel:", nombre_personaje_capitana_marvel)

superheroes_femeninos = [item['superheroe'] for item in cola if item['genero'] == 'F']
print("Superhéroes femeninos:", superheroes_femeninos)

personajes_masculinos = [item['personaje'] for item in cola if item['genero'] == 'M']
print("Personajes masculinos:", personajes_masculinos)

nombre_superheroe_scott_lang = next(item['superheroe'] for item in cola if item['personaje'] == 'Scott Lang')
print("Superhéroe del personaje Scott Lang:", nombre_superheroe_scott_lang)

personajes_con_S = [item for item in cola if item['personaje'].startswith('S') or item['superheroe'].startswith('S')]
print("Personajes o superhéroes con nombres que comienzan con S:")
for personaje in personajes_con_S:
    print(personaje)

carol_danvers = next((item for item in cola if item['personaje'] == 'Carol Danvers'), None)
if carol_danvers is not None:
    nombre_superheroe_carol_danvers = carol_danvers['superheroe']
    print("El personaje Carol Danvers se encuentra en la cola.")
    print("Su nombre de superhéroe es:", nombre_superheroe_carol_danvers)
else:
    print("El personaje Carol Danvers no se encuentra en la cola.")
