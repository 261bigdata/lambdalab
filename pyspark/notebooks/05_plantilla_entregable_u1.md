# Plantilla entregable U1

## Unidad 1: Arquitecturas Big Data y ETL batch distribuido

**Producto de la unidad:** pipeline batch de ETL distribuido con Spark, reglas
de calidad básica, diseño de almacenamiento y salidas analíticas en Parquet
listas para BI/ML.

---

## Datos generales

**Curso:** Big Data  
**Unidad:** 1  
**Estudiante / equipo:** ______________________________  
**Fecha:** ____ / ____ / ______  
**Docente:** ______________________________  

---

## Entregable esperado

El estudiante/equipo debe presentar un pipeline batch funcional basado en
Apache Spark, acompañado de una propuesta de arquitectura Big Data, evidencias
de extracción, transformación, validación de calidad, escritura en formato
analítico y una justificación técnica del diseño de almacenamiento elegido.

---

## Sesiones de la Unidad 1

| Sesión | Tema | Actividad práctica | Evidencia esperada |
|---|---|---|---|
| S1 | Arquitectura Big Data | Analizar un caso, identificar batch/streaming y proponer arquitectura Lambda o Kappa. | Ficha de arquitectura, flujo lógico y justificación de la elección. |
| S2 | Fundamentos Apache Spark | Crear SparkSession, cargar DataFrames, explorar datos, usar acciones, lazy evaluation y RDD. | Notebook ejecutado, resultados de consultas, acciones y plan de ejecución. |
| S3 | ETL distribuido en batch | Construir flujo ETL con limpieza, joins, funciones ventana y validación de calidad. | Pipeline ETL ejecutado, reglas aplicadas, métricas de calidad y salida Parquet. |
| S4 | HDFS, formatos y almacenamiento | Diseñar salida analítica con Parquet, particionado y lectura de validación. | Estructura física de salida, comparación CSV/Parquet y justificación técnica. |

---

## Estructura sugerida del informe

### 1. Resumen ejecutivo

Describe el caso elegido, el objetivo del pipeline batch y el resultado
obtenido.

### 2. Caso de negocio y arquitectura propuesta

Incluye:

- problema o necesidad de datos;
- usuarios o áreas que consumirán el resultado;
- tipo de procesamiento requerido: batch, streaming o mixto;
- arquitectura propuesta: Lambda, Kappa u otra variante justificada;
- flujo lógico desde fuentes hasta salida analítica.

### 3. Fuentes de datos

Documenta:

- datasets utilizados;
- ubicación de archivos fuente;
- formato original;
- volumen aproximado;
- columnas principales;
- problemas detectados en los datos.

#### Diccionario básico de datos

| Campo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### 4. Extracción y exploración con Spark

Documenta:

- creación de la SparkSession;
- lectura de archivos;
- esquema inferido o definido;
- conteo de registros;
- primeras filas;
- exploración inicial con DataFrames.

### 5. Transformaciones ETL

Describe las transformaciones implementadas:

- limpieza de nulos o registros inválidos;
- eliminación de duplicados;
- filtros de negocio;
- joins distribuidos;
- agregaciones;
- funciones ventana;
- columnas derivadas;
- decisiones iniciales de rendimiento.

### 6. Validación de calidad de datos

Registra los controles aplicados.

| Regla de calidad | Dataset/columna | Resultado | Acción aplicada | Evidencia |
|---|---|---|---|---|
| Nulos | | | | |
| Duplicados | | | | |
| Valores inválidos | | | | |
| Integridad de join | | | | |

### 7. Ejecución y plan de procesamiento

Incluye evidencias de:

- acciones que disparan ejecución;
- lazy evaluation;
- plan lógico o físico con `explain`;
- particiones utilizadas si aplica;
- observaciones de rendimiento.

### 8. Carga y almacenamiento analítico

Documenta:

- ruta de salida;
- formato elegido;
- particionado aplicado;
- compresión si aplica;
- lectura de validación desde Parquet;
- estructura física de carpetas;
- consulta objetivo que se beneficia del diseño.

### 9. Comparación y justificación técnica

Explica por qué el formato y particionado son adecuados para el caso.

| Criterio | CSV u origen | Parquet / salida analítica | Comentario |
|---|---|---|---|
| Tamaño | | | |
| Lectura selectiva | | | |
| Esquema | | | |
| Consumo BI/ML | | | |

### 10. Dataset final para BI/ML

Describe:

- tabla o dataset final generado;
- granularidad;
- columnas finales;
- métricas o indicadores disponibles;
- posibles consultas BI;
- posible uso posterior en ML.

### 11. Evidencias

Adjunta o referencia:

- capturas de ejecución;
- logs;
- salidas de consola;
- fragmentos de código;
- notebooks/scripts usados;
- rutas de archivos Parquet;
- tablas de resultados;
- capturas de estructura de carpetas.

### 12. Conclusiones

Resume:

- qué se logró implementar;
- qué problemas de datos se encontraron;
- qué decisiones técnicas se tomaron;
- cómo el resultado queda preparado para la Unidad 2 o para consumo BI/ML.

---

## Rúbrica de evaluación

| Criterio | N1 Inicio | N2 En proceso | N3 Logro esperado |
|---|---|---|---|
| Arquitectura Big Data | Presenta una arquitectura incompleta o sin relación clara entre componentes. | Presenta una arquitectura definida, pero con algunas incoherencias en el flujo de datos. | Presenta una arquitectura clara y coherente, incluyendo fuente, Spark, almacenamiento y salida analítica. |
| Procesamiento con Spark | Solo realiza lectura básica o transformaciones mínimas. | Realiza transformaciones, pero con errores o poca consistencia. | Realiza lectura, exploración, limpieza, tipado y transformaciones correctas en Spark. |
| Fundamentos de ejecución Spark | No evidencia acciones, lazy evaluation ni plan de ejecución. | Evidencia parcialmente acciones o plan de ejecución. | Explica y evidencia acciones, lazy evaluation y/o plan de ejecución con claridad. |
| Proceso ETL | ETL incompleto o no evidenciado. | ETL funcional, pero con debilidades en alguna fase. | ETL completo, estructurado y evidenciado: Extract, Transform y Load. |
| Calidad del dataset final | Dataset con errores, nulos críticos o mala estructura. | Dataset parcialmente limpio, con detalles pendientes. | Dataset limpio, consistente, tipado y listo para análisis/BI. |
| Almacenamiento analítico en Parquet | No almacena correctamente o no usa formato analítico. | Almacena en Parquet, pero sin validación o justificación suficiente. | Almacena correctamente en Parquet, valida lectura y justifica formato/particionado. |
| Diseño de almacenamiento | No explica ruta, estructura ni criterio de organización. | Describe parcialmente la salida o el particionado. | Explica ruta, estructura física, particionado y consulta objetivo beneficiada. |
| Evidencias de ejecución | No presenta evidencias. | Presenta evidencias parciales. | Presenta evidencias claras de Spark, ETL, validaciones y salida Parquet. |
| Estructura del entregable | Documento desordenado o incompleto. | Documento parcialmente organizado. | Documento completo, ordenado y alineado a la plantilla. |
| Claridad y presentación | Difícil de entender. | Entendible, pero poco claro. | Claro, ordenado y profesional. |

---

## Producto final de Unidad 1

Pipeline batch distribuido con Spark,
salida analítica en Parquet, validación de calidad básica y dataset preparado
para consumo BI/ML o integración con las siguientes unidades.
