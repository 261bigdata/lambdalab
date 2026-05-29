# Costos y escalado de pipelines streaming

## Propósito

Esta sección completa la sesion de observabilidad con una estimación cloud-agnostic de recursos, costos y escalado para el pipeline:

```text
Producer -> Kafka -> Spark Structured Streaming
```

La idea no es elegir un proveedor cloud, sino justificar capacidad usando unidades técnicas: vCPU, memoria, almacenamiento, red, particiones Kafka, ejecutores Spark, retención y réplicas.

## Resultado esperado

Entrega una propuesta técnica que incluya:

- volumen esperado de eventos;
- throughput promedio y de pico;
- número inicial de particiones Kafka;
- recursos estimados para Kafka;
- recursos estimados para Spark;
- estrategia de escalado horizontal o vertical;
- impacto de retención de mensajes y logs;
- riesgos de lag, backpressure o saturacion;
- buenas prácticas para optimizar costos;
- comparacion de escenarios pequeño, medio y alto.

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
| Tamaño promedio del evento | 1 KB |
| Topic principal | `orden-eventos` |
| Retencion inicial | 7 dias |
| Ambiente dev | 1 broker, replication factor 1 |
| Ambiente productivo propuesto | 3 brokers, replication factor 3 |

## 1. Estimar volumen

Formula:

```text
volumen_diario = cantidad_eventos_dia * tamaño_promedio_evento
```

Ejemplos:

| Escenario | Eventos por dia | Tamaño evento | Volumen diario |
|---|---:|---:|---:|
| Pequeño | 10 000 | 1 KB | 10 MB/dia |
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

Más particiones permiten mas paralelismo, pero también aumentan el overhead operativo.

Regla práctica para la propuesta:

| Escenario | Particiones sugeridas | Criterio |
|---|---:|---|
| Pequeño | 1 | Bajo volumen y laboratorio |
| Medio | 3 a 6 | Picos moderados y consumidores paralelos |
| Alto | 12 o mas | Alta concurrencia y crecimiento esperado |

La decisión debe justificarse con throughput, paralelismo de consumidores y crecimiento esperado.

## 4. Estimar almacenamiento con retención

Formula:

```text
almacenamiento_base = volumen_diario * dias_retención
almacenamiento_con_réplicas = almacenamiento_base * replication_factor
almacenamiento_recomendado = almacenamiento_con_réplicas * 1.3
```

Ejemplo:

```text
volumen diario: 5 GB
retención: 7 dias
replication factor: 3

almacenamiento_base = 35 GB
almacenamiento_con_réplicas = 105 GB
almacenamiento_recomendado = 136.5 GB
```

## 5. Escalar Spark

Si aumenta el lag o la latencia, evalúa:

- ajustar el intervalo de trigger;
- aumentar memoria del driver o executor;
- aumentar número de executors;
- aumentar cores por executor;
- revisar particiones Kafka;
- optimizar transformaciones;
- evitar operaciónes costosas por micro-batch;
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

| Escenario | Eventos/dia | Pico eventos/s | Tamaño evento | Particiones | Kafka | Spark | Riesgo principal |
|---|---:|---:|---:|---:|---|---|---|
| Pequeño | 10 000 | 20 | 1 KB | 1 | 1 broker dev | local/notebook | bajo |
| Medio | 1 000 000 | 300 | 1 KB | 3-6 | 3 brokers | cluster pequeño | lag en picos |
| Alto | 10 000 000 | 3000 | 1 KB | 12+ | 3+ brokers | cluster escalable | backpressure/costo |

## 8. Buenas prácticas

- Iniciar con particiones suficientes para el crecimiento esperado.
- No aumentar particiones sin una razón medible.
- Definir claves de particionado estables.
- Medir lag antes de escalar.
- Ajustar Spark según la duración de micro-batches.
- Separar ambientes `dev`, `test` y `prod`.
- Usar retención acorde al caso de negocio.
- Evitar eventos innecesariamente grandes.
- Monitorear CPU, memoria, disco y red.
- Definir umbrales de alerta antes de operar en produccion.

## Evidencias

Adjunta:

- tabla de supuestos;
- calculo de volumen diario;
- calculo de throughput promedio y pico;
- estimación de almacenamiento por retención;
- propuesta de particiones Kafka;
- propuesta de recursos para Kafka y Spark;
- tabla de escenarios pequeño, medio y alto;
- lista de riesgos y mitigaciones;
- conclusión técnica de escalado.
