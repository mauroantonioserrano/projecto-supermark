import sqlite3

conexion=sqlite3.connect("12.db ")
cursor=conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS producto (id INTEGER NOT NULL,nombre TEXT,precio REAL,PRIMARY KEY (id AUTOINCREMENT)) ") 
conexion.commit()
conexion.close()

