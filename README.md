# LambdaLab

Repositorio unico del curso de Big Data. Integra laboratorios ejecutables,
documentacion publicada y servicios Docker para trabajar con Spark, Kafka,
streaming, observabilidad y ML distribuido.

## Estructura

- `pyspark/notebooks/`: cuadernos fuente para ejecutar localmente con Jupyter.
- `pyspark/notebooks/index.md`: portada fuente del sitio y diagramas Mermaid.
- `pyspark/data/`: datasets de practica.
- `pyspark/artifacts/`: salidas, checkpoints y modelos generados por Spark.
- `pyspark/compose.yml`: laboratorio Spark/Jupyter.
- `pyspark/compose.kafka.yml`: override para conectar Spark con la red Kafka.
- `kafka/compose.yml`: broker Kafka, Kafka UI y Kafka Exporter.
- `kafka-debezium/compose.yml`: stack Kafka alternativo con ZooKeeper, Kafka Connect y Debezium para CDC.
- `obs/compose.yml`: Prometheus y Grafana para observabilidad.
- `uso-rapido/`: caso de uso ligero en Python para producer/consumer Kafka.
- `uso-ms-sb/`: caso de uso con microservicios Spring Boot.
- `uso-atmos/`: caso de uso IoT reservado para mas adelante.
- `uso-replica-cdc/`: caso de uso futuro para migracion CDC MySQL a PostgreSQL RAW con Debezium y ETL BI/ML con Spark.
- `docs/`: version documental en Markdown publicada con MkDocs.

## Laboratorio Spark local

Levanta el entorno desde la raiz del repositorio:

```powershell
docker compose -f pyspark/compose.yml up --build
```

Luego abre JupyterLab:

```text
http://localhost:4488/lab?token=sintoken
```

Tambien puedes entrar a Jupyter Notebook:

```text
http://localhost:4488/?token=sintoken
```

Spark UI queda disponible en:

```text
http://localhost:4040
```

## Elegir stack Kafka

Antes de levantar Kafka, elige el stack segun recursos y necesidad de Debezium.
No es tanto una decision por caso de uso, porque `kafka-debezium/` tambien sirve
para MS, MQ, Big Data, Spark y observabilidad/Telemetria IoT. La diferencia es
que agrega ZooKeeper, Kafka Connect y Debezium, por lo que consume mas recursos.

| Stack | Uso recomendado |
|---|---|
| `kafka/` | Usa este stack si no trabajaras CDC/Debezium. Es el Kafka moderno y mas liviano. |
| `kafka-debezium/` | Usa este stack si trabajaras CDC/Debezium. Tambien sirve para MS, MQ, Spark, observabilidad y Telemetria IoT. |

Ambos stacks usan los mismos puertos, el mismo alias interno `kafka:9092` y la
misma red `lambdalab-kafka-net`. Tecnicamente podrian correr en paralelo si se
cambian puertos, nombres internos, alias y red Docker, pero para el curso se
recomienda ejecutar solo uno a la vez por equipos limitados y claridad operativa.

Para trabajar con streaming, primero levanta un stack Kafka desde la raiz del
repositorio.

Kafka moderno:

```powershell
docker compose -f kafka/compose.yml up -d
```

Kafka con Debezium:

```powershell
docker compose -f kafka-debezium/compose.yml up -d
```

Esto crea la red compartida:

```text
lambdalab-kafka-net
```

### Cambiar de stack Kafka

Los stacks `kafka/` y `kafka-debezium/` usan los mismos puertos, el mismo alias
interno `kafka:9092` y la misma red. Para cambiar de uno a otro, elimina primero
los contenedores del stack activo y luego levanta el otro. Las imagenes Docker
no se eliminan con estos comandos.

De Kafka moderno a Kafka Debezium:

```powershell
docker compose -f kafka/compose.yml down
docker compose -f kafka-debezium/compose.yml up -d
```

De Kafka Debezium a Kafka moderno:

```powershell
docker compose -f kafka-debezium/compose.yml down
docker compose -f kafka/compose.yml up -d
```

Si quieres liberar espacio despues de usar CDC, puedes eliminar solo las
imagenes legacy de Debezium. Primero baja el stack:

```powershell
docker compose -f kafka-debezium/compose.yml down
```

Opcionalmente, elimina las imagenes Debezium:

```powershell
docker image rm debezium/zookeeper:2.7.3.Final
docker image rm debezium/kafka:2.7.3.Final
docker image rm debezium/connect:2.7.3.Final
```

No elimines `provectuslabs/kafka-ui:latest` ni
`danielqsj/kafka-exporter:v1.9.0`, porque tambien se usan en el stack Kafka
moderno.

Luego Spark puede levantarse conectado a esa red:

```powershell
docker compose -f pyspark/compose.yml -f pyspark/compose.kafka.yml up --build
```

Para observabilidad:

```powershell
cd obs
docker compose up -d
cd ..
```

Servicios disponibles:

- Kafka UI: `http://localhost:48085`
- Prometheus: `http://localhost:49090`
- Grafana: `http://localhost:43000`

## Puertos

| Modulo | Servicio | Host | Contenedor |
|---|---|---:|---:|
| `pyspark` | Jupyter | 4488 | 8888 |
| `pyspark` | Spark UI | 4040 | 4040 |
| `kafka` | Kafka externo | 49092 | 49092 |
| `kafka` | Kafka Exporter | 49308 | 9308 |
| `kafka` | Kafka UI | 48085 | 8080 |
| `kafka-debezium` | Kafka Connect | 48083 | 8083 |
| `kafka-debezium` | ZooKeeper | 42181 | 2181 |
| `obs` | Prometheus | 49090 | 9090 |
| `obs` | Grafana | 43000 | 3000 |
| `obs` | Loki, comentado | 43100 | 3100 |
| `uso-ms-sb/ec-orden-ms` | MySQL ordenes | 49020 | 3306 |
| `uso-ms-sb/ec-orden-ms` | API ordenes | 49021 | 9021 |
| `uso-ms-sb/ec-pago-ms` | MySQL pagos | 49030 | 3306 |
| `uso-ms-sb/ec-pago-ms` | API pagos | 49031 | 9031 |
| `uso-rapido/ec-orden-py` | Python producer/consumer | - | - |

## Casos de uso

Los contenedores de los casos de uso tambien usan el prefijo `lambdalab-*` para
que puedan identificarse y eliminarse en bloque.

- Python rapido: `uso-rapido/ec-orden-py`
- Spring Boot: `uso-ms-sb/ec-orden-ms` y `uso-ms-sb/ec-pago-ms`
- IoT: `uso-atmos` queda reservado para una practica posterior.
- Migracion CDC MySQL a PostgreSQL RAW con Debezium: `uso-replica-cdc` queda reservado para una practica posterior con dos caminos: migracion sin detener el monolito y ETL BI/ML con Spark.

## Sitio de documentacion

La carpeta `docs/` se genera desde los notebooks. Los alumnos ejecutan los
`.ipynb` desde `pyspark/notebooks/`; GitHub Pages publica solo la version
documental exportada a Markdown durante el deploy.

Para regenerar la documentacion desde los notebooks:

```powershell
python scripts/export_notebooks.py
```

El workflow de GitHub Pages ejecuta ese script antes de compilar el sitio, asi
que el despliegue siempre publica la version Markdown derivada de los notebooks.
En la practica, la fuente que debes editar es `pyspark/notebooks/`.

Para probar el sitio localmente:

```powershell
mkdocs serve
```

Para construirlo:

```powershell
mkdocs build
```

## Contenido

### U1: Arquitecturas Big Data y ETL distribuido

Producto: pipeline batch en Spark con dataset listo para BI/ML.

- Sesion 1: Arquitectura Big Data.
- Sesion 2: Fundamentos Apache Spark.
- Sesion 3: Procesamiento batch con Spark: ETL distribuido.
- Sesion 4: Almacenamiento, HDFS y formatos.
- Sesion 5: Evaluacion U1.

### U2: Sistema Big Data en tiempo real

Producto: pipeline streaming en Spark para ML/BI a escala y en tiempo real.

- Sesion 6: Ingesta en tiempo real con Kafka.
- Sesion 7: Procesamiento en streaming con Spark.
- Sesion 8: Observabilidad con Grafana y costos.
- Sesion 9: ML distribuido: regresion con MLlib.
- Sesion 10: Series de tiempo e inferencia en streaming.
- Sesion 11: Tuning y experimentacion distribuida.
- Sesion 12: Evaluacion U2.
