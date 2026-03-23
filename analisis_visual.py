import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

print("Conectando a la base de datos...")

# Conectar a SQLite
conn = sqlite3.connect("datos_mision.db")

# Consulta SQL
query = "SELECT pl_rade, pl_bmasse FROM exoplanetas"

df = pd.read_sql_query(query, conn)

conn.close()

print("Datos cargados desde SQLite.")

# Extraer variables
radio = df["pl_rade"]
masa = df["pl_bmasse"]

print("Generando grafica...")

# Crear scatter plot
plt.figure()
plt.scatter(radio, masa)

# Escalas logaritmicas (MUY IMPORTANTE)
plt.xscale("log")
plt.yscale("log")

# Etiquetas
plt.xlabel("Radio (Tierras)")
plt.ylabel("Masa (Tierras)")
plt.title("Masa vs Radio de Exoplanetas")

# Guardar imagen
plt.savefig("resultado.png")

#plt.show()

print("Grafica guardada como resultado.png")
