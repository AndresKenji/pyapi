# pyapi
Single fastapi app 

Esta API, creada con FastAPI, muestra una página web con un mensaje de bienvenida y la fecha y hora actuales

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn
- Jinja2

## Instalación

1. Clona este repositorio:
    ```bash
    git clone git@github.com:AndresKenji/pyapi.git
    cd pyapi
    ```

2. Crea un entorno virtual (opcional, pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    uvicorn main:app --reload
    ```

Abre tu navegador y navega a `http://localhost:8000`. Deberías ver una página con un mensaje de bienvenida y la fecha y hora actuales.

## Uso en docker

Si cuentas con Doker instalado puedes ejecutarlo de la siguiente manera:

1. Construye la app en doker:
```bash
docker build -t apipy .
```

2. Ejecuta una instancia de la app:
```bash
docker run -p 80:80 apipy
```

Abre tu navegador y navega a `http://localhost:8000`. Deberías ver una página con un mensaje de bienvenida y la fecha y hora actuales.

## Documentación

FastAPI genera automáticamente documentación interactiva la cual puede ser consultada en las siguientes rutas:

- Documentación Swagger: `http://localhost:8000/docs`
- Documentación Redoc: `http://localhost:8000/redoc`
