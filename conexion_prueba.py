import sqlite3
def agregar_productos(ruta,a):
    conexion=sqlite3.connect(ruta)
    cursor=conexion.cursor()
    cursor.executemany("INSERT INTO Producto VALUES(?,?,?)",a)
    conexion.commit()
    conexion.close()


productos=[(None,"plasma",300)]
agregar_productos("basededatosdesupermercado.db",productos)

