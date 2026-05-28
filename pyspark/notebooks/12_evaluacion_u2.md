# Evaluacion U2

## Unidad 2: Sistema Big Data en tiempo real

**Producto de la unidad:** pipeline streaming en Spark para BI/ML a escala y en tiempo real.

**Alcance:** la Unidad 2 evalua las sesiones 6, 7 y 8:

- Sesion 6: Kafka para ingesta en tiempo real.
- Sesion 7: Spark Structured Streaming.
- Sesion 8: observabilidad, costos y escalado.

Las sesiones 9, 10 y 11 quedan como continuidad para la siguiente unidad de ML distribuido y experimentacion.

## Datos generales

| Campo | Valor |
|---|---|
| Curso | Big Data |
| Unidad | 2 |
| Estudiante o equipo | |
| Fecha | |
| Docente | |

## Entregable esperado

El estudiante o equipo debe presentar un pipeline streaming funcional basado en Kafka y Spark Structured Streaming, acompanado de evidencias tecnicas, metricas operativas y una propuesta basica de observabilidad, costos y escalado.

## Sesiones evaluadas

| Sesion | Tema | Actividad practica | Actividad autonoma | Evidencia esperada |
|---|---|---|---|---|
| S6 | Kafka para ingesta en tiempo real | Crear un topic y ejecutar producer/consumer. Definir el esquema de evento y el patron de ingesta. | Documentar el contrato de evento, ejemplos y estrategia de particionado. | Capturas o logs del topic, producer, consumer y mensaje de ejemplo. |
| S7 | Spark Structured Streaming | Implementar un stream con lectura desde Kafka, validacion de JSON, ventanas o filtros y checkpoint. | Ajustar trigger, watermark o volumen de mensajes y registrar efectos. | Notebook, script o evidencia del stream con resultados medidos. |
| S8 | Observabilidad, costos y escalado | Instrumentar el pipeline con metricas de latencia, throughput, errores y lag. | Proponer dashboard, alertas, recursos, costos y estrategia de escalado. | Metricas, logs, dashboard, alertas, estimacion de costos y plan operativo. |

## Estructura sugerida del informe

### 1. Resumen ejecutivo

Describe el objetivo del pipeline, el problema abordado y el resultado obtenido.

### 2. Arquitectura del pipeline

Incluye:

- fuente de datos;
- Kafka como sistema de ingesta;
- Spark Structured Streaming como motor de procesamiento;
- salida del pipeline para BI, monitoreo o almacenamiento;
- supuestos tecnicos de ejecucion.

### 3. Ingesta en tiempo real con Kafka

Documenta:

- nombre del topic;
- numero de particiones;
- estrategia de particionado;
- producer utilizado;
- consumer utilizado;
- ejemplo de evento generado.

#### Contrato de evento

| Campo | Tipo de dato | Descripcion | Ejemplo |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### 4. Procesamiento en streaming con Spark

Documenta:

- fuente de lectura desde Kafka;
- transformaciones aplicadas;
- uso de ventanas;
- uso de watermarking;
- configuracion de trigger;
- salida del stream.

#### Parametros utilizados

| Parametro | Valor | Justificacion |
|---|---|---|
| Trigger | | |
| Watermark | | |
| Ventana | | |
| Output mode | | |
| Checkpoint | | |

### 5. Metricas de rendimiento

Registra resultados de pruebas controladas.

| Prueba | Trigger | Watermark | Throughput | Latencia | Observaciones |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### 6. Observabilidad del pipeline

Incluye:

- metricas clave;
- logs generados;
- errores identificados;
- umbrales de alerta;
- propuesta de dashboard minimo.

#### Dashboard minimo propuesto

| Metrica | Descripcion | Umbral sugerido | Frecuencia de revision |
|---|---|---|---|
| Latencia | | | |
| Throughput | | | |
| Errores | | | |
| Backpressure o lag | | | |

### 7. Costos y escalado

Estima los recursos necesarios para operar el pipeline:

- CPU;
- memoria;
- particiones Kafka;
- ejecutores Spark;
- volumen de datos esperado;
- retencion de mensajes;
- riesgos de backpressure;
- estrategia de escalado.

#### Estimacion de recursos

| Recurso | Estimacion | Justificacion |
|---|---|---|
| CPU | | |
| Memoria | | |
| Particiones Kafka | | |
| Ejecutores Spark | | |
| Almacenamiento | | |

### 8. Evidencias

Adjunta o referencia:

- capturas de ejecucion;
- logs;
- salidas de consola;
- fragmentos de codigo;
- resultados de pruebas;
- tablas de metricas;
- enlaces a notebooks o scripts usados.

### 9. Conclusiones

Resume:

- que se logro implementar;
- que limitaciones se encontraron;
- que mejoras se proponen;
- como se prepararia el pipeline para una siguiente etapa con ML distribuido.

## Checklist de entrega

| Criterio | Cumple | Observaciones |
|---|---|---|
| Se creo y probo un topic Kafka. | [ ] | |
| Se ejecuto producer y consumer. | [ ] | |
| Se documento el contrato de evento. | [ ] | |
| Se implemento un pipeline con Spark Structured Streaming. | [ ] | |
| Se usaron ventanas, filtros o watermarking. | [ ] | |
| Se midio latencia y throughput. | [ ] | |
| Se propuso una estrategia de observabilidad. | [ ] | |
| Se definieron metricas, alertas y umbrales. | [ ] | |
| Se estimaron costos o recursos de operacion. | [ ] | |
| Se propuso una estrategia de escalado. | [ ] | |
| Se adjuntaron evidencias tecnicas. | [ ] | |

## Producto final

Pipeline streaming Kafka + Spark con metricas de rendimiento, documentacion operativa, propuesta de observabilidad y estimacion basica de costos y escalado.
