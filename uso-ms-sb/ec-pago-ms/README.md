# ec-pago-ms

Microservicio de pagos con Spring Boot, MySQL y Kafka. Consume eventos desde
`orden-eventos`, procesa un pago simulado y publica el resultado en
`pago-eventos`.

## Servicios

| Servicio | URL/Puerto |
|---|---|
| App | `http://localhost:49031` |
| MySQL | `localhost:49030` |
| Kafka interno Docker | `kafka:9092` |

Contenedores:

- `lambdalab-ec-pago-ms`
- `lambdalab-mysql-ec-pago-ms`

## Requisitos

Levanta primero Kafka para crear la red `lambdalab-kafka-net`:

```powershell
cd ..\..\..\kafka
docker compose up -d
```

## Uso

Desde esta carpeta:

```powershell
docker compose up -d --build
```

Probar endpoint:

```text
GET http://localhost:49031/pagos/saludo
```

Este servicio consume `orden-eventos` y publica `pago-eventos`.
