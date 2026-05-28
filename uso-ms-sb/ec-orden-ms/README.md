# ec-orden-ms

Microservicio de ordenes con Spring Boot, MySQL y Kafka.

## Servicios

| Servicio | URL/Puerto |
|---|---|
| App | `http://localhost:49021` |
| MySQL | `localhost:49020` |
| Kafka interno Docker | `kafka:9092` |

Contenedores:

- `lambdalab-ec-orden-ms`
- `lambdalab-mysql-ec-orden-ms`

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
