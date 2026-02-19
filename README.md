# Python

## FASE 1 – Fundamentos Python Backend

### Ejercicio 1 – Modelado básico

- [x] Crear clases:
  - Producto

  - Sucursal

  - Precio

  - Relacionarlas

- [x] Simular carrito y calcular total

> Usar:

    @dataclass

    Tipado (typing)

> Objetivo: entender modelado estilo backend en Python.

### Ejercicio 2 – Async real

- [x] Hacer 10 requests en paralelo con httpx.AsyncClient

- [x] Medir tiempo total

- [x] Comparar con versión sin async

> Objetivo: entender async/await y concurrencia.

```
1. No hay una carga tan alta de requests. Como los métodos async buscan matar los tiempos muertos, si no hay una alta demanda de solicitudes (concurrencia), no tiene sentido utilizar método asíncrono.
2. Las tareas están vinculadas a la CPU y no a la red, vos mismo lo dijiste. El I/O (In y Out) son las operacioens de entrada y salida de recursos externos. Si las tareas están dentro de la misma CPU, hay entrada y salidad de memoria, disco, etc. Todo ocurre adentro.
3. Las solicitudes son individuales async no muestran gran diferencia de tiempo cuando las tareas en simultáneo del CPU se ejecutan. COn async duele menos la espera.

```

## FASE 2 – FastAPI básico

### Ejercicio 3 – CRUD en memoria

- [x] Crear API con:
  - GET /product

  - GET /product/{id}

  - POST /product

  - PUT /product/{id}

  - DELETE /product/{id}

> Sin base de datos

> Objetivo: entender routing, validación, models y Swagger automático

### Ejercicio 4 – Filtro por query param

- [x] GET /product?region=manhattan

- [x] Filtrar resultados

> Objetivo: simular caso real de región/sucursal.

## FASE 3 – Base de datos real

### Ejercicio 5 – PostgreSQL + SQLAlchemy

- [x] Crear modelos:

- [x] Producto

- [x] Sucursal

- [x] Precio (con timestamp)

- [-] Insert / Select / Update

- [-] Integrarlo a FastAPI

> Objetivo: ORM real y manejo de sesiones.
> Nuevo: tratar de nromalizar la bdd.

## FASE 4 – Simulación de scraping

### Ejercicio 6 – Consumir API externa

- [ ] Consumir API pública (ej: FakeStoreAPI)

- [ ] Transformar datos

- [ ] Guardarlos en DB

- [ ] Exponerlos vía FastAPI

> Objetivo: pipeline completo fetch → persist → exponer

## FASE 5 – Background jobs

### Ejercicio 7 – Tarea en segundo plano

- [ ] Crear endpoint /trigger-update

- [ ] Ejecutar tarea en background

- [ ] Luego automatizar con APScheduler

> Objetivo: entender workers y tareas programadas.

## FASE 6 – Manejo de sesión HTTP

### Ejercicio 8 – Simular login y sesión persistente

- [ ] Usar httpx.Client

- [ ] Manejar cookies

- [ ] Reutilizar sesión

- [ ] Enviar headers personalizados

## Bonus – Mini proyecto intermedio

- Hacer un “mini agregador” que:
  - Scrapee una API pública

  - Guarde precios históricos

  - Permita ver evolución

  - Calcule variación porcentual
