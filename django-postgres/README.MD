# Inicio de un proyecto Django - Postgres

## Componentes del proyecto

Crear los siguientes archivos:

- `requirements.txt` con los paquetes necesarios para la ejecución del proyecto.
- `Dockerfile` con la imagen de python para la creación del proyecto.
- `compose-yaml` para ejecutar los contenedores de `python` y `postgres`.

## Creación del proyecto

Una vez creados el Dockerfile y el Compose, ejecutar los siguientes comandos:

1. Crear el proyecto Django.

    ```s
    sudo docker-compose run --rm web django-admin startproject PROJECT_NAME .
    ```

2. Listar el contenido del proyecto

    ```s
    drwxr-xr-x 2 root root 4096 Dec  5 20:06 my_project
    drwxr-xr-x 3 root root 4096 Dec  5 18:08 data
    -rw-rw-r-- 1 user user  492 Dec  5 20:15 docker-compose.yaml
    -rw-rw-r-- 1 user user  342 Dec  5 20:39 Dockerfile
    -rwxr-xr-x 1 root root  663 Dec  5 20:06 manage.py
    -rw-rw-r-- 1 user user  119 Dec  5 18:31 requirements.txt
    ```

    Debido a que el contenedor correo como usuario root, los archivos creados con `django-admin` son propiedad del mismo. Se debe cambiar el dueño de estos archivos al usuario del sistema.
    La carpeta `data` debe ser propiedad del usuario `root` para que al ejecutar el contenedor de postgres no genere problemas.

    ```s
    sudo chown -R $USER:$USER my_project manage.py
    ```

## Conexión a la Base de Datos

1. Editar el `settings.py` del proyecto

    ```py
    # settings.py

    import os
    
    ...

    ALLOWED_HOSTS = ['*']
    ...

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
        }
    }
    ```

## Ejecución del proyecto

1. Ubicado en la raíz del proyecto ejecuta:
    
    ```s
    docker-compose up
    ```

2. Para crear una app dentro del proyecto ejecuta:

    ```s
    sudo docker-compose run --rm web python3 manage.py startapp my_app
    ```

    No olvidar que la app se creará y el usuario root será el dueño de esa carpeta y su contenido. Cambiar el dueño al usuario del sistema.


# Algunos comandos

- Ejecutar compose de un archivo específico
    ```s
    docker-compose -f ARCHIVO.yaml ...
    ```
    Se puede añadir:
    - `build`
    - `run SERVICE → para ejecutar un servicio específico`
    - `up`
    - `ps`

- Entrar al contenedor de la DB en modo interactivo
    ```s
    docker exec -it CONTAINER_NAME bash
    ```

- Ingresar a la consola de Postgres
    ```s
    psql -U USER -d DATABASE --password
    ```
    El usuario por defecto es postgres si no se especifica

- Comandos administrativos de Django
    ```s
    docker-compose run --rm DJANGO_SERVICE COMMAND
    ```
    - `python3 manage.py createsuperuser`
    - `python3 manage.py shell`
    - `python3 manage.py startapp my_app`