# Ingesta de eventos empresariales en tiempo real

## Proposito de la sesion

Implementar y validar un flujo basico de ingesta de eventos empresariales en
tiempo real. En el laboratorio se usa Kafka como broker principal, pero el
patron tambien puede implementarse con otras tecnologias de mensajeria o event
streaming.

La practica puede trabajarse con uno de dos casos empresariales:

- **Caso MS:** microservicios que publican y consumen eventos de negocio.
- **Caso replica-cdc:** cambios de una base OLTP capturados con Debezium y publicados en Kafka.

En el caso MS, la practica conecta tres niveles de trabajo:

- producer y consumer manuales dentro del broker Kafka;
- producer y consumer en Python para pruebas rapidas;
- microservicios Spring Boot que publican y consumen eventos de negocio.

## Resultado esperado

Al finalizar, debes demostrar que Kafka recibe eventos en el topic `orden-eventos`, que los productores pueden publicar mensajes y que los consumidores pueden leerlos desde consola, Python o Spring Boot.

Si el grupo trabaja el caso replica-cdc, el resultado equivalente es demostrar
que los cambios de una tabla OLTP llegan a Kafka como eventos CDC y quedan
disponibles para consumo posterior con Spark.

El flujo de referencia es:

```text
ec-orden-ms -> orden-eventos -> ec-pago-ms -> pago-eventos
```

## Herramientas

- Apache Kafka
- Docker Compose
- Kafka UI
- Python
- Spring Boot
- Java 17
- PowerShell

## Entorno de trabajo

En LambdaLab, usa estos modulos:

- Kafka: `kafka/`
- Python rapido: `uso-rapido/ec-orden-py/`
- Microservicio de ordenes: `uso-ms-sb/ec-orden-ms/`
- Microservicio de pagos: `uso-ms-sb/ec-pago-ms/`

Servicios principales:

| Servicio | URL o host |
|---|---|
| Kafka externo | `localhost:49092` |
| Kafka interno Docker | `ec-kafka:9092` |
| Kafka UI | `http://localhost:48085` |
| Red Docker | `lambdalab-kafka-net` |

## 1. Levantar Kafka

Desde la raiz del repositorio:

```powershell
cd kafka
docker compose up -d
docker compose ps
cd ..
```

Verifica que esten activos el broker Kafka, Kafka UI y Kafka Exporter.

## 2. Crear el topic de trabajo

Entra al contenedor del broker:

```powershell
cd kafka
docker compose exec ec-kafka bash
```

Crea el topic `orden-eventos`:

```bash
/opt/kafka/bin/kafka-topics.sh --create \
  --topic orden-eventos \
  --bootstrap-server ec-kafka:9092 \
  --partitions 1 \
  --replication-factor 1
```

Lista los topics:

```bash
/opt/kafka/bin/kafka-topics.sh --list \
  --bootstrap-server ec-kafka:9092
```

Resultado esperado:

```text
orden-eventos
```

## 3. Probar producer y consumer manuales

Dentro del contenedor del broker, abre un producer:

```bash
/opt/kafka/bin/kafka-console-producer.sh \
  --topic orden-eventos \
  --bootstrap-server ec-kafka:9092
```

Escribe un mensaje de prueba:

```text
hola
```

En otra terminal, abre un consumer:

```bash
/opt/kafka/bin/kafka-console-consumer.sh \
  --topic orden-eventos \
  --bootstrap-server ec-kafka:9092 \
  --from-beginning
```

Verifica que el mensaje aparezca en el consumer.

## 4. Probar producer y consumer en Python

Usa el caso rapido:

```powershell
cd uso-rapido/ec-orden-py
docker compose up -d --build
```

Ejecuta el producer:

```powershell
docker compose exec ec-orden-py python /app/producer_ordenes.py
```

Ejecuta el consumer:

```powershell
docker compose exec ec-orden-py python /app/consumer_ordenes.py
```

Ejemplo de evento:

```json
{
  "tipoEvento": "orden.creada",
  "ordenId": 321,
  "total": 180.0,
  "estado": "PENDIENTE",
  "origen": "python",
  "timestamp": 1713350000000
}
```

## 5. Integrar con microservicios Spring Boot

### Ordenes como producer

```powershell
cd uso-ms-sb/ec-orden-ms
docker compose up -d
.\mvnw.cmd spring-boot:run
```

Publica una orden:

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://localhost:49021/ordenes" `
  -ContentType "application/json" `
  -Body '{"usuarioId":1,"total":100}'
```

Evento esperado en Kafka:

```json
{
  "tipoEvento": "orden.creada",
  "ordenId": 1,
  "total": 100.0,
  "estado": "PENDIENTE",
  "origen": "ec-orden-ms",
  "timestamp": 1713350000000
}
```

### Pagos como consumer y producer

```powershell
cd uso-ms-sb/ec-pago-ms
docker compose up -d
.\mvnw.cmd spring-boot:run
```

Verifica que `ec-pago-ms` consuma `orden-eventos`, procese el pago y publique en `pago-eventos`.

## Evidencias

Adjunta:

- captura de `docker compose ps` del entorno Kafka;
- captura de Kafka UI con el topic `orden-eventos`;
- captura del producer y consumer manual;
- captura del producer y consumer en Python;
- salida del `POST /ordenes`;
- evidencia del consumo de `ec-pago-ms` y publicacion en `pago-eventos`.

## Actividad autonoma

Documenta el contrato del evento `orden.creada`.

| Campo | Tipo | Descripcion | Ejemplo |
|---|---|---|---|
| `tipoEvento` | string | Tipo de evento publicado | `orden.creada` |
| `ordenId` | number | Identificador de la orden | `321` |
| `total` | number | Monto de la orden | `180.0` |
| `estado` | string | Estado de la orden | `PENDIENTE` |
| `origen` | string | Aplicacion productora | `ec-orden-ms` |
| `timestamp` | number | Unix timestamp en milisegundos | `1713350000000` |

Incluye tambien el topic, productor, consumidor y estrategia inicial de particionado.
