# ec-pago-ms

Microservicio de pagos con Spring Boot, PostgreSQL y Kafka. Consume eventos desde
`orden-eventos`, procesa un pago simulado y publica el resultado en
`pago-eventos`.

## Servicios

| Servicio | URL/Puerto |
|---|---|
| App | `http://localhost:49031` |
| PostgreSQL | `localhost:49030` |
| Kafka interno Docker | `kafka:9092` |

Contenedores:

- `lambdalab-ec-pago-ms`
- `lambdalab-postgres-ec-pago-ms`

## Requisitos

Levanta primero Kafka para crear la red `lambdalab-kafka-net`:

```powershell
cd ..\..\..\kafka
docker compose up -d
```

## Uso

Para desarrollo local, levanta solo PostgreSQL:

```powershell
docker compose -f compose-dev.yml up -d
```

Luego ejecuta la aplicacion en tu IDE o con Maven usando el perfil `dev`.

Para ejecutar app y PostgreSQL dentro de Docker:

```powershell
docker compose up -d --build
```

Probar endpoint:

```text
GET http://localhost:49031/pagos/saludo
```

Este servicio consume `orden-eventos` y publica `pago-eventos`.
