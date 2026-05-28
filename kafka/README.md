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

Desde la raiz del repositorio:

```powershell
docker compose -f kafka/compose.yml up -d
```

Red compartida:

```text
lambdalab-kafka-net
```

Los otros modulos del curso, como `pyspark` y `obs`, se conectan a esa red para
consumir eventos y metricas.

## Cambiar a Kafka Debezium

Si necesitas trabajar CDC/Debezium, reemplaza este stack por
`kafka-debezium/`. El comando `down` elimina los contenedores del stack Kafka
moderno, pero no borra las imagenes Docker.

Desde la raiz del repositorio:

```powershell
docker compose -f kafka/compose.yml down
docker compose -f kafka-debezium/compose.yml up -d
```
