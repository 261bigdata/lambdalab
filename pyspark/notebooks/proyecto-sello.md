?# Proyecto Sello de Big Data

## 1. Propósito

El Proyecto Sello integra las sesiones de **Big Data** alrededor de una solución distribuida end-to-end. El curso parte de una arquitectura de datos y culmina en un sistema que procesa datos batch y streaming, genera salidas analíticas o ML, incorpora observabilidad y demuestra valor para la toma de decisiones.

```text
Arquitectura -> Batch -> Almacenamiento -> Streaming -> Observabilidad -> ML/BI -> Integración -> Sustentación
```

## 2. El Proyecto

Durante el semestre desarrollarás un **sistema Big Data distribuido end-to-end** con procesamiento batch, procesamiento streaming, analítica/ML, observabilidad y visualización o salida para decisiones.

El proyecto debe ejecutarse de forma reproducible en el laboratorio, trabajar con datos representativos, generar evidencias de ejecución y explicar el valor analítico del procesamiento realizado.

No se considera Proyecto Sello:

- Notebooks aislados sin flujo común.
- Transformaciones Spark sin problema analítico.
- Streaming que solo consume mensajes sin generar salida útil.
- Modelos ML sin evaluación ni reutilización.
- Métricas técnicas sin interpretación.
- Una solución que el estudiante no pueda reproducir ni defender.

## 3. Evolución del Proyecto

| Unidad | Temas principales | Evolución del proyecto |
|---|---|---|
| Unidad 1 | Arquitectura Big Data, Spark, ETL batch, HDFS/formats y Parquet. | Pipeline batch distribuido con salidas analíticas preparadas. |
| Unidad 2 | Kafka, Spark Streaming, observabilidad, costos, ML distribuido, series de tiempo e inferencia. | Pipeline en tiempo real con salidas BI/ML y evidencias operacionales. |
| Unidad 3 | Integración, hardening, validación técnica y demo end-to-end. | Sistema Big Data final integrado y sustentado. |

```mermaid
flowchart TB
    A[Problema de datos] --> B[Arquitectura]
    B --> C[ETL batch Spark]
    C --> D[Parquet / datos analíticos]
    D --> E[Kafka]
    E --> F[Spark Streaming]
    F --> G[Observabilidad]
    G --> H[ML / BI]
    H --> I[Validación]
    I --> J[Sustentación]
```

### Alineamiento por sesiones

Este alineamiento muestra cómo el sistema Big Data crece desde procesamiento batch distribuido hasta integración streaming, observabilidad y analítica/ML.

| Sesiones | Contenido central | Avance del proyecto |
|---|---|---|
| S1-S2 | Arquitectura Big Data y fundamentos Spark. | Brief técnico-analítico, entorno reproducible y primeras transformaciones distribuidas. |
| S3-S4 | ETL distribuido, almacenamiento, HDFS/formats y Parquet. | Pipeline batch con datos transformados, validados y almacenados para consumo analítico. |
| S5 | Evaluación U1. | Producto U1: pipeline batch distribuido sustentado. |
| S6-S7 | Ingesta Kafka y procesamiento streaming con Spark. | Flujo de eventos consumido y procesado en tiempo real. |
| S8 | Observabilidad y costos. | Métricas, paneles o evidencias operacionales del pipeline. |
| S9-S11 | ML distribuido, inferencia, series de tiempo y tuning. | Modelo entrenado, evaluado, guardado, reutilizado y mejorado con experimentación. |
| S12 | Evaluación U2. | Producto U2: pipeline streaming con salida BI/ML y evidencias. |
| S13-S15 | Integración, revisión técnica y sustentación final. | Sistema Big Data end-to-end integrado, validado y defendido. |
| S16 | Evaluación final. | Recuperación de competencias pendientes y cierre técnico. |

## 4. Cronograma

| Hito | Momento | Producto esperado |
|---|---|---|
| S2 | Brief técnico-analítico | Problema de datos, fuentes, arquitectura, salidas esperadas y alcance. |
| S5 | Producto U1 | Pipeline batch distribuido con datos transformados, validados y almacenados en formato analítico. |
| S12 | Producto U2 | Pipeline streaming con Kafka/Spark, observabilidad, costos y salida BI/ML o inferencia. |
| S15 | Producto final | Sistema Big Data end-to-end integrado, validado y sustentado con demo reproducible. |
| S16 | Cierre individual | Evaluación final o recuperación de competencias pendientes. |

## 5. Producto Final

Componentes mínimos:

- Problema de datos delimitado.
- Arquitectura técnica del flujo.
- Dataset o fuente de eventos representativa.
- Pipeline batch con Spark.
- Transformaciones y validación básica de calidad.
- Salida analítica en formato eficiente, como Parquet.
- Ingesta o simulación de eventos con Kafka.
- Procesamiento streaming con Spark Structured Streaming.
- Evidencia de observabilidad técnica.
- Métricas de rendimiento, costos o comportamiento operacional.
- Modelo ML, inferencia, salida BI o análisis distribuido según alcance.
- Evidencias reproducibles de ejecución.
- Documentación técnica y demo final.

## 6. Evaluación

| Criterio | Qué se observa |
|---|---|
| Problema y arquitectura | El proyecto responde a una necesidad de datos y define una arquitectura distribuida coherente. |
| Procesamiento batch | El pipeline Spark transforma, valida y almacena datos de forma reproducible. |
| Almacenamiento analítico | Las salidas están organizadas en formatos adecuados para análisis posterior. |
| Streaming | El sistema consume, procesa y produce resultados útiles a partir de eventos. |
| Observabilidad | Existen métricas, logs o paneles que permiten entender el comportamiento del sistema. |
| BI/ML distribuido | El proyecto genera análisis, inferencia, modelo o salida BI con valor para decisiones. |
| Reproducibilidad | El entorno, comandos, notebooks y evidencias permiten volver a ejecutar la solución. |
| Integración | Batch, streaming, observabilidad y analítica forman un flujo común, no piezas aisladas. |
| Evidencias | Se presentan notebooks, salidas, métricas, capturas, artefactos y resultados verificables. |
| Sustentación profesional | El equipo demuestra el sistema, defiende decisiones técnicas y evidencia aporte individual. |

## 7. Sustentación

| Momento | Tiempo sugerido | Propósito |
|---|---:|---|
| Exposición técnica | 10 minutos | Presentar problema, arquitectura, fuentes, pipelines, observabilidad, resultados y valor analítico. |
| Demostración end-to-end | 5 minutos | Ejecutar o evidenciar el flujo batch/streaming, salidas generadas, métricas y resultados BI/ML. |

Cada integrante debe demostrar una parte verificable: arquitectura, Spark batch, Kafka, streaming, observabilidad, ML/BI, validación, documentación o pruebas. La demo debe mostrar ejecución o evidencias reproducibles, no solo explicación conceptual.

Se espera comunicación clara, presentación personal adecuada, puntualidad, vestimenta limpia y actitud profesional.

## 8. Resultado Esperado

Al finalizar el curso, el estudiante debe demostrar que puede construir una solución Big Data distribuida, observable y orientada a decisiones.

```text
Datos -> Procesamiento distribuido -> Streaming -> Observabilidad -> Analítica/ML -> Decisión -> Sustentación
```

