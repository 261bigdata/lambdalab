# LambdaLab

Curso practico de Big Data con procesamiento distribuido, streaming, observabilidad y BI/ML distribuido.

[LambdaLab](https://github.com/261bigdata/lambdalab) es un repositorio unico del
curso de Big Data para construir pipelines batch y streaming con Spark y Kafka,
gestionar datos en formatos analiticos como
Parquet, aplicar observabilidad y desarrollar BI/ML distribuido. Integra
laboratorios ejecutables, servicios Docker y documentacion publicada.

## Producto del curso

Producto del curso = Producto U3:

```text
Sistema Big Data distribuido end-to-end que integra procesamiento batch,
procesamiento streaming, analitica/ML, observabilidad y visualizacion BI para
la toma de decisiones.
```

Resultado esperado del curso:

Al finalizar el curso, el estudiante implementa, integra y sustenta una solucion
Big Data end-to-end que combina pipelines batch distribuidos, ingesta y
procesamiento de eventos en tiempo real, analitica/ML a escala, observabilidad
tecnica y visualizacion BI. La solucion debe ejecutarse de forma reproducible,
mostrar evidencias de ejecucion, reportar metricas tecnicas y del modelo, y
demostrar valor para la toma de decisiones.

## Contenido

### U1: Arquitecturas Big Data y ETL batch distribuido

Producto U1: pipeline batch de ETL distribuido con salidas analiticas en
Parquet listas para BI/ML.

Resultado esperado U1: el estudiante construye un pipeline batch reproducible
con procesamiento distribuido, aplica transformaciones sobre datos a escala,
valida la calidad basica de los datos, organiza salidas en formatos analiticos
como Parquet y deja un dataset preparado para consumo BI/ML.

- Sesion 1: Arquitectura Big Data.
- Sesion 2: Fundamentos Apache Spark.
- Sesion 3: Procesamiento batch con Spark: ETL distribuido.
- Sesion 4: Almacenamiento, HDFS y formatos.
- Sesion 5: Evaluacion U1.

### U2: Sistema Big Data en tiempo real: streaming, operacion y ML a escala

Producto U2: pipeline streaming en Spark para ML/BI a escala y en tiempo real.

Resultado esperado U2: el estudiante implementa un pipeline Big Data en tiempo
real que integra ingesta de eventos mediante Kafka, procesamiento distribuido
con Spark Structured Streaming, observabilidad y estimacion de costos
operacionales. Ademas, entrena, evalua, guarda y reutiliza modelos distribuidos
con Spark MLlib para inferencia batch y/o streaming, seleccionando mejores
configuraciones mediante experimentacion distribuida.

- Sesion 6: Ingesta en tiempo real (Kafka).
- Sesion 7: Procesamiento en Streaming con Spark.
- Sesion 8: Observabilidad (Grafana) y Costos.
- Sesion 9: ML distribuido: regresion con MLlib (modelo entrenado, evaluado y guardado).
- Sesion 10: Series de tiempo e inferencia en streaming (aplicacion del modelo guardado sobre datos batch y/o Kafka streaming).
- Sesion 11: Tuning y experimentacion distribuida (mejor modelo seleccionado con validacion distribuida).
- Sesion 12: Evaluacion U2.

### U3: Integracion, DataOps y despliegue del sistema final

Producto U3 / producto del curso: sistema Big Data distribuido end-to-end que
integra procesamiento batch, procesamiento streaming, analitica/ML,
observabilidad y visualizacion BI para la toma de decisiones.

Resultado esperado U3: el estudiante integra los componentes desarrollados en
las unidades anteriores, despliega o empaqueta el sistema mediante practicas de
DataOps/DevOps, prepara una demo end-to-end, documenta la operacion del sistema,
valida resultados tecnicos, analiticos y operacionales, y sustenta una solucion
final orientada a la toma de decisiones.

- Sesion 13: Integracion del sistema, DataOps y BI.
- Sesion 14: Revision tecnica final y hardening.
- Sesion 15: Sustentacion final con demo end-to-end.
- Sesion 16: Evaluacion final.

## Arquitectura del laboratorio

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
3. En los laboratorios de streaming, Spark consume eventos desde el broker y produce resultados para BI/ML.
4. Los casos de uso publican y consumen eventos para simular flujos reales.


## Arquitectura Uber

Uber maneja millones de eventos por segundo en tiempo real usando Kafka como
columna vertebral de su sistema de datos. La siguiente imagen muestra como
organizan el almacenamiento por niveles (tiered storage) para procesar
pedidos, pagos y ubicaciones a escala global. Esta arquitectura inspira los
conceptos que veremos en el curso: streaming, particionamiento, tolerancia a
fallos y procesamiento distribuido.

![Arquitectura Uber](https://lh7-us.googleusercontent.com/docsz/AD_4nXePSpSp72unfaVqK7tofbbbOpMaZLJ7qYJ2Es-Chg3CHBeZ9kcJDZ9ouvPRYs-CarI8bAqXs2459rJ0_QrsgBaUwqikE5fwYSianNkl1u6Ehbjz_yH6XuWJGn54P5kCaRSaBrCgeVPN4q2QC_RDu9ag1YgU?key=kis14CJAvWJjUiCdmN0jHg)

Fuente: [Kafka tiered storage at Uber](https://www.uber.com/us/en/blog/kafka-tiered-storage/)
