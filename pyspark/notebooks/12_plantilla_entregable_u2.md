# Plantilla entregable U2

## Unidad 2: Sistema Big Data en tiempo real

**Producto de la unidad:** pipeline streaming con multiples patrones de ingesta
y Spark, observabilidad, estimacion de recursos/costos y modelo
predictivo de analitica/ML entrenado y evaluado.

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
sistema de mensajeria/event streaming y procesamiento con Spark, acompanado de
evidencias tecnicas, metricas operativas, propuesta de observabilidad/costos y
un modelo predictivo entrenado y evaluado para integrarse en la U3.

---

## Sesiones de la Unidad 2

| Sesion | Tema | Actividad practica | Evidencia esperada |
|---|---|---|---|
| S6 | Ingesta de eventos empresariales en tiempo real | Publicar eventos de negocio desde microservicios o cambios CDC desde una base OLTP. | Topics, producer/consumer, contrato de evento y evidencias del caso elegido. |
| S7 | Ingesta de eventos IoT/sensores en tiempo real | Publicar eventos de sensores desde simulador, Wokwi o bridge MQTT/HTTP. | Topic de sensores, mensajes publicados, consumer y contrato del evento sensor. |
| S8 | Procesamiento streaming con Spark | Consumir eventos desde el broker con Spark, parsear JSON, validar esquema y transformar datos. | Notebook/script de streaming, checkpoint, salidas y validaciones. |
| S9 | Observabilidad, costos y escalado | Medir latencia, throughput, lag, errores; proponer dashboard, alertas y recursos. | Metricas, logs, dashboard, alertas y estimacion de costos/escalado. |
| S10 | BI/ML distribuido con Spark | Construir datasets analiticos, features, tablas mart o dataset de entrenamiento. | Salidas BI/ML en Parquet, features y/o tablas Gold/Mart. |
| S11 | Series de tiempo e inferencia en streaming | Entrenar/evaluar modelo predictivo e implementar evidencia de inferencia batch o streaming. | Modelo, metricas, predicciones y evidencia de inferencia. |

---

## Estructura sugerida del informe

### 1. Resumen ejecutivo

Describe el objetivo del pipeline streaming, el caso elegido y el resultado
obtenido.

### 2. Arquitectura del pipeline

Incluye:

- fuente de datos: MS, replica-cdc o sensores;
- sistema de mensajeria/event streaming como capa de ingesta;
- Spark como motor de procesamiento;
- almacenamiento/salidas analiticas;
- capa BI/ML;
- observabilidad y supuestos de ejecucion.

### 3. Ingesta de eventos en tiempo real

Documenta:

- caso elegido en S6: MS o replica-cdc;
- caso sensores en S7;
- topics, colas o canales utilizados;
- productores y consumidores;
- estrategia de particionado;
- ejemplos de eventos.

#### Contrato de evento

| Campo | Tipo de dato | Descripcion | Ejemplo |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### 4. Procesamiento en streaming con Spark

Documenta:

- lectura desde el broker/event stream;
- parseo JSON;
- validacion de esquema;
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

- dataset analitico generado;
- features construidas;
- tablas Gold/Mart si aplica;
- salidas en Parquet;
- uso previsto para BI o ML.

### 8. Modelo predictivo e inferencia

Incluye:

- objetivo del modelo;
- variables/features;
- algoritmo usado;
- metricas de evaluacion;
- predicciones generadas;
- evidencia de inferencia batch o streaming;
- artefactos/modelo listos para integrarse en U3.

### 9. Evidencias

Adjunta o referencia:

- capturas de ejecucion;
- logs;
- salidas de consola;
- fragmentos de codigo;
- notebooks/scripts usados;
- metricas del pipeline;
- metricas del modelo;
- archivos Parquet o artefactos generados.

### 10. Conclusiones

Resume:

- que se logro implementar;
- que limitaciones se encontraron;
- que decisiones tecnicas se tomaron;
- como se integrara el resultado en U3 mediante DataOps/DevOps.

---

## Checklist de entrega

| Criterio | Cumple | Observaciones |
|---|---|---|
| Se implemento ingesta de eventos para caso MS o replica-cdc. | [ ] | |
| Se implemento o documento ingesta de eventos para sensores. | [ ] | |
| Se documentaron contratos de evento. | [ ] | |
| Se implemento procesamiento streaming con Spark. | [ ] | |
| Se midio latencia, throughput, lag o errores. | [ ] | |
| Se propuso observabilidad con dashboard, metricas y alertas. | [ ] | |
| Se estimaron recursos, costos y escalado. | [ ] | |
| Se genero dataset BI/ML o tablas mart en Parquet. | [ ] | |
| Se entreno y evaluo un modelo predictivo. | [ ] | |
| Se evidencio inferencia batch o streaming. | [ ] | |
| Se adjuntaron evidencias tecnicas reproducibles. | [ ] | |

---

## Producto final de Unidad 2

Pipeline streaming con multiples fuentes de ingesta y Spark,
observabilidad operativa, salidas BI/ML y modelo predictivo listo para integrarse
y desplegarse en la U3.
