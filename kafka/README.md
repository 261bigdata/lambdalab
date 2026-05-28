# Kafka

Cluster Kafka local para los laboratorios de streaming de LambdaLab.

## Servicios

| Servicio | URL/Puerto |
|---|---|
| Kafka broker interno | `kafka:9092` |
| Kafka broker desde host | `localhost:49092` |
| Kafka UI | `http://localhost:48085` |
| Kafka Exporter | `http://localhost:49308/metrics` |

## Uso

Desde esta carpeta:

```powershell
docker compose up -d
```

Red compartida:

```text
lambdalab-kafka-net
```

Los otros módulos del curso, como `pyspark` y `obs`, se conectan a esa red para
consumir eventos y métricas.
