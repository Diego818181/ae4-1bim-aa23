"""
    Crear la base de datos de sqlite3
"""
import sqlite3
conn = sqlite3.connect('base_ejemplo_ciudades.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE ciudades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        poblacion INTEGER,
        pais TEXT
    )
''')

cursor.execute("INSERT INTO ciudades (nombre, poblacion, pais) VALUES (?, ?, ?)",
               ('Ciudad A', 1000000, 'Pais A'))

cursor.execute('''
    CREATE TABLE paises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        capital TEXT,
        idioma TEXT
    )
''')

cursor.execute("INSERT INTO paises (nombre, capital, idioma) VALUES (?, ?, ?)",
               ('Pais A', 'Ciudad A', 'Espaniol'))

conn.commit()

conn.close()