# Plantilla entregable U2

## Unidad 2: Sistema Big Data en tiempo real

**Producto de la unidad:** pipeline streaming con múltiples patrones de ingesta
y Spark, observabilidad, estimación de recursos/costos y modelo
predictivo de analítica/ML entrenado y evaluado.

---

## Datos generales

**Curso:** Big Data  
**Unidad:** 2  
**Estudiante / equipo:** ______________________________  
**Fecha:** ____ / ____ / ______  
**Docente:** ______________________________  

---

## Entregable esperado

El estudiante/equipo debe presentar un pipeline streaming funcional basado en un
sistema de mensajería/event streaming y procesamiento con Spark, acompañado de
evidencias técnicas, métricas operativas, propuesta de observabilidad/costos y
un modelo predictivo entrenado, evaluado y seleccionado mediante experimentación
distribuida para integrarse en la U3.

---

## Sesiones de la Unidad 2

| Sesión | Tema | Actividad práctica | Evidencia esperada |
|---|---|---|---|
| S6 | Ingesta en tiempo real (Kafka) | Publicar eventos de negocio desde microservicios o cambios CDC desde una base OLTP. | Topics, producer/consumer, contrato de evento y evidencias del caso elegido. |
| S7 | Procesamiento en Streaming con Spark | Consumir eventos desde el broker con Spark, parsear JSON, validar esquema y transformar datos. | Notebook/script de streaming, checkpoint, salidas y validaciones. |
| S8 | Observabilidad (Grafana) y Costos | Medir latencia, throughput, lag, errores; proponer dashboard, alertas y recursos. | Métricas, logs, dashboard, alertas y estimación de costos/escalado. |
| S9 | ML distribuido: regresión con MLlib | Entrenar, evaluar y guardar un modelo distribuido. | Modelo entrenado, métricas y artefacto guardado. |
| S10 | Series de tiempo e inferencia en streaming | Aplicar el modelo guardado sobre datos batch y/o Kafka streaming. | Predicciones, métricas y evidencia de inferencia. |
| S11 | Tuning y experimentación distribuida | Comparar configuraciones y seleccionar el mejor modelo con validación distribuida. | Mejor modelo seleccionado y tabla de experimentación. |

---

## Estructura sugerida del informe

### 1. Resumen ejecutivo

Describe el objetivo del pipeline streaming, el caso elegido y el resultado
obtenido.

### 2. Arquitectura del pipeline

Incluye:

- fuente de datos: MS o réplica CDC;
- sistema de mensajería/event streaming como capa de ingesta;
- Spark como motor de procesamiento;
- almacenamiento/salidas analíticas;
- capa BI/ML;
- observabilidad y supuestos de ejecución.

### 3. Ingesta de eventos en tiempo real

Documenta:

- caso elegido en S6: MS o réplica CDC;
- caso sensores en S7;
- topics, colas o canales utilizados;
- productores y consumidores;
- estrategia de particionado;
- ejemplos de eventos.

#### Contrato de evento

| Campo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### 4. Procesamiento en streaming con Spark

Documenta:

- lectura desde el broker/event stream;
- parseo JSON;
- validación de esquema;
- filtros y transformaciones;
- ventanas o watermarking si aplica;
- checkpoint;
- salida del stream.

### 5. Observabilidad y rendimiento

Registra resultados de pruebas controladas.

| Prueba | Fuente | Trigger | Throughput | Latencia | Lag/errores | Observaciones |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

### 6. Costos y escalado

Estima:

- CPU;
- memoria;
- particiones, colas o canales del broker;
- ejecutores Spark;
- volumen de datos esperado;
- almacenamiento;
- riesgos de backpressure;
- estrategia de escalado.

### 7. BI/ML distribuido con Spark

Documenta:

- dataset analítico generado;
- features construidas;
- tablas Gold/Mart si aplica;
- salidas en Parquet;
- uso previsto para BI o ML.

### 8. Modelo predictivo e inferencia

Incluye:

- objetivo del modelo;
- variables/features;
- algoritmo usado;
- métricas de evaluación;
- predicciones generadas;
- evidencia de inferencia batch o streaming;
- artefactos/modelo listos para integrarse en U3.

### 9. Evidencias

Adjunta o referencia:

- capturas de ejecución;
- logs;
- salidas de consola;
- fragmentos de código;
- notebooks/scripts usados;
- métricas del pipeline;
- métricas del modelo;
- archivos Parquet o artefactos generados.

### 10. Conclusiones

Resume:

- qué se logró implementar;
- qué limitaciones se encontraron;
- qué decisiones técnicas se tomaron;
- cómo se integrará el resultado en U3 mediante DataOps/DevOps.

---

## Checklist de entrega

| Criterio | Cumple | Observaciones |
|---|---|---|
| Se implementó ingesta de eventos para caso MS o réplica CDC. | [ ] | |
| Se documentaron contratos de evento. | [ ] | |
| Se implementó procesamiento streaming con Spark. | [ ] | |
| Se midió latencia, throughput, lag o errores. | [ ] | |
| Se propuso observabilidad con dashboard, métricas y alertas. | [ ] | |
| Se estimaron recursos, costos y escalado. | [ ] | |
| Se generó dataset BI/ML o tablas mart en Parquet. | [ ] | |
| Se entrenó y evaluó un modelo predictivo. | [ ] | |
| Se evidenció inferencia batch o streaming. | [ ] | |
| Se adjuntaron evidencias técnicas reproducibles. | [ ] | |

---

## Producto final de Unidad 2

Pipeline streaming con Kafka y Spark,
observabilidad operativa, salidas BI/ML y modelo predictivo listo para integrarse
y desplegarse en la U3.
