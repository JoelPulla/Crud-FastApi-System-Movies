# **Gestión de Películas - FastAPI - SqlAlchemy**

## **Descripción del Proyecto**

Este proyecto es una API para la gestión de películas y categorías, desarrollada con **FastAPI** y **SQLAlchemy**. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para películas y categorías, y filtrar películas según sus categorías, Estare agregando un modulo basico de canles por categorias

## **Tecnologías Utilizadas**

- **Python 3.10+**
- **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python.
- **SQLAlchemy**: ORM (Object-Relational Mapper) para trabajar con bases de datos relacionales en Python.
- **Pydantic**: Para validación de datos y creación de esquemas basados en modelos.
- **SQLite**: Base de datos relacional utilizada en desarrollo (puede ser reemplazada por otra en producción).

## **Instalación y Configuración**

1. **Clonar el Repositorio**:

    ```bash
    git clone https://github.com/JoelPulla/FastApi---SqlAlchemy.git
    ```

2. **Crear un Entorno Virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. **Instalar las Dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Crear la Base de Datos**:

    ```bash
    python -c 'from config.db import Base, engine; Base.metadata.create_all(bind=engine)'
    ```

5. **Iniciar el Servidor de Desarrollo**:

    ```bash
    uvicorn main:app --reload --port 'aqui el puerto que prefieras por ejemplo 5000'
    ```

6. **Documentación de la API**:

    - La documentación automática generada por FastAPI está disponible en: `http://127.0.0.1:5000/docs`.

## **Estructura del Proyecto**

```plaintext
.
│   ├── main.py                # Punto de entrada de la aplicación FastAPI
│   ├── models
|   |   ├── movie
|   |      ├── movie_category_model.py # Definición de los modelos SQLAlchemy
│   ├── schema
|   |   ├── movie
|   |      ├── movie_category_schema.py # Definición de los modelos Pydantic             # Definición de los esquemas de Pydantic
│   ├── database.py            # Configuración de la base de datos y sesión
│   ├── routers                # Directorio con los diferentes enrutadores (endpoints)
│   │   └── movie.py           # Endpoints para la gestión de películas
│   │   └── categorie_movie.py # Endpoints para la gestión de categorías
|   |   └── tv.py              # Endpoints para la gestión de categorías
│   └── __init__.py            # Archivo de inicialización del paquete
├── requirements.txt           # Lista de dependencias del proyecto
└── README.md                  # Documentación del proyecto

```
## ** Base de datos**

```BDD
+--------------------+          +-------------------+          +----------------------+
|      movie         |          |    movie_category |          |      category         |
+--------------------+          +-------------------+          +----------------------+
| id (PK)            |<---------| movie_id (FK)     |          | id (PK)              |
| movie_title        |          | category_id (FK)  |--------->| name                 |
| overview           |          +-------------------+          | is_active            |
| id_tmdb            |                                          | created_at           |
| url_video          |                                          | posther_path         |
| is_youtube         |                                          +----------------------+
| poster_path        |
| background_path    |
| voute_range        |
| popularity         |
| created_at         |
| release            |
+--------------------+
                  # Documentación del proyecto

```
