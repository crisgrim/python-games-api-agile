# python-games-api-agile

## Información
```
Nombre del proyecto: Backend Game API
Descripción: 
Se trata de una API desarrollada con Python y Django para gestionar una red social donde los usuarios pueden hablar sobre videojuegos.
Toda la información relacionada con el proyecto base está incluida en este fichero [README.md](https://github.com/crisgrim/python-games-api/blob/develop/README.md)
Alumna: Cristina Ponce Torres
```

## Instalación

| Alias | URL |
| :-------: | :------: |
| PyCharm |   https://www.jetbrains.com/es-es/pycharm/download/#section=mac| 
| viruatlenv |  https://docs.python.org/es/3/library/venv.html |
| Pg Admin 4 |  https://www.pgadmin.org/download/ |


## Versiones

| Alias | Version |
| :-------: | :------: |
| Python | 3.6   | 
| Django | 3.2.9   | 
| Django Rest Framework | 3.12.4 |
| Psycopg2 (PostgreSQL) | 2.9.2 | 
| Django Rest Auth | 0.9.5 | 
| Django All Auth | 0.46.0 | 
| Django Filter | 21.1 | 


## Línea de comandos

```
Inicializar proyecto          python manage.py runserver
Ejecutar tests                python manage.py test --verbosity 2
Crear migraciones             python manage.py makemigrations
Ejecutar migraciones          python manage.py migrate
```


## Principios SOLID

| Principio | Fichero | Comentarios |
| :-------: | :------: | :------: |
| SRP | [Serializers](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/serializers.py)  |  Como se puede apreciar en este fichero cada serializer sigue el principio de SRP porque cada uno define como será devuelto el modelo en el que se basa. Por ejemplo, GameSerializer, se basa en el modelo Game del que retornará tres campos: 'name', 'created_date' y 'added_by' donde devolverá el usuario que lo ha creado.   |
| SRP | [Models](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/models.py)  |  Como se puede apreciar en este fichero cada modelo sigue el principio de SRP porque cada uno se encarga de definir qué campos contiene y qué relación mantiene con otros modelos de la aplicación.   |
| SRP | [Views](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/views.py)  |  Como se puede apreciar en este fichero cada vista sigue el principio de SRP porque cada una se encarga de definir qué información va a traer de la base de datos en cada uno de los modelos, así como, el campo por el que serán ordenados y en los casos en los que aplica, se incluyen los campos por los que se permite filtrar.  |
| LSP | [Models](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/models.py)   |  Como se puede apreciar en este fichero la clase CustomUser extiende de la clase AbstractUser, cualquier función que reciba como parámetro esta implementación o la AbstractUser, podrá llamar sin comprobación de a qué clase hace referencia a los mismos métodos.  |
| ISP | [Models](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/models.py)   |  Como se puede apreciar en este fichero las clases BelongsTo & CreatedDate tienen ahora un dominio concreto, que las clases que lo requieran pueden implementar.  |
| ISP | [Views](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/views.py)   |  Como se puede apreciar en este fichero la clase Filterable tiene ahora un dominio concreto, que las clases que lo requieran pueden implementar |


## Patrones

| Patrón | Fichero |
| :-------: | :------: |
| Modelos | [Models](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/models.py)
| Vistas (Controladores) | [Views](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/views.py)

(*) Django hace uso del patrón MVT (Modelo, Vista, Plantilla), pero en este proyecto al tratarse de una api que no precisa de un sistema de visualización, he omitido el uso de plantillas, pero sí que he utilizado los modelos para gestionar la comunicación con la base de datos creada con PostgreSQL. Y las vistas a modo de controladores para poder devolver la información como se espera gracias a los serializers.


## Refactors

| Refactor | Fichero | Método | Comentarios |
| :-------: | :------: |:------: | :------: |
| Inline method | [Views](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/views.py) | Game.objects.all().order_by('name')| Al principio pensé que podría hacer un método genérico al que se le pasase la entidad a obtener y el campo por el que se quería ordenar los resultados. Pero luego vi que no aportaba nada y que sería agregar llamadas internamente totalmente innecesarias. Así que, preferí dejar la llamada a la base de datos con inline methods. |
| Extract Superclass | [Models](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/models.py)  | Clases BelongsTo & CreatedDate | He extraído la funcionalidad común de varios de los modelos de mi API en dos nuevas clases con una única responsabilidad. BelongsTo se encarga de agregar el campo que identifica el usuario que ha generado dicho elemento. CreatedDate se encarga de agregar el campo que identifica la fecha en que se ha creado dicho elemento. |
| Extract Superclass | [Views](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/views.py)  | Clase Filterable | He extraído la funcionalidad de filtrar, que era común en la mayoría de las vistas de mi API en una nueva clase que solo se encarga de esa responsabilidad en concreto. |
| Pull Up Field | [Models](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/models.py)  | Clases BelongsTo & CreatedDate | He extraído los campos comunes que tenían los distintos modelos en estas dos clases. |
| Pull Up Field | [Views](https://github.com/crisgrim/python-games-api-agile/blob/develop/gamesite/gameapi/views.py)  | Clase Filterable | He extraído los campos comunes de filtrado que tenían las distintas vistas en una clase extra |


## Notas
```
Cambios realizados en el proyecto base:

- Agregar principios SOLID implementados
- Realizar refactors
- Agregar comentarios en el código
- Agregar tests a modelos y vistas
```
