# Evaluación U1

## Unidad 1: Arquitecturas Big Data y ETL batch distribuido

**Producto de la unidad:** pipeline batch de ETL distribuido con salidas
analíticas en Parquet listas para BI/ML.

La evaluación de la Unidad 1 se trabaja con la plantilla oficial del
entregable:

[Abrir plantilla del entregable U1](05_plantilla_entregable_u1.md)

## Alcance

La Unidad 1 evalúa las sesiones 1 a 4:

- Sesión 1: Arquitectura Big Data, ecosistema, batch vs streaming, Lambda y Kappa.
- Sesión 2: Fundamentos Apache Spark: SparkSession, DataFrames, acciones,
  lazy evaluation, planes de ejecución y RDD.
- Sesión 3: Procesamiento batch con Spark: ETL distribuido, limpieza, joins,
  funciones ventana, validación de calidad y salida Parquet.
- Sesión 4: Almacenamiento, HDFS y formatos: diseño de almacenamiento,
  particionado, Parquet, lectura selectiva y justificación técnica.

## Indicación para el estudiante

Completa la plantilla con evidencias técnicas del pipeline batch:

- problema o caso de negocio elegido y arquitectura Big Data propuesta;
- datasets fuente, estructura, diccionario básico y reglas de calidad;
- notebook o script de Spark ejecutado de inicio a fin;
- transformaciones aplicadas: filtros, limpieza, joins, agregaciones o ventanas;
- evidencias de lazy evaluation, acciones y plan de ejecución cuando aplique;
- salida analítica en Parquet, estrategia de particionado y lectura de validación;
- comparación o justificación técnica del formato de almacenamiento elegido;
- dataset final preparado para consumo BI/ML.

Entrega el informe con capturas, logs, fragmentos de código, tablas de
resultados y rutas de artefactos que permitan verificar la ejecución.
