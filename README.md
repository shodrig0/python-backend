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

- [x] Insert / Select / Update

- [x] Integrarlo a FastAPI

> Objetivo: ORM real y manejo de sesiones.

> Nuevo: tratar de normalizar la bdd.

> Aclaración: Si bien faltan algunos métodos http como en los services, los más importantes (para aprender fastapi y sqlalchemy) están hechos. En los siguientes ejercicios se irán a ir agregando.

## FASE 4 – Simulación de scraping

### Ejercicio 6 – Consumir API externa

- [x] Consumir API pública (ej: FakeStoreAPI)

- [x] Transformar datos

- [x] Guardarlos en DB

- [x] Exponerlos vía FastAPI

> Objetivo: pipeline completo fetch → persist → exponer

#### GET

<img src="https://live.staticflickr.com/65535/55140034457_61c8988da7_b.jpg" width="1200" alt="api yaak"/>

#### DB

<img src="https://live.staticflickr.com/65535/55141099013_d8868f7661_z.jpg" width="620" alt="db pg"/></a>

## FASE 5 – Background jobs

### Ejercicio 7 – Tarea en segundo plano

- [x] Crear endpoint /trigger-update

- [x] Ejecutar tarea en background

- [x] Luego automatizar con APScheduler

> Objetivo: entender workers y tareas programadas.

> Para no hacer copy/paste del pipeline del ejercicio anterior, el ejercicio 7 se integró en el mismo directorio que el 6.

## FASE 6 – Manejo de sesión HTTP

### Ejercicio 8 – Simular login y sesión persistente

- [x] Usar httpx.Client

- [x] Manejar cookies

- [x] Reutilizar sesión

- [x] Enviar headers personalizados

> Para no hacer copy/paste del pipeline del ejercicio 6, el ejercicio 8 se integró en el mismo directorio, al igual que el 7.

## Bonus – Mini proyecto intermedio

- Hacer un “mini agregador” que:
  - Scrapee una API pública

  - Guarde precios históricos

  - Permita ver evolución

  - Calcule variación porcentual
