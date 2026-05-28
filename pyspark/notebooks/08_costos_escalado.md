# Costos y escalado de pipelines streaming

## Proposito

Esta seccion completa la sesion de observabilidad con una estimacion cloud-agnostic de recursos, costos y escalado para el pipeline:

```text
Producer -> Kafka -> Spark Structured Streaming
```

La idea no es elegir un proveedor cloud, sino justificar capacidad usando unidades tecnicas: vCPU, memoria, almacenamiento, red, particiones Kafka, ejecutores Spark, retencion y replicas.

## Resultado esperado

Entrega una propuesta tecnica que incluya:

- volumen esperado de eventos;
- throughput promedio y de pico;
- numero inicial de particiones Kafka;
- recursos estimados para Kafka;
- recursos estimados para Spark;
- estrategia de escalado horizontal o vertical;
- impacto de retencion de mensajes y logs;
- riesgos de lag, backpressure o saturacion;
- buenas practicas para optimizar costos;
- comparacion de escenarios pequeno, medio y alto.

## Caso base

Usa como referencia:

```text
Producer de ordenes -> Kafka topic orden-eventos -> Spark Structured Streaming
```

Evento ejemplo:

```json
{
  "ordenId": 101,
  "tipoEvento": "orden.creada",
  "total": 150.0,
  "estado": "PENDIENTE",
  "timestamp": 1710000000000,
  "origen": "ec-orden-ms"
}
```

Supuestos iniciales:

| Supuesto | Valor inicial |
|---|---:|
| Tamano promedio del evento | 1 KB |
| Topic principal | `orden-eventos` |
| Retencion inicial | 7 dias |
| Ambiente dev | 1 broker, replication factor 1 |
| Ambiente productivo propuesto | 3 brokers, replication factor 3 |

## 1. Estimar volumen

Formula:

```text
volumen_diario = cantidad_eventos_dia * tamano_promedio_evento
```

Ejemplos:

| Escenario | Eventos por dia | Tamano evento | Volumen diario |
|---|---:|---:|---:|
| Pequeno | 10 000 | 1 KB | 10 MB/dia |
| Medio | 1 000 000 | 1 KB | 1 GB/dia |
| Alto | 10 000 000 | 1 KB | 10 GB/dia |

## 2. Estimar throughput

Formula:

```text
throughput_promedio = eventos_dia / 86 400
throughput_pico = throughput_promedio * factor_pico
```

Ejemplo:

```text
1 000 000 eventos/dia / 86 400 = 11.57 eventos/s promedio
Si el factor pico es 25, el pico aproximado es 289 eventos/s
```

## 3. Definir particiones Kafka

Mas particiones permiten mas paralelismo, pero tambien aumentan el overhead operativo.

Regla practica para la propuesta:

| Escenario | Particiones sugeridas | Criterio |
|---|---:|---|
| Pequeno | 1 | Bajo volumen y laboratorio |
| Medio | 3 a 6 | Picos moderados y consumidores paralelos |
| Alto | 12 o mas | Alta concurrencia y crecimiento esperado |

La decision debe justificarse con throughput, paralelismo de consumidores y crecimiento esperado.

## 4. Estimar almacenamiento con retencion

Formula:

```text
almacenamiento_base = volumen_diario * dias_retencion
almacenamiento_con_replicas = almacenamiento_base * replication_factor
almacenamiento_recomendado = almacenamiento_con_replicas * 1.3
```

Ejemplo:

```text
volumen diario: 5 GB
retencion: 7 dias
replication factor: 3

almacenamiento_base = 35 GB
almacenamiento_con_replicas = 105 GB
almacenamiento_recomendado = 136.5 GB
```

## 5. Escalar Spark

Si aumenta el lag o la latencia, evalua:

- ajustar el intervalo de trigger;
- aumentar memoria del driver o executor;
- aumentar numero de executors;
- aumentar cores por executor;
- revisar particiones Kafka;
- optimizar transformaciones;
- evitar operaciones costosas por micro-batch;
- persistir resultados solo cuando sea necesario.

Ejemplo operativo:

```text
Si Kafka recibe 500 eventos/s y Spark procesa 200 eventos/s,
el lag crecera y sera necesario escalar el consumer o ajustar el procesamiento.
```

## 6. Indicadores de riesgo

Observa:

| Indicador | Interpretacion |
|---|---|
| `kafka_consumergroup_lag` | Eventos pendientes de consumo |
| `numInputRows` | Eventos procesados por micro-batch |
| `inputRowsPerSecond` | Velocidad de entrada |
| `processedRowsPerSecond` | Velocidad de procesamiento |
| Duracion del batch | Tiempo usado por cada micro-batch |
| `latencyMs` | Diferencia entre creacion y procesamiento del evento |

## 7. Tabla de escenarios

Completa y ajusta esta tabla:

| Escenario | Eventos/dia | Pico eventos/s | Tamano evento | Particiones | Kafka | Spark | Riesgo principal |
|---|---:|---:|---:|---:|---|---|---|
| Pequeno | 10 000 | 20 | 1 KB | 1 | 1 broker dev | local/notebook | bajo |
| Medio | 1 000 000 | 300 | 1 KB | 3-6 | 3 brokers | cluster pequeno | lag en picos |
| Alto | 10 000 000 | 3000 | 1 KB | 12+ | 3+ brokers | cluster escalable | backpressure/costo |

## 8. Buenas practicas

- Iniciar con particiones suficientes para el crecimiento esperado.
- No aumentar particiones sin una razon medible.
- Definir claves de particionado estables.
- Medir lag antes de escalar.
- Ajustar Spark segun la duracion de micro-batches.
- Separar ambientes `dev`, `test` y `prod`.
- Usar retencion acorde al caso de negocio.
- Evitar eventos innecesariamente grandes.
- Monitorear CPU, memoria, disco y red.
- Definir umbrales de alerta antes de operar en produccion.

## Evidencias

Adjunta:

- tabla de supuestos;
- calculo de volumen diario;
- calculo de throughput promedio y pico;
- estimacion de almacenamiento por retencion;
- propuesta de particiones Kafka;
- propuesta de recursos para Kafka y Spark;
- tabla de escenarios pequeno, medio y alto;
- lista de riesgos y mitigaciones;
- conclusion tecnica de escalado.
