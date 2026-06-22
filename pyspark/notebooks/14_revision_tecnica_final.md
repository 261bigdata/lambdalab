# Sesión 14: Revisión técnica final

## Unidad 3: Integración y sustentación del producto final

**Propósito:** revisar la consistencia técnica del producto final antes de la
sustentación, verificando ejecución, evidencias, artefactos y claridad del
recorrido end-to-end.

## Producto de la sesión

Lista de verificación técnica del sistema Big Data integrado y plan de ajustes
antes de la evaluación U3.

## 1. Revisión de arquitectura

Verifica que la arquitectura final:

- muestre fuentes de datos;
- conecte batch, streaming y ML cuando corresponda;
- identifique rutas o artefactos principales;
- distinga lo implementado de lo propuesto;
- no incluya componentes no trabajados como si estuvieran implementados.

Tabla de revisión:

| Componente | Implementado | Evidencia | Observación |
|---|---|---|---|
| Fuente de datos | [ ] | | |
| ETL batch Spark | [ ] | | |
| Salida Parquet | [ ] | | |
| Streaming Kafka/Spark | [ ] | | |
| ML / series de tiempo | [ ] | | |
| Inferencia | [ ] | | |

## 2. Revisión del pipeline batch U1

Valida:

- notebook o script ejecutado;
- lectura de datos;
- limpieza y transformaciones;
- reglas de calidad;
- escritura en Parquet;
- lectura de validación;
- evidencia del dataset final.

Preguntas guía:

- ¿El ETL puede explicarse como Extract, Transform y Load?
- ¿La salida Parquet existe o está evidenciada?
- ¿Se entiende qué problema resuelve el dataset final?

## 3. Revisión del pipeline U2

Valida según el alcance logrado:

- ingesta de eventos o fuente equivalente;
- procesamiento streaming si fue implementado;
- resultados del procesamiento;
- métricas, observabilidad o costos si fueron trabajados;
- modelo ML entrenado o reutilizado;
- evidencia de inferencia.

Preguntas guía:

- ¿Se entiende qué parte corresponde a tiempo real?
- ¿Hay evidencia de producer/consumer, Kafka o Spark Streaming?
- Si no se ejecutó streaming completo, ¿está claramente delimitado el alcance?

## 4. Revisión de ML con series de tiempo

Valida:

- variable objetivo;
- variable temporal u orden lógico;
- features;
- modelo o enfoque;
- métrica de evaluación;
- predicciones;
- interpretación de resultados.

Tabla sugerida:

| Elemento ML | Evidencia | Observación |
|---|---|---|
| Dataset de entrenamiento | | |
| Features | | |
| Modelo | | |
| Métrica | | |
| Predicciones | | |

## 5. Revisión de evidencias

Cada evidencia debe ser fácil de ubicar y explicar.

Evidencias mínimas:

- diagrama de arquitectura;
- notebooks o scripts principales;
- capturas o salidas de ejecución;
- tabla de calidad o validación;
- salida Parquet;
- resultados de streaming si aplica;
- resultados de ML/inferencia;
- limitaciones declaradas.

## 6. Ensayo de sustentación

Orden sugerido para la presentación:

1. Problema y objetivo.
2. Arquitectura integrada.
3. Entregable U1: batch + Parquet.
4. Entregable U2: streaming + ML.
5. Series de tiempo e inferencia.
6. Evidencias y resultados.
7. Limitaciones y mejoras futuras.

Tiempo recomendado:

| Bloque | Tiempo sugerido |
|---|---|
| Problema y arquitectura | 2 min |
| U1 batch/Parquet | 3 min |
| U2 streaming/ML | 3 min |
| Inferencia y resultados | 3 min |
| Cierre y limitaciones | 1 min |

## Actividad de la sesión

Completa la revisión final:

| Aspecto | Estado | Acción pendiente |
|---|---|---|
| Arquitectura final clara | | |
| ETL batch evidenciado | | |
| Parquet validado | | |
| Streaming o alcance U2 claro | | |
| ML/series de tiempo evidenciado | | |
| Demo preparada | | |
| Limitaciones declaradas | | |

## Cierre

Al finalizar esta sesión, el equipo debe tener el producto listo para la
sustentación final y saber exactamente qué evidencias mostrará para sostener su
evaluación.
