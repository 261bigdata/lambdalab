# Ingesta de eventos IoT/sensores en tiempo real

## Proposito de la sesion

Implementar un segundo patron de ingesta en tiempo real usando eventos de
sensores. Esta sesion complementa el caso empresarial de la sesion 6 y prepara
datos IoT para ser consumidos posteriormente con Spark Structured Streaming.

## Resultado esperado

Al finalizar, el estudiante debe tener un flujo de eventos de sensores publicado
en Kafka, con contrato de evento documentado y evidencias de producer, topic y
consumer.

## Flujo de referencia

```text
sensor o simulador -> producer/bridge -> Kafka -> consumer de validacion
```

Para el laboratorio se puede usar una de estas alternativas:

- simulador local en Python;
- Wokwi como entorno de sensores;
- puente MQTT/HTTP hacia Kafka, si la practica lo requiere.

## Topic sugerido

```text
sensor-eventos
```

## Evento sugerido

```json
{
  "tipoEvento": "sensor.lectura",
  "sensorId": "sensor-001",
  "variable": "temperatura",
  "valor": 24.8,
  "unidad": "C",
  "origen": "wokwi",
  "timestamp": 1710000000000
}
```

## Actividades

1. Crear el topic de sensores en Kafka.
2. Generar eventos desde el simulador o entorno Wokwi.
3. Validar los mensajes con un consumer.
4. Documentar el contrato del evento.
5. Registrar evidencias para la evaluacion U2.

## Evidencias

- topic creado en Kafka;
- mensajes de sensores publicados;
- consumer recibiendo eventos;
- contrato de evento;
- observaciones sobre frecuencia, volumen y formato de mensajes.

## Relacion con las siguientes sesiones

En la sesion 8, Spark Structured Streaming podra consumir eventos de negocio,
CDC o sensores desde Kafka. El objetivo es que el estudiante comprenda que Kafka
puede integrar multiples fuentes de ingesta para un mismo sistema Big Data.
