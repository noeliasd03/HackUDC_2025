# HackUDC_2025

## RAG AI SDK + Denodo Platform <img src="https://media.licdn.com/dms/image/v2/C4D0BAQF5UWSiPzwwqw/company-logo_200_200/company-logo_200_200/0/1630541945157/denodo_technologies_logo?e=1748476800&v=beta&t=vC6GNejzp3qAWaTVcCQyyKd_Mb-AY3gUuF5WlcPtnRU" alt="Denodo image" width="70" height=auto>

### Objetivo
Creación de un chatbot basado en LLM (Gemini 1.5) que responda en base a un dataset personalizado a través de RAG. De esta forma, el modelo de lenguaje podrá tener conocimiento dado un contexto que nosotros le demos y podrá responder las preguntas que se le hagan. El objetivo será crear esto con Denodo Platform y las tecnologías que proporciona:

  - Denodo Express. Esta solución nos permite añadir los datasets personalizados desde diversas fuentes (csv,texto plano,hdfs...).
  - Denodo Studio. Nos permite crear bases de datos en base a los datasets, además de las relaciones entre bases de datos. Las relaciones son útiles para el LLM a la hora de hacer inferencia en las respuestas.
  - Denodo AI SDK. Esta herramienta proporciona agilidad a la hora de transformar los datos (embbedings, BD vectorial) y proporcionarlos al chatbot a través de una API. 
