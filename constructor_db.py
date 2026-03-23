import pandas as pd
import sqlite3

print("Leyendo archivo CSV...")

# Leer datos
df = pd.read_csv("archivo.csv")

print("Filas originales:", len(df))

# --- LIMPIEZA  DE LOS DATOS ---

print("Iniciando limpieza de datos...")

# 1. Eliminar duplicados
df = df.drop_duplicates()

# 2. Convertir a valores numéricos (por seguridad)
df["pl_rade"] = pd.to_numeric(df["pl_rade"], errors="coerce")
df["pl_bmasse"] = pd.to_numeric(df["pl_bmasse"], errors="coerce")

# 3. Eliminar filas con valores nulos
df = df.dropna()

# 4. Filtrar valores físicamente razonables
df = df[(df["pl_rade"] > 0) & (df["pl_bmasse"] > 0)]

print("Limpieza completada.")
print("Filas despues de limpieza:", len(df))

print("Datos cargados correctamente.")

# ----------------------------------------------------

# Conectar a base de datos SQLite
conn = sqlite3.connect("datos_mision.db")

print("Guardando datos en SQLite...")

# Guardar en tabla
df.to_sql("exoplanetas", conn, if_exists="replace", index=False)

conn.close()

print("Base de datos creada exitosamente.")
