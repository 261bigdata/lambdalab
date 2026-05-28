# Uso Replica CDC

Caso de uso reservado para una practica posterior de migracion y analitica con
CDC desde MySQL hacia PostgreSQL RAW usando Debezium y Kafka.

## Escenario

El escenario simula la modernizacion de una aplicacion monolitica legacy que
usa MySQL como base transaccional principal y necesita migrar gradualmente hacia
PostgreSQL sin detener la operacion.

La idea es elevar el caso mas alla de una replica tecnica: el estudiante debe
entender CDC como una estrategia de transicion operativa y como fuente para
pipelines de BI/ML.

## Flujo base

El punto comun del caso es mantener una copia RAW de los cambios del monolito:

```text
MySQL OLTP legacy -> Debezium -> Kafka -> PostgreSQL RAW
```

Desde esa capa RAW se trabajan dos caminos complementarios.

## Camino 1: migracion de base de datos sin parar el monolito

Este camino usa CDC como estrategia de migracion progresiva.

El monolito sigue funcionando sobre MySQL mientras el equipo prepara PostgreSQL
como base destino. Durante ese periodo, Debezium mantiene sincronizados los
cambios nuevos para que la base destino no quede desactualizada.

Flujo conceptual:

```text
MySQL OLTP legacy
  -> Debezium
  -> Kafka
  -> PostgreSQL RAW
  -> ajustes de modelo, validacion y preparacion de la nueva base
  -> cutover hacia la nueva aplicacion
```

La migracion se ejecuta en fases:

- carga historica inicial desde MySQL hacia PostgreSQL;
- captura continua de cambios nuevos con CDC;
- validacion de consistencia entre origen y destino;
- cambios de esquema, indices, constraints y ajustes necesarios en PostgreSQL;
- ventana corta de cutover, por ejemplo de noche a la manana;
- cambio de la aplicacion para usar PostgreSQL sin que los usuarios perciban la transicion.

Objetivo: reducir downtime y permitir que el equipo avance con la base destino
sin congelar el monolito durante todo el proyecto.

## Camino 2: ETL para BI/ML con Spark

Este camino usa la misma captura CDC como fuente para construir productos
analiticos.

En vez de usar dbt sobre PostgreSQL como en un flujo BI tradicional, el curso de
Big Data trabaja el ETL con Spark y persiste resultados en archivos analiticos.

Flujo conceptual:

```text
MySQL OLTP legacy
  -> Debezium
  -> Kafka
  -> PostgreSQL RAW
  -> Spark ETL
  -> Bronze / Silver / Gold
  -> marts en Parquet
  -> Power BI / ML
```

Capas sugeridas:

| Capa | Rol |
|---|---|
| PostgreSQL RAW | Replica tecnica de eventos/tablas provenientes del monolito |
| Bronze | Datos crudos o casi crudos extraidos desde RAW |
| Silver | Datos limpiados, tipados, deduplicados y conformados |
| Gold | Tablas de negocio listas para BI/ML |
| Marts Parquet | Salidas analiticas consumibles por Power BI o modelos ML |

Objetivo: mostrar como una arquitectura CDC tambien puede alimentar analitica
moderna sin depender de un DW relacional tradicional ni de dbt.

## Fases de migracion operativa

### Fase 1: carga historica

Realizar una carga inicial de datos desde MySQL hacia PostgreSQL RAW.

Alternativas:

- exportacion masiva desde MySQL y carga en PostgreSQL;
- proceso ETL controlado;
- bulk load inicial antes de activar CDC.

### Fase 2: captura de cambios nuevos

Usar Debezium para leer el log transaccional de MySQL y publicar cambios en
Kafka.

Luego, replicar esos eventos hacia PostgreSQL RAW con un sink.

### Fase 3: cutover

Planificar el cambio operativo:

- detener escrituras en MySQL;
- validar consistencia entre MySQL y PostgreSQL;
- cambiar la aplicacion para escribir en PostgreSQL;
- dejar MySQL como respaldo temporal si corresponde.

## Objetivos de aprendizaje

- comprender CDC como Change Data Capture real;
- diferenciar carga historica de replicacion de cambios nuevos;
- usar Debezium para capturar inserts, updates y deletes;
- publicar eventos CDC en Kafka;
- replicar cambios hacia PostgreSQL RAW;
- discutir riesgos de migracion de monolitos legacy;
- construir un flujo ETL para BI/ML con Spark a partir de datos RAW;
- generar tablas mart en Parquet;
- reconocer que herramientas orientadas a BI no reemplazan CDC para migracion OLTP critica.

## Nota sobre Kafka y Debezium

El laboratorio principal de Big Data usa un Kafka moderno sin ZooKeeper:

```text
kafka/compose.yml -> apache/kafka:4.2.0
```

Ese Kafka trabaja en modo moderno con KRaft. En cambio, muchos laboratorios y
ejemplos de Debezium usan el stack clasico:

```text
ZooKeeper -> Kafka -> Kafka Connect -> Debezium
```

La diferencia no significa que Debezium dependa conceptualmente de ZooKeeper.
Debezium corre dentro de Kafka Connect y publica eventos en Kafka. Lo que ocurre
es que el stack oficial/clasico de Debezium para talleres suele venir con Kafka
mas antiguo y ZooKeeper porque es estable, conocido y facil de reproducir para
CDC.

Para el curso hay dos opciones:

1. Reemplazar el Kafka moderno por un stack Debezium completo con ZooKeeper,
   Kafka, Kafka UI y Kafka Connect.
2. Mantener dos stacks Kafka alternativos: `kafka/` para el Kafka moderno y
   `kafka-debezium/` para CDC. Como usan los mismos puertos, el alumno levanta
   uno u otro.

La segunda opcion es mas clara pedagogicamente porque conserva los mismos
puertos, la misma red y el mismo alias `kafka:9092`.

Tecnicamente ambos stacks podrian correr en paralelo si se cambian puertos,
nombres internos, alias y red Docker. Para el curso se recomienda no hacerlo:
por equipos limitados y por claridad operativa, se debe ejecutar `kafka/` o
`kafka-debezium/`, pero no ambos a la vez.

La prioridad de eleccion no es tanto el caso de uso, porque `kafka-debezium/`
puede cubrir los mismos escenarios del Kafka base y ademas CDC. La decision
principal es de recursos y necesidad:

- si no se trabajara CDC/Debezium, conviene usar `kafka/` porque es mas liviano;
- si se trabajara CDC/Debezium, conviene usar `kafka-debezium/` porque incluye
  ZooKeeper, Kafka Connect y Debezium;
- si el equipo tiene recursos limitados, no conviene cargar Debezium salvo que
  haga falta para la sesion.

### Stack Debezium disponible

El stack Debezium vive en:

```text
kafka-debezium/compose.yml
```

Usa los mismos puertos host que `kafka/` para funcionar como reemplazo directo
del Kafka moderno.

```yaml
name: lambdalab-kafka-debezium

services:
  zookeeper:
    image: debezium/zookeeper:2.7.3.Final
    container_name: lambdalab-kafka-debezium-zookeeper
    restart: unless-stopped
    ports:
      - "42181:2181"
    networks:
      - lambdalab-kafka-net

  kafka:
    image: debezium/kafka:2.7.3.Final
    container_name: lambdalab-kafka-debezium
    restart: unless-stopped
    ports:
      - "49092:9092"
    environment:
      ZOOKEEPER_CONNECT: zookeeper:2181
    depends_on:
      - zookeeper
    networks:
      lambdalab-kafka-net:
        aliases:
          - kafka

  kafka-exporter:
    image: danielqsj/kafka-exporter:v1.9.0
    container_name: lambdalab-kafka-debezium-exporter
    restart: unless-stopped
    command:
      - --kafka.server=kafka:9092
    depends_on:
      - kafka
    ports:
      - "49308:9308"
    networks:
      lambdalab-kafka-net:
        aliases:
          - kafka-exporter

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    container_name: lambdalab-kafka-debezium-ui
    restart: unless-stopped
    ports:
      - "48085:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: lambdalab-kafka-debezium
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9092
    depends_on:
      - kafka
    networks:
      - lambdalab-kafka-net

  connect:
    image: debezium/connect:2.7.3.Final
    container_name: lambdalab-kafka-debezium-connect
    restart: unless-stopped
    ports:
      - "48083:8083"
    environment:
      BOOTSTRAP_SERVERS: kafka:9092
      GROUP_ID: "1"
      CONFIG_STORAGE_TOPIC: "connect_configs"
      OFFSET_STORAGE_TOPIC: "connect_offsets"
      STATUS_STORAGE_TOPIC: "connect_statuses"
    depends_on:
      - kafka
    networks:
      - lambdalab-kafka-net

networks:
  lambdalab-kafka-net:
    name: lambdalab-kafka-net
```

Para usarlo:

```powershell
docker compose -f kafka/compose.yml down
docker compose -f kafka-debezium/compose.yml up -d
```

Asi quedan separados los dos laboratorios:

| Laboratorio | Kafka | Uso |
|---|---|---|
| `kafka/` | `apache/kafka:4.2.0` sin ZooKeeper | MS, MQ, Big Data, Spark, observabilidad/Telemetria IoT |
| `kafka-debezium/` | `debezium/kafka:2.7.3.Final` con ZooKeeper | MS, MQ, Big Data, Spark, observabilidad/Telemetria IoT + CDC, Kafka Connect, Debezium |

## Alcance del taller

Para el curso/taller, el alcance sera:

```text
MySQL -> Debezium -> Kafka -> PostgreSQL RAW
```

Desde PostgreSQL RAW se explicaran dos rutas:

- migracion de base de datos para una nueva aplicacion;
- ETL distribuido con Spark para BI/ML.

No se trabajara Oracle ni AWS DMS en la practica principal; pueden mencionarse
solo como contexto comparativo.
