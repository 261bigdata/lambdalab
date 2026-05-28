# Laboratorio PySpark

Entorno local para ejecutar los notebooks del curso con Spark y Jupyter.

## Carpetas

- `notebooks/`: cuadernos fuente ejecutables.
- `data/`: archivos de entrada para las practicas.
- `artifacts/`: resultados generados por Spark, como salidas Parquet,
  checkpoints y modelos.
- `Dockerfile`: imagen base del laboratorio.

## Uso

Desde la raiz del repositorio:

```powershell
docker compose -f pyspark/compose.yml up --build
```

Con Kafka:

```powershell
docker compose -f pyspark/compose.yml -f pyspark/compose.kafka.yml up --build
```

En modo Kafka, el broker interno queda disponible como:

```text
kafka:9092
```

Luego abre Jupyter en:

```text
http://localhost:4488
```

Los notebooks quedan montados dentro del contenedor en:

```text
/opt/notebooks
```

Los datos quedan disponibles en:

```text
/opt/data
```

Los artefactos generados se escriben en:

```text
/opt/artifacts
```

## Notebooks principales

- `01_arquitecturas_big_data.ipynb`
- `02_fundamentos_practica.ipynb`
- `03_etl_spark.ipynb`
- `04_hdfs_formatos.ipynb`
- `07_spark_streaming_consumer_ordenes.ipynb`
- `08_observabilidad_pipeline_kafka_spark.ipynb`
- `09_ml_distribuido_regresion_mllib.ipynb`
- `10_series_tiempo_inferencia_spark.ipynb`
- `11_tuning_experimentacion_distribuida.ipynb`
