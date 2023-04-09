# back-PDDD-2023s1

## Integrantes

* Enzo Galarza
* Carlos "Charlie" Cuoco

## Tecnologia

#### Backend: Python/Flask
#### DB: Mongo

## Prueba de Concepto

Se recomienda usar [VirtualEnv](https://virtualenv.pypa.io/en/latest/)
Ejemplo instalacion [VirtualEnv en Python 3.9](https://gist.github.com/barseghyanartur/479b0b4749d7a726167faf834706c852)

Primero instalar dependencias que se encuentran en requeriments.txt con el comando:

```python
        pip install requeriments.txt

```


Para demostrar el funcionamiento ejecutar:

```python
	flask --app backPDD run

```
En modo debug:

```python
	flask --app backPDD run --debug

```


## Variables de entorno

Deben crearse un archivo .env con las siguientes variables de entorno:

```bash
        MONGODB_USER
        MONGODB_PASSWORD
        MONGODB_DATABASE
        MONGODB_PORT
```


## Uso de pre-commit

Para mantener un codigo ordenado y dentro de los estanderes PEP, necesitamos utilizar pre-commit, por lo cual luego de instalar los requeriments, debemos ejecutar:

```bash
        pre-commit install

```

## MongoDB
Se utilizara pymongo para conectar con una db de Mongo, para realizar esto utilizamos la siguiente linea en el `main.py`:
```python
client = MongoClient(
    "localhost",
    int(os.getenv("MONGODB_PORT", 27017)),
    username="nombre_usuario",
    password="password",
)
```
