from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['base_ejemplo_mongodb']

ciudades_collection = database['ciudades']

ciudad = {
    'nombre': 'Ciudad A',
    'pais': 'Pais A',
    'poblacion': 1000000
}
ciudades_collection.insert_one(ciudad)

ciudad = {
    'nombre': 'Ciudad B',
    'pais': 'Pais A',
    'poblacion': 1000000
}
ciudades_collection.insert_one(ciudad)

ciudad = {
    'nombre': 'Ciudad C',
    'pais': 'Pais B',
    'poblacion': 1000000
}
ciudades_collection.insert_one(ciudad)

paises_collection = database['paises']

pais = {
    'nombre': 'Pais A',
    'continente': 'Continente A',
    'idioma': 'Idioma A'
}
paises_collection.insert_one(pais)

pais = {
    'nombre': 'Pais B',
    'continente': 'Continente A',
    'idioma': 'Idioma A'
}
paises_collection.insert_one(pais)

ciudades = ciudades_collection.find()
for ciudad in ciudades:
    print(ciudad)

paises = paises_collection.find()
for pais in paises:
    print(pais)
