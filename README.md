# pyapi
Single fastapi app 

Esta API, creada con FastAPI, muestra una página web con un mensaje de bienvenida y la fecha y hora actuales

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual (opcional, pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install fastapi uvicorn
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    uvicorn main:app --reload
    ```

2. Abre tu navegador y navega a `http://localhost:8000`. Deberías ver una página con un mensaje de bienvenida y la fecha y hora actuales.

## Documentación

FastAPI genera automáticamente documentación interactiva para tu API. Puedes acceder a la documentación en las siguientes rutas:

- Documentación Swagger: `http://localhost:8000/docs`
- Documentación Redoc: `http://localhost:8000/redoc`
