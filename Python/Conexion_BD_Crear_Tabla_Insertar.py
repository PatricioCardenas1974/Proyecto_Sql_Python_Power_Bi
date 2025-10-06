import pyodbc
import pandas as pd
import random
import time

conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PATRICIO;'
    'DATABASE=Dataxelab;'
    'Trusted_Connection=yes;'
    'Encrypt=no;TrustServerCertificate=yes;'
)

cursor = conexion.cursor()

cursor.execute("DELETE FROM datos_ventas_directquery;")
conexion.commit()
print("Tabla vaciada, Inicio Simulacion")


# Bucle limitado a 50 iteraciones (osea 50 registros)
for _ in range(50):
    registro = (
        pd.Timestamp.now(),
        random.randint(5,20),
        random.randint(0,5),
        random.randint(10,50),
        random.randint(5,30),
        random.choice(["Santiago", "Concepción", "Valparaiso"]),
        random.choice(["Corte Intempestivo", "Lenta Conexion", "Facturacion incorrecta"]),
        random.choice(["Juan", "Maria", "Pedro"]),
        random.choice(["Whatsapp", "Pagina Web", "Call Center"]),
        random.choice(["En Proceso", "Completado", "Rechazado"]),
        random.choice(["Cliente Desiste", "Error direccion", "Espera alta"]),
        random.choice(["Sin Cobertura", "Sin stockj", "Error Sistema"]),
        random.randint(0,10),
        random.randint(0,15),
        random.randint(0,10)
    )
    try:
        cursor.execute(
            """INSERT INTO datos_ventas_directquery
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", registro)
        conexion.commit()
        print("Nuevo dato insertado:", registro)
    except Exception as e:
        print("Error al insertar:", e)
    time.sleep(5)

print("Simulación finalizada: 50 registros insertados")


# Bucle ilimitado de registros

# while True:
#         registro = (
#         pd.Timestamp.now(),
#         random.randint(5,20),
#         random.randint(0,5),
#         random.randint(10,50),
#         random.randint(5,30),
#         random.choice(["Santiago", "Concepción", "Valparaiso"]),
#         random.choice(["Corte Intempestivo", "Lenta Conexion", "Facturacion incorrecta"]),
#         random.choice(["Juan", "Maria", "Pedro"]),
#         random.choice(["Whatsapp", "Pagina Web", "Call Center"]),
#         random.choice(["En Proceso", "Completado", "Rechazado"]),
#         random.choice(["Cliente Desiste", "Error direccion", "Espera alta"]),
#         random.choice(["Sin Cobertura", "Sin stockj", "Error Sistema"]),
#         random.randint(0,10),
#         random.randint(0,15),
#         random.randint(0,10)
#     )
#         try:
#                 cursor.execute(
#                         """INSERT INTO datos_ventas_directquery
#                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", registro)
#                 conexion.commit()
#                 print("Nuevo dato insertado:", registro)
        
#         except Exception as e:
#                 print("Error al insertar:", e)
#         time.sleep(5)