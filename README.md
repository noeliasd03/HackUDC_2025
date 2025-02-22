# Global Wealth 2021 🌍💰



## Descripción 📖
Principalmente, hemos creado un chatbot basado en LLM (Gemini 1.5) que responda en base a un dataset sobre economía global en el año 2021. 

Como añadido, hemos incluído una serie gráficas que nos permitan comprender mejor los datos de los que disponemos.

El objetivo será crear esto integrando la herramientas de trabajo de Denodo.

<!-- <img src="https://media.licdn.com/dms/image/v2/C4D0BAQF5UWSiPzwwqw/company-logo_200_200/company-logo_200_200/0/1630541945157/denodo_technologies_logo?e=1748476800&v=beta&t=vC6GNejzp3qAWaTVcCQyyKd_Mb-AY3gUuF5WlcPtnRU" alt="Denodo image" width="50" height=auto> -->

## Tecnologías 🛠️
  - **Denodo Express**. Esta solución nos permite añadir los datasets personalizados desde diversas fuentes (csv,texto plano,hdfs...).
  - **Denodo Studio**. Nos permite crear bases de datos en base a los datasets, además de las relaciones entre bases de datos. Las relaciones son útiles para el LLM a la hora de hacer inferencia en las respuestas.
  - **Denodo AI SDK**. Esta herramienta proporciona agilidad a la hora de transformar los datos (embbedings, BD vectorial) y proporcionarlos al chatbot a través de una API. 
  - Integración Denodo con **Grafana**
  - **Gradio**. Biblioteca de Python para crear interfaces web interactivas y compartir modelos de machine learning fácilmente.

## Fuentes de datos 📚
- [500 Richest People 2021](https://www.kaggle.com/datasets/frtgnn/500-richest-people-2021)

- [PIB-GDP Global by countries since 1960](https://www.kaggle.com/datasets/fredericksalazar/pib-gdp-global-by-countries-since-1960-to-2021)
- [World Economic Data](https://www.kaggle.com/datasets/madhurpant/world-economic-data/data?select=cost_of_living.csv). Se ha empleado 'cost_of_living.csv'


## Instalación ⚙️
  > Requisito: Python 3.13.2
  1. Realizar integración de datos siguiendo la documentación técnica de DenodoPlatform
  2. Instalación librerías:
    ```
    pip install -r auxiliar/requirements.txt
    ```
  3. Levantar la UI:
    ```
    python ui_global_wealth.py
    ```


## Equipo 👥
Y nada de esto hubiese salido adelante sin el incansable trabajo que hemos realizado juntos durante estas 36 horas
  - Noelia Sánchez
  - Javi Esmorís
  - Celia Incera
  - Inés Poses

## Licencia
Este proyecto está licenciado bajo la **GNU General Public License (GPL)**, lo que permite a cualquier persona usar, modificar y distribuir el código, siempre que se mantenga la misma licencia. Asegura la libertad de compartir y mejorar el software para todos.