<!-- Transcripcion fiel generada desde: bigdata2026-1.docx -->

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
| 06 | Horas de la asignatura | H. Te. Pract: 32 / H. Prc. Pres: 32 | 14 | Ano y semestre academico | 2026-1 |
| 07 | Docente | Sullon Macalupu Abel Angel |  |  |  |
| 08 | Pre requisito | Mineria de datos |  |  |  |

## II. Sumilla

Disena e implementa soluciones Big Data integrando arquitecturas batch y streaming, construyendo pipelines distribuidos con Spark y Kafka, instrumentandolos con observabilidad y buenas practicas operativas, y ejecutando experimentos de analitica/ML a escala para generar resultados reproducibles y orientados a decision.

## III. Competencia del perfil de egreso en relacion a la asignatura

| Tipo | Competencia | Nivel / dimensiones |
|---|---|---|
| General | **INVESTIGACION E INNOVACION:** Desarrolla y aplica habilidades de investigacion cientifica y formativa, asi como la capacidad de innovar de manera etica y basada en principios biblico-cristianos, para contribuir al avance del conocimiento y la solucion de problemas en la sociedad. | N. 1.1: Problematizacion, Diseno de Investigacion. |
| Especifica | **CIENCIA DE DATOS E INTELIGENCIA ARTIFICIAL:** Disena y gestiona sistemas inteligentes basandose en metodologias, estandares y herramientas a fin de lograr estrategias de mejora para la organizacion. | N. 1.1: Analista de negocios, ingenieria de datos, cientifico de datos, analista de datos. |

## IV. Resultado de aprendizaje de la asignatura

| Resultado de aprendizaje | Producto Academico |
|---|---|
| Disena e implementa soluciones Big Data integrando arquitecturas batch y streaming, construyendo pipelines distribuidos con Spark y Kafka, instrumentandolos con observabilidad y buenas practicas operativas, y ejecutando experimentos de analitica/ML a escala para generar resultados reproducibles y orientados a decision. | **Nombre:** Demo de arquitectura integrada (batch + streaming). |
|  | **Descripcion:** Solucion Big Data que integra un pipeline batch (ETL distribuido con Spark) y un pipeline streaming (Kafka + Spark Structured Streaming) con observabilidad (metricas, logging, alertas) y documentacion operativa. Incluye un caso aplicado a regresion o series de tiempo a escala con reporte de metricas y guia de ejecucion/reproduccion. |

## V. Unidades de aprendizaje

## Unidad 1: Arquitecturas Big Data y ETL distribuido

| Resultado de aprendizaje | Producto |
|---|---|
| Analiza arquitecturas Big Data y construye un pipeline batch distribuido con Spark, desde la ingesta hasta la salida verificada, usando almacenamiento y formatos optimizados. | **Nombre:** Pipeline batch en Spark: ingesta -> transformacion -> salida verificada. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Distingue arquitecturas Lambda/Kappa y selecciona enfoque batch/streaming segun el caso. Configura almacenamiento distribuido y elige formatos (Parquet/Avro/ORC) con particionado adecuado. Implementa transformaciones distribuidas en Spark usando DataFrames y evidencia lazy evaluation/planes. Aplica joins y funciones ventana considerando particionado y performance. Verifica la salida con controles de calidad y evidencia de ejecucion reproducible. | Pipeline batch implementado con Spark que ingesta datos, transforma con operaciones distribuidas (joins/ventanas) y publica una salida verificada (controles de calidad, particionado y formato columnar). |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 1 | 15/03/2026 - 21/03/2026 | Arquitecturas Big Data: ecosistema Big Data, arquitecturas Lambda/Kappa, batch vs. streaming, casos reales. | 2 | 2 | Analizar un caso real y decidir arquitectura (Lambda/Kappa) justificando batch vs. streaming y componentes del ecosistema. | Completar una ficha de arquitectura (diagrama, decisiones, supuestos y riesgos) para el caso elegido. |
| 2 | 22/03/2026 - 28/03/2026 | Almacenamiento distribuido: HDFS, formatos Parquet/Avro/ORC, particionado. | 2 | 2 | Disenar layout de almacenamiento (carpetas/particiones) y convertir un dataset a formato columnar con particionado. | Documentar decision de formato y particionado (criterios de consulta, volumen, cardinalidad) con evidencias de lectura/tamano. |
| 3 | 29/03/2026 - 04/04/2026 | Fundamentos de Spark: modelo de ejecucion, DataFrames API, lazy evaluation, planes (logical/physical). | 2 | 2 | Ejecutar transformaciones/acciones en Spark e inspeccionar el plan con explain(), identificando optimizaciones basicas. | Responder guia breve: que se observa en el plan y como impacta en performance (capturas y comentario). |
| 4 | 05/04/2026 - 11/04/2026 | ETL escalable con Spark: transformaciones, joins distribuidos, funciones ventana. | 2 | 2 | Construir un ETL con joins distribuidos y al menos una funcion ventana, incorporando validaciones basicas. | Refinar el ETL: optimizar joins (broadcast/particiones si aplica) y documentar decisiones de performance. |
| 5 | 12/04/2026 - 18/04/2026 | Producto Unidad 1: pipeline batch en Spark, ingesta -> transformacion -> salida verificada. | 2 | 2 | Integrar el pipeline batch completo y presentar evidencia de ejecucion, salida verificada y particionado. | Consolidar entrega final del producto U1 con documentacion (pasos, parametros, supuestos, validaciones). |

## Unidad 2: Streaming, observabilidad y operacion

| Resultado de aprendizaje | Producto |
|---|---|
| Implementa un pipeline streaming con Kafka y Spark Structured Streaming, instrumentandolo con metricas y logs, y aplicando criterios de operacion y costos para escalar de forma cloud-agnostic. | **Nombre:** Pipeline streaming (Kafka + Spark) con metricas de rendimiento. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Configura Kafka (topicos, productores, consumidores) y define patrones de ingesta. Procesa streaming con ventanas y watermarking comprendiendo semantica de entrega. Implementa observabilidad (metricas, logging estructurado) para el pipeline. Define alertas y umbrales operativos para latencia, throughput y errores. Justifica decisiones de escalado y costos con buenas practicas cloud-agnostic. | Pipeline en tiempo real que ingiere eventos con Kafka y procesa con Spark Structured Streaming, incorporando ventanas/watermarking y reportando metricas de latencia/throughput con logging estructurado y alertas basicas. |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 1 | 19/04/2026 - 25/04/2026 | Kafka para ingesta en tiempo real: Apache Kafka, topicos, productores, consumidores; patrones de ingesta en tiempo real. | 2 | 2 | Crear un topico y ejecutar productor/consumidor; definir esquema de evento y patron de ingesta para el caso. | Documentar contrato de evento (campos, tipos, ejemplos) y estrategia de particionado del topico. |
| 2 | 26/04/2026 - 02/05/2026 | Spark Structured Streaming: micro-batch, ventanas, watermarking, semantica de entrega. | 2 | 2 | Implementar un stream con ventanas y watermarking, y medir comportamiento (latencia y throughput). | Ajustar parametros (trigger, watermark) y registrar efectos en latencia/throughput (tabla). |
| 3 | 03/05/2026 - 09/05/2026 | Observabilidad de pipelines: metricas latencia/throughput, logging estructurado, alertas. | 2 | 2 | Instrumentar el pipeline con metricas (latencia/throughput/errores) y logging estructurado; definir alertas y umbrales. | Proponer un tablero minimo de operacion (que medir, umbrales, frecuencia) y adjuntar evidencias. |
| 4 | 10/05/2026 - 16/05/2026 | Costos y escalado cloud-agnostic: estimacion, elasticidad, buenas practicas. | 2 | 2 | Estimar recursos/costos del pipeline (batch/stream) y proponer estrategia de escalado (CPU/memoria/particiones). | Redactar nota operativa: buenas practicas, riesgos (backpressure) y plan de escalado/optimizacion. |
| 5 | 17/05/2026 - 23/05/2026 | Producto Unidad 2: pipeline streaming (Kafka + Spark) con metricas de rendimiento. | 2 | 2 | Integrar pipeline streaming end-to-end con metricas y evidenciar rendimiento bajo carga controlada. | Consolidar documentacion operativa (metricas, alertas, parametros, pasos de ejecucion). |

## Unidad 3: ML a escala, regresion y series de tiempo distribuidos

| Resultado de aprendizaje | Producto |
|---|---|
| Ejecuta experimentos de ML a escala con Spark MLlib (regresion/clasificacion y/o series de tiempo), ajusta hiperparametros de forma distribuida e integra criterios de calidad y DataOps conectando resultados a BI a escala. | **Nombre:** Experimento MLlib con regresion o serie de tiempo + reporte de metricas. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Construye un pipeline MLlib escalable para regresion o clasificacion. Aplica regularizacion (Ridge/Lasso) y evalua con metricas pertinentes. Implementa enfoque de series de tiempo (descomposicion y modelo) en contexto Big Data. Ejecuta ajuste de hiperparametros distribuido (CrossValidator/ParamGridBuilder) y justifica seleccion. Integra controles de calidad y criterios DataOps, conectando resultados a BI a escala. | Experimento en Spark MLlib aplicando regresion o series de tiempo a escala, con pipeline, ajuste de hiperparametros distribuido, metricas de evaluacion y reporte tecnico con interpretacion y recomendaciones. |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 1 | 24/05/2026 - 30/05/2026 | Regresion distribuida con MLlib: pipeline de ML escalable, regresion distribuida (Ridge/Lasso a escala). | 2 | 2 | Construir pipeline MLlib de regresion y entrenar Ridge/Lasso, reportando metricas y tiempos de ejecucion. | Comparar Ridge vs Lasso (metricas + complejidad) y redactar conclusiones tecnicas breves. |
| 2 | 31/05/2026 - 06/06/2026 | Series de tiempo a escala: series de tiempo en Big Data, descomposicion, ARIMA/Prophet distribuido con Spark. | 2 | 2 | Preparar series (resampling/estacionalidad) y ejecutar un modelo (ARIMA/Prophet) en enfoque distribuido o por particiones. | Documentar supuestos del modelo y comparar al menos dos configuraciones con metricas/errores. |
| 3 | 07/06/2026 - 13/06/2026 | Hiperparametros distribuidos: clasificacion y ajuste de hiperparametros distribuido, CrossValidator, ParamGridBuilder. | 2 | 2 | Implementar CrossValidator con ParamGridBuilder para un modelo (clasificacion o regresion) y seleccionar mejor configuracion. | Completar tabla de experimentos (parametros, metricas, tiempo) y justificar la seleccion final. |
| 4 | 14/06/2026 - 20/06/2026 | DataOps y BI a escala: calidad de datos y analitica BI a escala, DataOps, conexion Power BI/Databricks. | 2 | 2 | Definir controles de calidad y preparar dataset/modelo para consumo BI (Power BI/Databricks). | Redactar mini guia DataOps: validaciones, linaje basico y versionado de artefactos. |
| 5 | 21/06/2026 - 27/06/2026 | Producto Unidad 3: experimento MLlib con regresion o serie de tiempo + reporte de metricas. | 2 | 2 | Integrar experimento (pipeline + tuning + metricas) y presentar reporte con interpretacion y recomendaciones. | Consolidar reporte final y evidencias (configuracion, metricas, reproducibilidad minima). |

## Unidad 4: Proyecto perfil de egreso

| Resultado de aprendizaje | Producto |
|---|---|
| Presenta proyecto de perfil de egreso. | **Nombre:** Proyecto de perfil de egreso. |

| Criterios de evaluacion del producto | Descripcion del producto |
|---|---|
| Evalua si el producto incorpora buenas practicas y estandares reconocidos en la gestion de servicios TI, como ITIL, COBIT o ISO 27001. Evidencia la aplicacion de conocimientos teoricos en un contexto practico y real. Analiza la claridad, precision y fundamentacion tecnica en la documentacion del plan de operacion, soporte y evaluacion de servicios TI. Evalua si el producto integra un diagnostico efectivo de la gestion de incidentes, infraestructura tecnologica y desempeno de los servicios. | Un informe tecnico del Plan Integral incluye procedimientos de gestion operativa de servicios, estrategias de resolucion de incidentes, administracion de problemas y gestion de cambios; administracion de infraestructura tecnologica; monitoreo y auditoria de desempeno; propuesta de mejora continua basada en auditorias y analisis de desempeno. |

### Sesiones de aprendizaje

| N. | Fecha | Contenido | HT | HP | Actividad practica | Actividad autonoma |
|---|---|---|---|---|---|---|
| 1 | 28/06/2026 - 04/07/2026 | Producto de Curso: demo de arquitectura integrada (batch + streaming) + documentacion operativa de pipeline aplicado a la regresion o series de tiempo. Presentacion final de proyectos, sustentacion de proyecto de perfil de egreso. | 2 | 2 | Realizar demo end-to-end mostrando batch + streaming, observabilidad y el caso ML (regresion o series) con metricas y evidencia de operacion. Presentacion del producto y evaluacion con rubricas de aprendizaje. | Preparar sustentacion final y documentacion operativa completa (pasos, parametros, metricas, alertas, guia de reproduccion). Organizar los entregables del producto y subirlo en la tarea de la unidad. |

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
| 14/04/2026 | Unidad 1: Arquitecturas Big Data y ETL distribuido | Pipeline batch en Spark: ingesta -> transformacion -> salida verificada. | Evaluacion del producto | 20% |
| 14/04/2026 | Unidad 1: Arquitecturas Big Data y ETL distribuido | Pipeline batch en Spark: ingesta -> transformacion -> salida verificada. | Evaluacion de sesiones | 5% |
| 19/05/2026 | Unidad 2: Streaming, observabilidad y operacion | Pipeline streaming (Kafka + Spark) con metricas de rendimiento. | Evaluacion de sesiones | 5% |
| 19/05/2026 | Unidad 2: Streaming, observabilidad y operacion | Pipeline streaming (Kafka + Spark) con metricas de rendimiento. | Evaluacion del producto | 20% |
| 23/06/2026 | Unidad 3: ML a escala, regresion y series de tiempo distribuidos | Experimento MLlib con regresion o serie de tiempo + reporte de metricas. | Evaluacion de sesiones | 5% |
| 23/06/2026 | Unidad 3: ML a escala, regresion y series de tiempo distribuidos | Experimento MLlib con regresion o serie de tiempo + reporte de metricas. | Evaluacion del producto | 20% |
| 30/06/2026 | Unidad 4: Proyecto perfil de egreso | Proyecto de perfil de egreso. | Evaluacion de sesiones | 5% |
| 30/06/2026 | Unidad 4: Proyecto perfil de egreso | Proyecto de perfil de egreso. | Evaluacion del producto | 10% |
| 30/06/2026 | Competencia General | INVESTIGACION E INNOVACION: Desarrolla y aplica habilidades de investigacion cientifica y formativa, asi como la capacidad de innovar de manera etica y basada en principios biblico-cristianos, para contribuir al avance del conocimiento y la solucion de problemas en la sociedad. | Competencia General | 10% |

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