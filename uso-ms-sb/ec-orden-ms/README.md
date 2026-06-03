# ec-orden-ms

Microservicio de ordenes con Spring Boot, PostgreSQL y Kafka.

## Servicios

| Servicio | URL/Puerto |
|---|---|
| App | `http://localhost:49021` |
| PostgreSQL | `localhost:49020` |
| Kafka interno Docker | `kafka:9092` |

Contenedores:

- `lambdalab-ec-orden-ms`
- `lambdalab-postgres-ec-orden-ms`

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

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://localhost:49021/ordenes" `
  -ContentType "application/json" `
  -Body '{"usuarioId":1,"total":100}'
```

Swagger:

```text
http://localhost:49021/swagger-ui/index.html
```

Este servicio publica eventos en el topic `orden-eventos`.
