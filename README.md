# PROMTIOR CHALLENGE
Aqui presento el challenge de PROMTIOR

### Atencion :technologist:
En esta branch main tenes acceso a solo la aplicacion backend, la aplicacion frontend se encuentra en la branch rag_app_front. En la seccion docs tenes acceso a la documentacion detallada, diagramas y capturas.

## Iniciemos :boom:

Las siguientes instrucciones te permitiran tener una copia del proyecto funcionando en tu maquina local. En la seccion de **despliegue** tendrás
los links del proyecto desplegado. 


### Pre-Requisitos :technologist:

Aqui presentamos que cosas necesitas para correr las apps. 
```
- Docker
- Docker-compose
- Docker-desktop (En caso de windows)
```

## Diagrama y resumen :computer:
![diagram](https://github.com/user-attachments/assets/255aaa68-0735-40b2-baac-909b156169bb)
Como podemos observar la solución se divide en dos partes. La parte del frontend, la cual interactúa con el usuario fue desarrollada en Angular, dockerizada y desplegada en Azure. La parte del backend fue desarrollada en Python, en la cual se divide en dos partes, los módulos de la arquitectura RAG y la API desarrollada con la librería FAST API, toda la app fue también dockerizada y deployada en azure.
Lo más importante es la arquitectura RAG la cual fue desarrollada en 4 módulos.
1. Data Source Module
2. Retrieval Module
3. Argumentation Module
4. Generation Module

Data Source Module brinda los datos necesarios para la aplicación, como son en este caso el pdf del challenge y también el texto encontrado en la web de Promtior. 

Retrieval Module recibe los datos de entrada, como primer paso aplica un método de separación de datos, en este caso la recursividad.  Dicho método nos permite obtener fragmentos de textos adecuados, organizados en cierto patrón y tamaño. El segundo paso consiste en guardar en una base de datos de vectores los datos obtenidos en el paso uno. En nuestro caso usamos la base de datos Chroma. La importancia de una base de datos de vectores es que permite identificar rápidamente cuáles fragmentos de información son semánticamente relevantes a una consulta.

Argumentation Module recibe la base de datos de vectores, en donde aplica 3 pasos, la primera es la inicialización del LLM que en este caso es OpenAI. El segundo paso es la generación del prompt indicando  un contexto adecuado. A partir del primer y segundo paso podemos generar una simple subcadena. Esta subcadena se combina en el 3er paso, el cual consiste en convertir nuestra base de datos de vectores en un recuperador de datos y brindarle el LLM inicializado más el prompt. Con ello ya tenemos una cadena, la cual es un objeto “callable”, un disparador ante una consulta, que recupera y responde a la consulta ingresada.

Generation Module recibe la cadena y la pregunta realizada a través de la API, este módulo simplemente ejecuta la cadena ingresando la consulta. Como salida obtenemos la respuesta aplicando la arquitectura RAG.



## Documentacion detallada
[Documentacion](https://docs.google.com/document/d/1qDoBhpY4VPFuYJjzYic_37mQNcBEmgEoQ-TAl_wqKcE/edit?usp=sharing)

## Construido con :neckbeard:

- [Python 3.12](https://www.python.org/) - Lenguaje de programacion del backend
- [Typescript](https://www.typescriptlang.org/) - Lenguaje de programacion del frontend
- [Fast API](https://fastapi.tiangolo.com/) - Libreria de API
- [Angular 18](https://angular.dev/) - Framework de frotend
- [OpenAI](https://chaton.ai/web_06/?utm_source=google&utm_medium=cpc&utm_campaign=ChatOn%20|%20Web%20|%20LATAM%20|%20Search%20|%20Website%20Mix%20|%20Purch%20No%20Trial%20|%2022.01.2025&utm_content=730205885966&utm_term=openai&campaign_id=22157592439&adset_id=174662267900&ad_id=730205885966&gad_source=1&gclid=Cj0KCQjwhMq-BhCFARIsAGvo0Kdq0ZZZGVftqSQEdgdrYBPwt1uagEfWZNEVSmH3Eh7g226-QhiadjsaAl6MEALw_wcB) - LLM
- [LangChain](https://python.langchain.com/docs/introduction/) - Framework de LLM
- [Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma/) - Base de datos de vectores
- [Docker](https://www.docker.com/) - Virtualizacion y contenedor de aplicaciones
- [Azure] - Plataforma de despligue en la nube

## Despliegue :warning:

API : [Backend](https://my-challenge-app-api.azurewebsites.net/docs#/)
FRONTEND : [Frontend](https://my-challenge-app-promtior.azurewebsites.net/)

## Capturas
![app_deployada_1](https://github.com/user-attachments/assets/e11844f8-fc07-4ce4-a46b-b93e8ffe29dc)
![app_deployada_2](https://github.com/user-attachments/assets/7777039d-1d3c-4eba-9fc3-6688e916b01a)
![app_deployada_3](https://github.com/user-attachments/assets/2f22ffc7-9c24-440b-84a2-ff8bcbdff0b3)
![app_deployada_4](https://github.com/user-attachments/assets/e14e3877-cf5b-4f32-b648-744df0222da4)
![app_deployada_5](https://github.com/user-attachments/assets/41f54145-e07f-4366-895a-3a448204148e)
![app_deployada_6](https://github.com/user-attachments/assets/2c814682-f63b-409b-97ef-88862fa39fe7)

## Autores :star_struck:

- Fernández Ian - *Desarrollador Backend, Frontend, Documentación* - :alien:[ianklebold](https://www.linkedin.com/in/ian-fern%C3%A1ndez-a72598179/)

## Conclusiones y dificultades
Este challenge ha sido una experiencia increíblemente enriquecedora y desafiante. La mayor complicación se presentó al seleccionar el LLM adecuado para la solución. Inicialmente se consideró utilizar Llama, pero rápidamente se evidenciaron ciertas limitaciones y problemas en su desempeño y manejo del contexto, lo que dificultó su aplicación en un entorno de producción robusto.

Frente a estos obstáculos, se optó por cambiar a un modelo de mayor confiabilidad y escalabilidad, integrándose en una arquitectura de Retrieval Augmented Generation (RAG APP). La solución final combina la capacidad generativa del LLM con una base de datos de vectores (Croma) para recuperar información relevante, lo que permite generar respuestas precisas y fundamentadas.

Este enfoque híbrido no solo superó los inconvenientes iniciales, sino que también demostró la potencia de combinar técnicas de recuperación y generación para aplicaciones avanzadas en inteligencia artificial. Sin duda, el challenge me permitió explorar y aprender en profundidad sobre la integración de modelos de lenguaje y sistemas de recuperación, abriendo nuevas oportunidades para el desarrollo de soluciones innovadoras.


## Despedida

Fue un gusto trabajar en este proyecto y compartir mis conocimientos. Con :heart: Por :alien:[ianklebold](https://www.linkedin.com/in/ian-fern%C3%A1ndez-a72598179/) 
