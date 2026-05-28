# Observabilidad

Stack de observabilidad para LambdaLab con Prometheus y Grafana.

## Servicios

| Servicio | URL/Puerto |
|---|---|
| Prometheus | `http://localhost:49090` |
| Grafana | `http://localhost:43000` |

Credenciales de Grafana:

```text
admin / admin
```

## Uso

Primero levanta Kafka para crear la red `lambdalab-kafka-net`:

```powershell
cd ../kafka
docker compose up -d
```

Luego levanta observabilidad:

```powershell
cd ../obs
docker compose up -d
```

Loki y Promtail quedan preparados en `compose.yml`, pero comentados por ahora.
