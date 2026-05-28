# Kafka Debezium

Stack Kafka alternativo para practicas CDC con Debezium.

Usa los mismos puertos y la misma red que `kafka/` para funcionar como reemplazo
directo del Kafka moderno del laboratorio principal.

Ambos stacks podrian correr en paralelo si se cambian puertos, nombres internos,
alias y red Docker. Para el curso se recomienda no hacerlo: por equipos
limitados y por claridad operativa, ejecuta `kafka/` o `kafka-debezium/`, pero
no ambos a la vez.

La eleccion no depende tanto del caso de uso, porque `kafka-debezium/` tambien
sirve para MS, MQ, Big Data, Spark y observabilidad/Telemetria IoT. La decision
principal es de recursos y necesidad de Debezium:

- usa `kafka/` si no trabajaras CDC/Debezium;
- usa `kafka-debezium/` si trabajaras CDC/Debezium;
- evita cargar ZooKeeper, Kafka Connect y las imagenes pesadas de Debezium si no
  hacen falta para la sesion.

## Servicios

| Servicio | URL o puerto |
|---|---|
| Kafka broker desde host | `localhost:49092` |
| Kafka interno Docker | `kafka:9092` |
| Kafka UI | `http://localhost:48085` |
| Kafka Exporter | `http://localhost:49308/metrics` |
| Kafka Connect | `http://localhost:48083` |
| ZooKeeper | `localhost:42181` |

## Uso

Primero deten el stack Kafka moderno si esta activo:

```powershell
docker compose -f kafka/compose.yml down
```

Luego levanta el stack Debezium desde la raiz del repositorio:

```powershell
docker compose -f kafka-debezium/compose.yml up -d
```

Para volver al Kafka moderno:

```powershell
docker compose -f kafka-debezium/compose.yml down
docker compose -f kafka/compose.yml up -d
```

## Nota

Este stack conserva el alias interno `kafka:9092` y la red
`lambdalab-kafka-net`, de modo que los laboratorios de MS, MQ, Spark y
observabilidad puedan apuntar al mismo nombre de broker.
