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

Desde la raiz del repositorio, primero elimina los contenedores del stack Kafka
moderno si esta activo:

```powershell
docker compose -f kafka/compose.yml down
```

Luego levanta el stack Debezium:

```powershell
docker compose -f kafka-debezium/compose.yml up -d
```

El comando `down` elimina contenedores y red del compose activo cuando ya no
estan en uso, pero no borra las imagenes Docker.

Para volver al Kafka moderno:

```powershell
docker compose -f kafka-debezium/compose.yml down
docker compose -f kafka/compose.yml up -d
```

## Liberar espacio

Si quieres eliminar las imagenes legacy de Debezium despues de usarlas, primero
baja el stack:

```powershell
docker compose -f kafka-debezium/compose.yml down
```

Opcionalmente, elimina solo las imagenes Debezium:

```powershell
docker image rm debezium/zookeeper:2.7.3.Final
docker image rm debezium/kafka:2.7.3.Final
docker image rm debezium/connect:2.7.3.Final
```

No elimines `provectuslabs/kafka-ui:latest` ni
`danielqsj/kafka-exporter:v1.9.0`, porque tambien se usan en el stack Kafka
moderno.

## Nota

Este stack conserva el alias interno `kafka:9092` y la red
`lambdalab-kafka-net`, de modo que los laboratorios de MS, MQ, Spark y
observabilidad puedan apuntar al mismo nombre de broker.
