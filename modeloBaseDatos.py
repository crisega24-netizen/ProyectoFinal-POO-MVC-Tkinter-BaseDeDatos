import mysql.connector

def hacerConexion():
    host = "localhost"
    user = "root"
    password = ""     
    database = "Invernadero"

    try:
        conexion = mysql.connector.connect(host=host, user=user, password=password, database=database)
        if conexion.is_connected():
            print("Conexión a la base de datos establecida correctamente.")
            return conexion
        else:
            print("No fue posible establecer la conexión con la base de datos.")
            return None
    except:
        print("Error: no se pudo conectar a la base de datos. Revisa credenciales y que el servidor MySQL esté activo.")
        return None