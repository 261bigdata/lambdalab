# Guia de sesion: Spark Structured Streaming

## Proposito

Consumir eventos Kafka con Spark Structured Streaming, parsear mensajes JSON, validar el contrato del evento y aplicar transformaciones basicas en tiempo real.

Esta guia complementa el notebook de la sesion. El notebook contiene la ejecucion paso a paso; esta seccion resume el objetivo pedagogico, las evidencias y la actividad autonoma.

## Requisitos previos

Antes de empezar:

- levantar Kafka desde `kafka/`;
- verificar que exista el topic `orden-eventos`;
- generar eventos desde `uso-rapido/ec-orden-py` o `uso-ms-sb/ec-orden-ms`;
- levantar Spark/Jupyter con el override de Kafka.

```powershell
docker compose -f pyspark/compose.yml -f pyspark/compose.kafka.yml up --build
```

## Evento esperado

```json
{
  "tipoEvento": "orden.creada",
  "ordenId": 1,
  "total": 150.0,
  "estado": "PENDIENTE",
  "origen": "ec-orden-ms",
  "timestamp": 1710000000000
}
```

Campos minimos:

- `tipoEvento`
- `ordenId`
- `total`
- `estado`

Campos recomendados:

- `origen`
- `timestamp`

## Practica

En el notebook:

1. Crea una `SparkSession` con el conector Kafka.
2. Lee desde `orden-eventos` usando `.format("kafka")`.
3. Convierte `value` de binario a texto.
4. Parsea el JSON con un esquema explicito.
5. Filtra eventos invalidos.
6. Aplica una transformacion simple, por ejemplo `total > 100`.
7. Configura salida a consola y checkpoint.
8. Observa latencia, volumen y comportamiento del micro-batch.

## Que observar

Registra:

- si Spark recibe eventos en tiempo real;
- si el parseo JSON funciona;
- si el esquema coincide con el contrato;
- cuantos eventos pasan el filtro;
- diferencias entre eventos emitidos por Python y por Spring Boot;
- efecto de cambiar trigger, volumen o frecuencia de generacion.

## Evidencias

Adjunta:

- captura del notebook leyendo desde Kafka;
- captura del esquema parseado;
- salida de eventos validos;
- evidencia del filtro aplicado;
- tabla breve con observaciones de latencia y throughput.

## Actividad autonoma

Ajusta parametros y registra su efecto:

| Prueba | Trigger | Eventos generados | Latencia observada | Eventos procesados | Observaciones |
|---|---|---:|---:|---:|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
