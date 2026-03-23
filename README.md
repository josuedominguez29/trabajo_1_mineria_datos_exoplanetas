# Proyecto: Análisis Masa-Radio de Exoplanetas

## 📌 Descripción

Este proyecto implementa un pipeline reproducible para el análisis de datos de exoplanetas provenientes del archivo público *NASA Exoplanet Archive*.

El objetivo es estudiar la relación entre la masa y el radio de los exoplanetas, con el fin de identificar la transición entre planetas rocosos densos y gigantes gaseosos.


---

## 🔬 Análisis Físico
La gráfica en escala log-log de masa vs radio muestra una clara distribución de los exoplanetas en dos regímenes principales.

Para radios menores a aproximadamente 1.5–2 radios terrestres, los planetas siguen una tendencia consistente con cuerpos rocosos, donde un aumento en el radio implica un incremento significativo en la masa. Esto es característico de planetas densos con composiciones similares a la Tierra.

Por otro lado, para radios mayores a ~2 radios terrestres, la relación masa-radio se vuelve más dispersa. En esta región, los planetas aumentan considerablemente su radio sin un incremento proporcional en la masa, lo que indica la presencia de envolturas gaseosas.

Esta transición marca el paso de planetas rocosos a gigantes gaseosos o sub-neptunos, donde la densidad promedio disminuye significativamente.

---

## 📊 Resultados ![Relación Masa vs Radio](resultado.png)

---

## ⚙️ Reproducibilidad

Para ejecutar el proyecto:

```bash
git clone https://github.com/josuedominguez29/trabajo_1_mineria_datos_exoplanetas.git
cd trabajo_1_mineria_datos_exoplanetas
bash pipeline.sh

