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
- `obs/compose.yml`: Prometheus y Grafana para observabilidad.
- `uso-rapido/`: caso de uso ligero en Python para producer/consumer Kafka.
- `uso-ms-sb/`: caso de uso con microservicios Spring Boot.
- `uso-atmos/`: caso de uso IoT reservado para mas adelante.
- `docs/`: version documental en Markdown publicada con MkDocs.

## Laboratorio Spark local

Levanta el entorno desde la raiz del repositorio:

```powershell
docker compose -f pyspark/compose.yml up --build
```

Luego abre:

```text
http://localhost:4488
```

Spark UI queda disponible en:

```text
http://localhost:4040
```

Para trabajar con streaming, primero levanta Kafka:

```powershell
cd kafka
docker compose up -d
cd ..
```

Esto crea la red compartida:

```text
lambdalab-kafka-net
```

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
