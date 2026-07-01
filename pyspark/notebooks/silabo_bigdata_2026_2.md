<!-- Version 2026-2 construida desde silabo_bigdata_2026_1.md y propuesta_silabo_2026_2.md -->

Universidad Peruana Union  
Carret. Central km. 19.5 Nana. Telf. 01-6186300 Casilla 3564 Lima 1, Peru

# Silabo: Big Data

## I. Informacion General de Asignatura

| N. | Campo | Informacion | N. | Campo | Informacion |
|---|---|---|---|---|---|
| 01 | Facultad/EGP | Facultad de Ingenieria y Arquitectura | 09 | Ano de plan de estudio | 2022-1 |
| 02 | Programa de estudio | EP Ingenieria de Sistemas | 10 | Ciclo de estudio | 9 |
| 03 | Tipo de estudio | General | 11 | Codigo de asignatura |  |
| 04 | Nombre de asignatura | Big Data | 12 | Numero de creditos | 3 |
| 05 | Duracion |  | 13 | Nota minima probatoria | 13 |
| 06 | Horas de la asignatura | H. Te. Pract: 32 / H. Prc. Pres: 32 | 14 | Ano y semestre academico | 2026-2 |
| 07 | Docente | Sullon Macalupu Abel Angel |  |  |  |
| 08 | Pre requisito | Mineria de datos |  |  |  |

## II. Sumilla

La asignatura de Big Data es de caracter teorico-practico. Desarrolla competencias para implementar soluciones Big Data distribuidas con procesamiento batch, procesamiento streaming, observabilidad, analitica/ML y visualizacion BI. El curso utiliza LambdaLab como entorno integrado de procesamiento distribuido en batch y streaming con Spark y Kafka, permitiendo construir pipelines de datos, gestionar almacenamiento analitico en Parquet, aplicar observabilidad y desarrollar soluciones BI/ML distribuidas mediante laboratorios reproducibles basados en Docker.

## III. Competencia del perfil de egreso en relacion a la asignatura

| Tipo | Competencia | Nivel / dimensiones |
|---|---|---|
| General | **INVESTIGACION E INNOVACION:** Desarrolla y aplica habilidades de investigacion cientifica y formativa, asi como la capacidad de innovar de manera etica y basada en principios biblico-cristianos, para contribuir al avance del conocimiento y la solucion de problemas en la sociedad. | N. 1.1: Problematizacion, Diseno de Investigacion. |
| Especifica | **CIENCIA DE DATOS E INTELIGENCIA ARTIFICIAL:** Disena y gestiona sistemas inteligentes basandose en metodologias, estandares y herramientas a fin de lograr estrategias de mejora para la organizacion. | N. 1.1: Analista de negocios, ingenieria de datos, cientifico de datos, analista de datos. |

## IV. Resultado de aprendizaje de la asignatura

| Resultado de aprendizaje | Producto Academico |
|---|---|
| Implementa, integra y sustenta una solucion Big Data end-to-end que combina pipelines batch distribuidos, ingesta y procesamiento de eventos en tiempo real, analitica/ML a escala, observabilidad tecnica y una capa de visualizacion BI, demostrando valor para la toma de decisiones. | **Nombre:** Sistema Big Data distribuido end-to-end para procesamiento batch y streaming, analitica/ML, observabilidad y visualizacion BI para la toma de decisiones. |
|  | **Descripcion:** Solucion Big Data reproducible que integra Spark, Kafka, almacenamiento analitico, procesamiento streaming, observabilidad con Grafana, analitica/ML distribuida, series de tiempo o inferencia y visualizacion BI. La solucion muestra evidencias de ejecucion, metricas tecnicas y del modelo, documentacion operativa y demo end-to-end. |

## V. Unidades de aprendizaje

## Unidad 1: Arquitecturas Big Data y ETL batch distribuido

| Resultado de aprendizaje | Producto |
|---|---|
| Construye un pipeline batch reproducible con procesamiento distribuido, aplica transformaciones sobre datos a escala, valida la calidad basica de los datos, organiza salidas en formatos analiticos como Parquet y deja un dataset preparado para consumo BI/ML. | **Nombre:** Pipeline batch de ETL distribuido con salidas analiticas en Parquet listas para BI/ML. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Arquitectura Big Data seleccionada y justificada. Uso correcto de Spark/PySpark para extraccion, transformacion, agregacion y procesamiento distribuido. Datos cargados y particionados en formatos analiticos. Pipeline batch reproducible. Primer componente ML distribuido con metricas basicas. Evidencias tecnicas y documentacion de ejecucion. | Pipeline batch que procesa datos distribuidos con Spark, genera salidas analiticas en Parquet y deja resultados preparados para analitica, ML y BI. |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 1 | 10/08/2026 - 15/08/2026 | Arquitectura Big Data. | 2 | 2 | Analiza LambdaLab y define la arquitectura base del sistema Big Data para un caso de negocio. | Elabora un diagrama de arquitectura, decisiones tecnicas, supuestos y riesgos. |
| 2 | 16/08/2026 - 22/08/2026 | Fundamentos PySpark: extraccion, transformaciones, funciones, agrupaciones, agregaciones y RDD. | 2 | 2 | Ejecuta transformaciones distribuidas con PySpark y valida resultados mediante DataFrames/RDD. | Documenta transformaciones, funciones aplicadas y evidencias de ejecucion. |
| 3 | 23/08/2026 - 29/08/2026 | Procesamiento distribuido y carga de datos particionada en HDFS y formatos analiticos. | 2 | 2 | Construye una salida analitica particionada en formato columnar lista para BI/ML. | Justifica formato, particionado, estructura de carpetas y criterios de consulta. |
| 4 | 30/08/2026 - 05/09/2026 | ML distribuido con Spark MLlib (Regresion). | 2 | 2 | Entrena un modelo de regresion distribuida con Spark MLlib y reporta metricas iniciales. | Compara configuraciones basicas y documenta resultados del modelo. |
| 5 | 06/09/2026 - 12/09/2026 | Evaluacion U1. | 2 | 2 | Sustenta el pipeline batch de ETL distribuido con salidas analiticas en Parquet listas para BI/ML. | Corrige observaciones y consolida la documentacion tecnica de U1. |

## Unidad 2: Sistema Big Data en tiempo real: ingesta, streaming, observabilidad y BI/ML

| Resultado de aprendizaje | Producto |
|---|---|
| Implementa un pipeline Big Data en tiempo real que integra ingesta de eventos empresariales e IoT/sensores mediante Kafka, procesamiento distribuido con Spark Structured Streaming, observabilidad con Grafana y estimacion de costos operacionales. Ademas, prepara salidas BI/ML distribuidas y reutiliza modelos para series de tiempo e inferencia batch y/o streaming. | **Nombre:** Pipeline en tiempo real con ingesta de eventos empresariales e IoT/sensores, procesamiento streaming con Spark, observabilidad/costos y salidas BI/ML distribuidas. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Ingesta de eventos empresariales mediante Kafka. Ingesta de eventos IoT/sensores. Procesamiento streaming con Spark Structured Streaming. Observabilidad con metricas y tableros. Estimacion de costos y criterios de escalado. Salidas BI/ML distribuidas. Series de tiempo o inferencia en streaming documentada y validada. | Pipeline Big Data en tiempo real que procesa eventos, produce resultados analiticos, expone metricas operativas y prepara resultados para BI/ML distribuido. |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 6 | 13/09/2026 - 19/09/2026 | Ingesta de eventos empresariales en tiempo real. | 2 | 2 | Publica y consume eventos empresariales con Kafka para un flujo de negocio. | Documenta contrato de evento, topico, particionado y evidencia de publicacion/consumo. |
| 7 | 20/09/2026 - 26/09/2026 | Ingesta de eventos IoT/sensores en tiempo real. | 2 | 2 | Simula eventos de sensores o telemetria y los integra al pipeline de Kafka. | Ajusta esquema de evento, frecuencia, volumen y validaciones de datos. |
| 8 | 27/09/2026 - 03/10/2026 | Procesamiento en streaming con Spark. | 2 | 2 | Implementa procesamiento con Spark Structured Streaming usando ventanas y agregaciones. | Registra efectos de parametros de streaming, latencia y throughput. |
| 9 | 04/10/2026 - 10/10/2026 | Observabilidad con Grafana y costos. | 2 | 2 | Instrumenta el pipeline con metricas, tablero de observabilidad y estimacion de costos. | Define umbrales, riesgos operativos, costos estimados y plan de escalado. |
| 10 | 11/10/2026 - 17/10/2026 | BI/ML distribuido con Spark. | 2 | 2 | Prepara salidas analiticas y/o modelo distribuido para consumo BI/ML. | Documenta datos de salida, metricas, validaciones y uso esperado en BI/ML. |
| 11 | 18/10/2026 - 24/10/2026 | Series de tiempo e inferencia en streaming. | 2 | 2 | Aplica un modelo o inferencia sobre datos batch y/o eventos streaming. | Compara resultados, errores, supuestos y recomendaciones tecnicas. |
| 12 | 25/10/2026 - 31/10/2026 | Evaluacion U2. | 2 | 2 | Sustenta el pipeline en tiempo real con ingesta, streaming, observabilidad, costos y salidas BI/ML. | Corrige observaciones y prepara la integracion final del sistema. |

## Unidad 3: Integracion, DataOps y despliegue del sistema final

| Resultado de aprendizaje | Producto |
|---|---|
| Integra los componentes desarrollados en las unidades anteriores, despliega o empaqueta el sistema mediante practicas de DataOps/DevOps, prepara una demo end-to-end, documenta la operacion del sistema, valida resultados tecnicos y analiticos, y sustenta una solucion final orientada a la toma de decisiones. | **Nombre:** Sistema Big Data distribuido end-to-end para procesamiento batch y streaming, analitica/ML, observabilidad y visualizacion BI para la toma de decisiones. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Integracion end-to-end de batch, streaming y BI/ML. Practicas DataOps/DevOps aplicadas al empaquetado o despliegue. Documentacion operativa completa. Hardening y revision tecnica final. Demo reproducible. Sustentacion tecnica con evidencias de ejecucion, metricas, resultados y valor para la toma de decisiones. | Producto final que integra pipelines batch y streaming, observabilidad, analitica/ML, visualizacion BI y documentacion operativa para una demo end-to-end defendida tecnicamente. |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 13 | 01/11/2026 - 07/11/2026 | Integracion del sistema, DataOps y BI. | 2 | 2 | Integra los componentes batch, streaming, observabilidad y BI/ML en una demo end-to-end. | Documenta flujo completo, dependencias, pasos de ejecucion y evidencias de integracion. |
| 14 | 08/11/2026 - 14/11/2026 | Revision tecnica final y hardening. | 2 | 2 | Realiza revision tecnica, estabiliza configuracion, corrige fallos y mejora documentacion operativa. | Completa checklist de hardening, riesgos, recuperacion y reproducibilidad. |
| 15 | 15/11/2026 - 21/11/2026 | Sustentacion final con demo end-to-end. | 2 | 2 | Sustenta el sistema Big Data distribuido, mostrando procesamiento batch, streaming, observabilidad, BI/ML y valor para la toma de decisiones. | Consolida repositorio, evidencias finales, metricas y respuestas a observaciones. |
| 16 | 22/11/2026 - 28/11/2026 | Evaluacion final de recuperacion para estudiantes que no alcanzaron el nivel esperado o quedaron con calificacion baja. | 2 | 2 | Desarrolla evaluacion final individual y recupera competencias pendientes. | Reflexiona sobre aprendizajes, limitaciones del sistema y mejoras futuras. |

## VI. Estrategias metodologicas

| N. | Estrategias de ensenanza y de aprendizaje que se aplicaran en la asignatura |
|---|---|
| 1.1 | Aprendizaje Cooperativo: Fomenta habilidades colaborativas y de trabajo en equipo, cruciales en la mayoria de los entornos laborales modernos. |
| 1.2 | Flipped Classroom (Clase Invertida): En esta metodologia, los estudiantes revisan el material teorico fuera del aula, generalmente en linea, y utilizan el tiempo en clase para actividades practicas y discusiones. |
| 1.3 | Simulacion: Ofrece experiencias practicas que son esenciales para la aplicacion de teorias en situaciones del mundo real. |
| 1.4 | Estudios de caso: Desarrolla el pensamiento critico y la toma de decisiones al analizar situaciones complejas, preparando a los estudiantes para enfrentar problemas similares en sus futuras carreras profesionales. |
| 1.5 | Proyectos: Fomentan habilidades de investigacion, gestion del tiempo y trabajo en equipo, todas cruciales en el mundo profesional. |

## VII. Evaluacion

La evaluacion de los estudiantes se rige por el Reglamento de Estudios, disponible en: <https://upeu.edu.pe/reglamentos/evaluacion/>.

La estructura evaluativa comprende componentes formativos y/o de procesos, de producto y genericos, reflejando un enfoque integral.

### Componentes de evaluacion y ponderacion

- **Evaluacion de Sesiones (ES):** Es el promedio de las evaluaciones aplicadas a los estudiantes para verificar su proceso de aprendizaje durante las sesiones de las unidades. Su contribucion a la nota final es de hasta el 20%.
- **Evaluacion de Productos (EP):** Es el promedio ponderado de las evaluaciones de los productos entregados en cada unidad. Este componente representa un minimo del 70% de la nota final.
- **Evaluacion de Competencias Generales (ECG):** Esta evaluacion aporta hasta un 10% al calculo de la nota final.

### Programacion de evaluaciones

| Fecha | Unidad | Producto | Evaluacion de proceso y de resultado | Pesos |
|---|---|---|---|---|
| 12/09/2026 | Unidad 1: Arquitecturas Big Data y ETL batch distribuido | Pipeline batch de ETL distribuido con salidas analiticas en Parquet listas para BI/ML. | Evaluacion de sesiones | 5% |
| 12/09/2026 | Unidad 1: Arquitecturas Big Data y ETL batch distribuido | Pipeline batch de ETL distribuido con salidas analiticas en Parquet listas para BI/ML. | Evaluacion del producto | 20% |
| 31/10/2026 | Unidad 2: Sistema Big Data en tiempo real: ingesta, streaming, observabilidad y BI/ML | Pipeline en tiempo real con ingesta de eventos empresariales e IoT/sensores, procesamiento streaming con Spark, observabilidad/costos y salidas BI/ML distribuidas. | Evaluacion de sesiones | 5% |
| 31/10/2026 | Unidad 2: Sistema Big Data en tiempo real: ingesta, streaming, observabilidad y BI/ML | Pipeline en tiempo real con ingesta de eventos empresariales e IoT/sensores, procesamiento streaming con Spark, observabilidad/costos y salidas BI/ML distribuidas. | Evaluacion del producto | 25% |
| 28/11/2026 | Unidad 3: Integracion, DataOps y despliegue del sistema final | Sistema Big Data distribuido end-to-end para procesamiento batch y streaming, analitica/ML, observabilidad y visualizacion BI para la toma de decisiones. | Evaluacion de sesiones | 10% |
| 28/11/2026 | Unidad 3: Integracion, DataOps y despliegue del sistema final | Sistema Big Data distribuido end-to-end para procesamiento batch y streaming, analitica/ML, observabilidad y visualizacion BI para la toma de decisiones. | Evaluacion del producto | 25% |
| 28/11/2026 | Competencia General | INVESTIGACION E INNOVACION: Desarrolla y aplica habilidades de investigacion cientifica y formativa, asi como la capacidad de innovar de manera etica y basada en principios biblico-cristianos, para contribuir al avance del conocimiento y la solucion de problemas en la sociedad. | Competencia General | 10% |

| Componente | Peso |
|---|---|
| Evaluacion de sesiones | 20% |
| Evaluacion del producto | 70% |
| Evaluacion de competencia generica | 10% |
| **Total** | **100%** |

## VIII. Recursos, medios y materiales

| N. | Recursos, medios y materiales |
|---|---|
| 1 | Guias y/o tutoriales |
| 2 | PC de Escritorio con programas de ofimatica |
| 3 | Laboratorios |
| 4 | Internet - Wifi |
| 5 | Proyector y/o TV Smart |

## IX. Referencias

### Basica (Fuentes primarias)

- Brink, H., Richards, J. and Fetherolf, M. (2016). *Real-World Machine Learning*. Manning Publications.
- Erl, T., Khattak, W. and Buhler, P. (2016). *Big Data Fundamentals: Concepts, Drivers & Techniques*. Prentice Hall.
- Cielen, D., Meysman, A. and Ali, M. (2016). *Introducing Data Science*. Manning Publications.

### Complementaria (Fuentes secundarias)

- Garillot, F. and Maas, G. (2017). *Stream Processing with Apache Spark*. O'Reilly.
- Richert, W. and Pedro-Coelho, L. (2013). *Building Machine Learning Systems with Python*. Packt Publishing.
- Grus, J. (2015). *Data Science from Scratch*. O'Reilly Media Inc.
- Poole, D. L. and Mackworth, A. K. (2010). *Artificial Intelligence: Foundations of Computer Agents*. Cambridge University Press.
- Marz, N. and Warren J. (2015). *Big Data: Principles and Best Practices of Scalable Realtime Data Systems*. Manning Publications.
- Ryza, S., Laserson, U., Owen, S., and Wills, J. (2017). *Advanced Analytics with Spark*. 2nd ed. O'Reilly.
- Harrington, P. (2012). *Machine Learning in Action*. Manning.
- Kelleher, J. D., Mac Namee, B. and D'Arcy, A. (2015). *Fundamentals of Machine Learning for Predictive Data Analytics: Algorithms, Worked Examples, and Case Studies*. The MIT Press.
- Gurin, J. (2014). *Open Data Now*. McGraw-Hill.
- Ryza, S., Laserson, U., Owen, S., and Wills, J. (2015). *Advanced Analytics with Spark*. O'Reilly.
- Geron, A. (2017). *Hands-on Machine Learning with Scikit-Learn & TensorFlow*. O'Reilly.
- Kitchin, R. (2014). *The Data Revolution: Big Data, Open Data, Data Infrastructures and Their Consequences*. SAGE Publications.

### Libros

- Pena, S. (2017). *Analisis de datos*. Fundacion universitaria. Bogota.
- Caballero, R., Riesco, E. (2019). *Big Data con Python: recoleccion, almacenamiento y proceso*. Alfaomega Cloud.
- Holmes, D. (2017). *Big Data, una breve introduccion*. Alfaomega Cloud.

### Enlaces de internet

- Corpus de modelos entrenados en espanol: <https://github.com/roquegv/spanishNLPModelCorpus>
- Pandas: <https://pandas.pydata.org/>
- Beautiful Soup: <https://beautiful-soup-4.readthedocs.io/en/latest/>
- Curso Machine Learning: <https://www.aprendemachinelearning.com>
- Data.gov: <https://www.data.gov>
- Documentacion Spark: <https://spark.apache.org/docs/latest/>