# DAE - Lab01: Introducción a Django

## Descripción

En este laboratorio desarrollé una primera aplicación web utilizando Django, organizando el proyecto mediante una configuración principal y una aplicación llamada `semana1`.

La página presenta los principales contenidos de la Semana 1 del curso, como la introducción a las aplicaciones empresariales, sus objetivos, tipos de sistemas, arquitectura empresarial, ciclo de desarrollo, herramientas, sistema de evaluación y bibliografía.

## Estructura del proyecto

El proyecto contiene principalmente:

- `config/`: contiene la configuración principal del proyecto Django.
- `semana1/`: contiene la aplicación desarrollada para la Semana 1.
- `manage.py`: permite ejecutar los comandos principales del proyecto.
- `requirements.txt`: contiene las dependencias utilizadas.
- `README.md`: contiene la descripción y documentación del proyecto.

## Desarrollo realizado

### Configuración del proyecto

Se creó el proyecto utilizando Django y se organizó la configuración principal dentro de `config`.

La aplicación `semana1` fue registrada en `INSTALLED_APPS` para que Django pueda reconocerla como parte del proyecto.

### Rutas

Se configuraron las rutas de la aplicación `semana1` y se enlazaron con las rutas principales del proyecto mediante `include()`.

Esto permite mantener las rutas de la aplicación separadas de la configuración principal y tener una mejor organización.

### Vista y plantilla

Se creó una vista para mostrar la página principal de la Semana 1 mediante la plantilla `inicio.html`.

En esta página se presenta información introductoria del curso, incluyendo los objetivos de la semana, contenidos principales, tipos de sistemas empresariales, arquitectura empresarial, ciclo de desarrollo, herramientas del curso, sistema de evaluación y bibliografía.

## Dependencias

Las dependencias utilizadas se encuentran registradas en el archivo `requirements.txt`.

Este archivo fue generado mediante:

```bash
pip freeze > requirements.txt
```

Entre las dependencias utilizadas se encuentra Django 6.1.

## Instalación y ejecución

1. Crear un entorno virtual:

```bash
python -m venv .venv
```

2. Activar el entorno virtual en Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar el servidor:

```bash
python manage.py runserver
```

5. Abrir la aplicación en el navegador:

```text
http://127.0.0.1:8000/
```

## Tecnologías utilizadas

- Python
- Django
- HTML
- Git
- GitHub

## Capturas del funcionamiento

### Pantalla principal

Vista principal de la Semana 1 donde se muestra la introducción y los objetivos del curso.

<img width="1376" height="908" alt="image" src="https://github.com/user-attachments/assets/dc7d2ccb-16b5-4a50-aae9-2ebe4ac36b8e" />

### Contenidos de la Semana 1

Sección donde se muestran los principales contenidos y conceptos trabajados durante la primera semana.


<img width="1395" height="897" alt="image" src="https://github.com/user-attachments/assets/e51cb9b5-ba00-47c5-a4e4-3c055e9d772f" />

### Sistema de evaluación y bibliografía

Sección final de la página donde se muestra el sistema de evaluación y la bibliografía recomendada.


<img width="1352" height="907" alt="image" src="https://github.com/user-attachments/assets/b45c0dbc-c5eb-4e49-87d9-14b2d22487c1" />

## Observaciones

Durante el desarrollo pude organizar el proyecto separando la configuración principal de la aplicación `semana1`, permitiendo mantener una estructura más ordenada.

También se configuraron las rutas mediante `include()`, permitiendo que la aplicación tenga sus propias rutas sin colocar toda la configuración directamente en el proyecto principal.

Finalmente, las dependencias utilizadas quedaron registradas en `requirements.txt`, permitiendo conocer los paquetes necesarios para volver a ejecutar el proyecto.

## Conclusiones

1. Aprendí a crear y organizar un proyecto en Django utilizando una configuración principal y una aplicación separada, esto me permitió entender mejor cómo se distribuyen los archivos dentro de un proyecto.

2. Comprendí la importancia de registrar una aplicación en `INSTALLED_APPS` y configurar sus rutas, ya que esto permite que Django reconozca la aplicación y pueda mostrar su contenido en el navegador.

3. Pude aprender cómo utilizar una vista y una plantilla HTML para mostrar información desde una aplicación Django, entendiendo mejor cómo se conectan estas partes para obtener un resultado en la página web.

4. Comprendí la importancia de utilizar un entorno virtual y registrar las dependencias en `requirements.txt`, ya que permite mantener organizado el proyecto y facilita volver a instalar lo necesario para ejecutarlo.
