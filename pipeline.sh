# !/bin/bash

set -e

echo "Iniciando pipeline de datos..."

# Paso 1: Descargar datos
echo "Descargando datos..."

wget -q -O archivo.csv 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,pl_bmasse+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+pl_bmasse+IS+NOT+NULL&amp;format=csv'

# Paso 2: Construir base de datos

echo "Construyendo base de datos..."
python3 constructor_db.py

# Paso 3: Analisis y visualizacion

echo "Generando analisis..."
python3 analisis_visual.py

echo "Pipeline completado exitosamente."
