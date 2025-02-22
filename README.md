# Twitter Clone API

Este proyecto es un ejercicio educativo que simula una API parecida y simple de Twitter. Utilizando tecnologias para la parte del server como FastAPI, para la base de datos Postgress y ORM SQLModel, para poder ejecutarlo sin problemas Docker.

## Requisitos

- Docker
- Docker Compose

## Estructura de carpetas

Esto es una vista general de como se organizaron los archivos del proyecto, en donde se organizaron por funcionalidad.

```Markdown
.
├── docker-compose.yml  
├── Dockerfile  
├── README.md  
├── .env
├── requirements.txt  
├── src/ 
│   ├── main.py  
│   ├── crud/  
│   │   ├── profile_photo.py   
│   │   ├── user.py 
│   │   └── ... 
│   ├── database/  
│   │   ├── connection.py  
│   │   ├── config.py 
│   │   └── ...  
│   ├── models/
│   │   ├── models.py  
│   │   ├── user.py 
│   │   └── ...  
│   ├── routers/  
│   │   ├── auth.py  
│   │   ├── user.py 
│   │   └── ...  
│   ├── schemas/  
│   │   ├── user.py 
│   │   ├── tweet.py  
│   │   └── ...  
│   └── utils/  
│       ├── auth.py  
│       ├── security.py 
│       └── ...  
└── static/  
    └── ProfilePhoto/  
        ├── image1.jpg
        ├── image2.jpg  
        └── ... 
```


## Configuración del entorno

1. Clona el repositorio:

    ```sh
    git clone https://github.com/AC-Santiago/TwitterCloneAPI.git
    cd TwitterCloneAPI
    ```

2. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

    ```env
    DB_HOST=twitter_clone_db
    DB_PORT=5432
    DB_NAME=twitter_clone
    DB_USERNAME=tu_usuario
    DB_PASSWORD=tu_contraseña

    ALGORITHM=HS256
    SECRET_KEY=tu_secreto
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

## Levantar los contenedores

1. Construye y levanta los contenedores con Docker Compose:

    ```sh
    docker-compose up --build
    ```

2. La API estará disponible en `http://localhost:5000`.

## Endpoints

Puedes explorar los endpoints disponibles utilizando la documentación interactiva de Swagger en `http://localhost:5000/docs`.

## Notas

Las parte grafica (frontend), fue realizado usando el lenguage de programacion kotlin usando el framework de JetPack Compose, siendo para app moviles en general, este se encuentra en el repositorio:

```sh
git clone https://github.com/Sebastianmjk/TwitterCloneUI.git
```