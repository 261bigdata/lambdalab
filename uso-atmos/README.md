# uso-atmos

Caso de uso atmosferico reservado para sensores, ESP32 y datos meteorologicos.

La idea del curso es usar este dominio para conectar la arquitectura Lambda:

- U1: Spark batch lee historico y genera datasets en `pyspark/artifacts/`.
- U2: Kafka recibe eventos y Spark procesa streaming.
- OBS: Prometheus y Grafana visualizan metricas operativas.
