# Plantilla entregable U3

## Unidad 3: Integración y sustentación del producto final

**Producto de la unidad / producto del curso:** sistema Big Data integrado con
procesamiento batch, procesamiento streaming y componente de ML con series de
tiempo e inferencia.

---

## Datos generales

**Curso:** Big Data  
**Unidad:** 3  
**Estudiante / equipo:** ______________________________  
**Fecha:** ____ / ____ / ______  
**Docente:** ______________________________  

---

## Entregable esperado

El estudiante/equipo debe presentar el producto final del curso como integración
de los entregables de la U1 y U2. El sistema debe evidenciar un flujo Big Data
coherente que parte de datos procesados en batch, incorpora ingesta o
procesamiento en tiempo real cuando corresponda, y desarrolla un componente de
ML con series de tiempo e inferencia.

DataOps y BI pueden describirse como proyección o mejora futura, pero no son
obligatorios en esta evaluación porque no se desarrollaron completamente por
limitaciones de tiempo.

---

## Sesiones de la Unidad 3

| Sesión | Tema | Actividad esperada | Evidencia esperada |
|---|---|---|---|
| S13 | Integración del sistema | Unificar entregables U1 y U2 en una arquitectura final. | Diagrama, flujo integrado y relación entre componentes. |
| S14 | Revisión técnica final | Validar ejecución, estructura, artefactos y consistencia del producto. | Evidencias de pruebas, revisión de notebooks/scripts y resultados. |
| S15 | Sustentación final | Presentar demo end-to-end o recorrido técnico del sistema. | Demo, capturas, resultados y explicación técnica. |
| S16 | Evaluación final | Consolidar el informe final del producto del curso. | Informe completo, rúbrica y conclusiones. |

---

## Estructura sugerida del informe

### 1. Resumen ejecutivo

Describe el producto final, el problema abordado y el valor del sistema Big
Data construido.

### 2. Objetivo del producto

Incluye:

- problema o necesidad de negocio;
- objetivo general del sistema;
- usuarios o áreas beneficiadas;
- pregunta analítica o predictiva principal;
- alcance real implementado.

### 3. Arquitectura integrada del sistema

Incluye:

- fuentes de datos;
- pipeline batch de U1;
- pipeline streaming de U2 si aplica;
- almacenamiento analítico;
- componente de ML/series de tiempo;
- salidas o resultados del sistema;
- componentes no implementados y justificación.

### 4. Integración del entregable U1

Resume el pipeline batch construido en la Unidad 1:

- datasets fuente;
- transformaciones ETL aplicadas;
- reglas de calidad;
- joins, agregaciones o ventanas;
- salida en Parquet;
- particionado o diseño de almacenamiento;
- dataset final preparado para análisis o ML.

#### Evidencias U1

| Evidencia | Ruta / captura / resultado | Observación |
|---|---|---|
| Notebook o script ETL | | |
| Dataset procesado | | |
| Salida Parquet | | |
| Validación de calidad | | |

### 5. Integración del entregable U2

Resume el trabajo de la Unidad 2:

- ingesta de eventos con Kafka o fuente equivalente;
- procesamiento streaming con Spark si fue implementado;
- métricas, observabilidad o costos si fueron trabajados;
- dataset analítico o salida generada;
- modelo ML entrenado, evaluado o reutilizado;
- inferencia batch o streaming.

#### Evidencias U2

| Evidencia | Ruta / captura / resultado | Observación |
|---|---|---|
| Producer/consumer o fuente streaming | | |
| Notebook/script streaming | | |
| Métricas o resultados operativos | | |
| Modelo ML o artefacto | | |

### 6. ML con series de tiempo e inferencia

Documenta el componente analítico principal de cierre:

- variable objetivo;
- ventana temporal o criterio de ordenamiento;
- features utilizadas;
- algoritmo o enfoque aplicado;
- separación entrenamiento/evaluación;
- métricas obtenidas;
- predicciones generadas;
- evidencia de inferencia.

#### Resultados del modelo

| Experimento | Features | Modelo | Métrica principal | Resultado | Observación |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### 7. Demo end-to-end

Describe el recorrido técnico que se presentará en la sustentación:

- inicio del flujo;
- ejecución o evidencia del pipeline batch;
- ejecución o evidencia del pipeline streaming;
- generación o uso del dataset analítico;
- entrenamiento o carga del modelo;
- inferencia y resultados;
- interpretación final.

### 8. Evidencias técnicas

Adjunta o referencia:

- notebooks ejecutados;
- scripts relevantes;
- capturas de ejecución;
- logs;
- rutas de artefactos;
- tablas de resultados;
- capturas de predicciones;
- archivos Parquet o modelos guardados.

### 9. Limitaciones y alcance no implementado

Declara con claridad:

- qué partes quedaron completamente implementadas;
- qué partes quedaron como propuesta o mejora futura;
- si DataOps no fue implementado;
- si BI no fue implementado;
- riesgos o restricciones técnicas encontradas.

### 10. Conclusiones

Resume:

- qué se logró integrar;
- cómo se relacionan U1 y U2 en el producto final;
- qué valor aporta el componente de ML/series de tiempo;
- qué mejoras serían prioritarias para una siguiente versión.

---

## Rúbrica de evaluación

| Criterio | N1 Inicio | N2 En proceso | N3 Logro esperado |
|---|---|---|---|
| Integración del producto | Presenta componentes aislados sin relación clara. | Integra parcialmente U1 y U2, pero con vacíos en el flujo. | Integra U1 y U2 en una arquitectura final clara y coherente. |
| Pipeline batch U1 | No evidencia el pipeline batch o la salida analítica. | Evidencia parcialmente ETL, calidad o salida Parquet. | Evidencia ETL batch reproducible, calidad básica y salida Parquet validada. |
| Pipeline streaming U2 | No evidencia ingesta o procesamiento en tiempo real. | Evidencia parcialmente Kafka, Spark Streaming o resultados operativos. | Evidencia un flujo streaming o equivalente, con resultados verificables. |
| ML y series de tiempo | No presenta modelo, inferencia ni resultados claros. | Presenta modelo o inferencia con evidencias incompletas. | Presenta ML con series de tiempo, métricas e inferencia claramente evidenciada. |
| Coherencia técnica | El sistema no muestra relación entre datos, procesamiento y resultados. | La relación técnica existe, pero con explicaciones incompletas. | Explica claramente cómo los datos procesados alimentan los resultados o predicciones. |
| Evidencias de ejecución | No presenta evidencias verificables. | Presenta evidencias parciales o poco ordenadas. | Presenta evidencias claras de notebooks, scripts, artefactos, resultados y predicciones. |
| Sustentación end-to-end | La demo o explicación no permite entender el producto. | La sustentación muestra partes del sistema, pero sin recorrido completo. | La sustentación presenta un recorrido técnico claro del sistema integrado. |
| Manejo de limitaciones | No declara limitaciones ni alcance real. | Declara limitaciones de forma general. | Declara con precisión lo implementado, lo no implementado y mejoras futuras. |
| Estructura del informe | Documento incompleto o desordenado. | Documento parcialmente organizado. | Documento completo, ordenado y alineado a la plantilla. |
| Claridad y presentación | Difícil de entender. | Entendible, pero poco claro. | Claro, ordenado y profesional. |

---

## Producto final del curso

Sistema Big Data integrado que consolida el pipeline batch de U1, el trabajo
streaming/ML de U2 y una sustentación final centrada en ML con series de tiempo
e inferencia, dejando DataOps y BI como mejoras futuras cuando no hayan sido
implementados.
