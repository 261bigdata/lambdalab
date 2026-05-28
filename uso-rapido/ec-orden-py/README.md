# ec-orden-py

Caso de uso rapido en Python para probar Kafka con un producer y un consumer
simples.

## Requisitos

Levanta primero Kafka:

```powershell
cd ..\..\kafka
docker compose up -d
```

El contenedor se conecta a:

- broker interno: `kafka:9092`
- red Docker: `lambdalab-kafka-net`

## Uso

Desde esta carpeta:

```powershell
docker compose up -d --build
```

Entrar al contenedor:

```powershell
docker compose exec ec-orden-py sh
```

Ejecutar producer:

```bash
python /app/producer_ordenes.py
```

Ejecutar consumer en otra terminal:

```powershell
docker compose exec ec-orden-py python /app/consumer_ordenes.py
```

Contenedor:

```text
lambdalab-ec-orden-py
```
