# Sesión 13: Integración del sistema

## Unidad 3: Integración y sustentación del producto final

**Propósito:** integrar los entregables de la Unidad 1 y la Unidad 2 en una
arquitectura final coherente para preparar la sustentación del producto del
curso.

## Producto de la sesión

Mapa integrado del sistema Big Data construido durante el curso, conectando:

- pipeline batch de U1;
- salida analítica en Parquet;
- pipeline streaming o evidencias de ingesta/procesamiento de U2;
- componente de ML con series de tiempo e inferencia;
- evidencias técnicas que sostienen la demo final.

## Alcance real trabajado

En esta versión del curso, la integración se enfoca en consolidar U1 + U2 y el
componente de ML. DataOps y BI pueden describirse como mejoras futuras, pero no
son componentes obligatorios de la entrega final.

## 1. Arquitectura integrada

El equipo debe construir un diagrama general del sistema.

Componentes mínimos:

- fuentes de datos;
- procesamiento batch con Spark;
- almacenamiento analítico en Parquet;
- ingesta o procesamiento streaming si fue implementado;
- dataset analítico para ML;
- modelo de series de tiempo o inferencia;
- resultados o predicciones.

Ejemplo de flujo lógico:

```text
Fuentes de datos
  -> Spark batch / ETL
  -> Dataset limpio en Parquet
  -> Dataset analítico
  -> Modelo ML / series de tiempo
  -> Inferencia y resultados
```

Si el equipo implementó streaming:

```text
Eventos Kafka
  -> Spark Structured Streaming
  -> Salida analítica
  -> Inferencia batch o streaming
```

## 2. Integración de U1

Resume el entregable de la Unidad 1:

- caso de negocio;
- datasets usados;
- transformaciones ETL;
- reglas de calidad aplicadas;
- salida Parquet;
- ruta de artefactos;
- validación de lectura.

Tabla sugerida:

| Elemento U1 | Evidencia | Estado |
|---|---|---|
| Notebook/script ETL | | |
| Dataset limpio | | |
| Salida Parquet | | |
| Validación de calidad | | |

## 3. Integración de U2

Resume el entregable de la Unidad 2:

- ingesta de eventos o fuente usada;
- procesamiento streaming si aplica;
- métricas o resultados operativos si fueron trabajados;
- dataset generado;
- modelo entrenado;
- inferencia realizada.

Tabla sugerida:

| Elemento U2 | Evidencia | Estado |
|---|---|---|
| Producer/consumer o fuente | | |
| Notebook/script streaming | | |
| Modelo ML | | |
| Inferencia | | |

## 4. Relación entre datos y ML

Explica cómo el dataset procesado alimenta el componente predictivo:

- qué columnas se usan como features;
- cuál es la variable objetivo;
- qué representa la dimensión temporal;
- cómo se separa entrenamiento/evaluación;
- qué predicción o resultado se obtiene.

## 5. Preparación de la demo

La demo no necesita ejecutar todo desde cero si el tiempo es limitado, pero debe
mostrar evidencias verificables.

Orden sugerido:

1. Presentar problema y arquitectura.
2. Mostrar ETL batch y salida Parquet.
3. Mostrar streaming o evidencias de U2.
4. Mostrar modelo de series de tiempo/inferencia.
5. Interpretar resultados.
6. Declarar limitaciones y mejoras futuras.

## Actividad de la sesión

Completa una ficha de integración:

| Pregunta | Respuesta |
|---|---|
| ¿Cuál es el problema que resuelve el sistema? | |
| ¿Qué entrega U1 al producto final? | |
| ¿Qué entrega U2 al producto final? | |
| ¿Dónde aparece ML o series de tiempo? | |
| ¿Qué evidencia se mostrará en la demo? | |
| ¿Qué quedó fuera del alcance? | |

## Cierre

Al finalizar esta sesión, el equipo debe tener claro cómo se conectan sus
notebooks, datos, artefactos y resultados en un solo producto final.
