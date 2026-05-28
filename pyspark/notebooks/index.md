# LambdaLab

Curso practico de Big Data con Spark, Kafka, streaming, observabilidad y ML distribuido.

## Arquitectura del proyecto

```mermaid
flowchart LR
    subgraph PySparkModule["pyspark"]
        direction TB
        Notebooks["notebooks/*.ipynb"]
        Jupyter["Jupyter<br/>localhost:4488"]
        Spark["Spark / PySpark<br/>localhost:4040"]
        Data["data/*.csv"]
        Artifacts["artifacts/"]
        Notebooks --> Jupyter --> Spark
        Data --> Spark --> Artifacts
    end

    subgraph UseFast["uso-rapido"]
        PyQuick["ec-orden-py<br/>publica / consume<br/>orden-eventos"]
    end

    subgraph UseMS["uso-ms-sb"]
        direction TB
        OrdenMS["ec-orden-ms<br/>API localhost:49021<br/>publica orden-eventos"]
        OrdenDB["mysql ordenes<br/>localhost:49020"]
        PagoMS["ec-pago-ms<br/>API localhost:49031<br/>consume orden-eventos<br/>publica pago-eventos"]
        PagoDB["mysql pagos<br/>localhost:49030"]
        OrdenMS --> OrdenDB
        PagoMS --> PagoDB
    end

    subgraph UseIoT["uso-atmos"]
        IoT["pendiente"]
    end

    subgraph UseCDC["uso-replica-cdc"]
        CDC["pendiente<br/>MySQL -> Debezium -> Kafka -> PostgreSQL RAW<br/>migracion / Spark BI-ML"]
    end

    subgraph KafkaModule["kafka"]
        direction TB
        subgraph KafkaStack[" "]
            direction TB
            Kafka["Apache Kafka<br/>kafka:9092<br/>localhost:49092"]
            KafkaUI["Kafka UI<br/>localhost:48085"]
            KafkaExporter["Kafka Exporter<br/>localhost:49308"]
            Kafka --> KafkaUI
            Kafka --> KafkaExporter
        end
    end

    subgraph ObsModule["obs"]
        direction TB
        subgraph ObsStack[" "]
            direction TB
            Prometheus["Prometheus<br/>localhost:49090"]
            Grafana["Grafana<br/>localhost:43000"]
            Prometheus --> Grafana
        end
    end

    PySparkModule -->|"U2: streaming consumer"| Kafka
    UseFast -->|"orden-eventos"| Kafka
    UseMS -->|"orden-eventos / pago-eventos"| Kafka
    UseIoT -. "futuro" .-> Kafka
    UseCDC -. "futuro: migracion CDC" .-> Kafka
    KafkaExporter -->|"metricas"| Prometheus

    style KafkaStack fill:transparent,stroke:transparent,color:transparent
    style ObsStack fill:transparent,stroke:transparent,color:transparent
```

## Flujo de trabajo

1. El alumno ejecuta los notebooks desde `pyspark/notebooks/` usando el laboratorio local.
2. Spark lee datos desde `pyspark/data/` y escribe resultados temporales en `pyspark/artifacts/`.
3. En los laboratorios de streaming, Spark consume eventos desde Kafka y produce resultados para BI/ML.
4. Los casos de uso publican y consumen eventos de Kafka para simular flujos reales.

## Unidades

### U1: Arquitecturas Big Data y ETL distribuido

Producto: pipeline batch en Spark con dataset listo para BI/ML.

### U2: Sistema Big Data en tiempo real

Producto: pipeline streaming en Spark para ML/BI a escala y en tiempo real.
