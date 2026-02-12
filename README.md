# Python

## FASE 1 – Fundamentos Python Backend

### Ejercicio 1 – Modelado básico

- [x] Crear clases:
  - Producto

  - Sucursal

  - Precio

  - Relacionarlas

- [parcial] Simular carrito y calcular total

> Usar:

    @dataclass

    Tipado (typing)

> Objetivo: entender modelado estilo backend en Python.

### Ejercicio 2 – Async real

- [ ] Hacer 10 requests en paralelo con httpx.AsyncClient

- [ ] Medir tiempo total

- [ ] Comparar con versión sin async

> Objetivo: entender async/await y concurrencia.

## FASE 2 – FastAPI básico

### Ejercicio 3 – CRUD en memoria

- [ ] Crear API con:
  - GET /productos

  - GET /productos/{id}

  - POST /productos

  - DELETE /productos/{id}

> Sin base de datos

> Objetivo: entender routing, validación, models y Swagger automático

### Ejercicio 4 – Filtro por query param

- [ ] GET /productos?region=manhattan

- [ ] Filtrar resultados

> Objetivo: simular caso real de región/sucursal.

## FASE 3 – Base de datos real

### Ejercicio 5 – PostgreSQL + SQLAlchemy

- [ ] Crear modelos:

- [ ] Producto

- [ ] Sucursal

- [ ] Precio (con timestamp)

- [ ] Insert / Select / Update

- [ ] Integrarlo a FastAPI

> Objetivo: ORM real y manejo de sesiones.

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
