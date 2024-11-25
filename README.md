# Proyecto Backend y Frontend

Este proyecto contiene tanto el backend como el frontend de una aplicación. A continuación se detallan las instrucciones para iniciar y ejecutar ambas partes de la aplicación de manera local.

## Requisitos Previos

Antes de comenzar, hay que  tener los siguientes requisitos instalados en la máquina:

- **Python** >= 3.8 (para el backend)
- **Node.js** >= 14.0.0 (para el frontend)
- **Redis** (para Celery)
- **npm** o **yarn** (para instalar dependencias de Node.js)

## Backend (Django)

El backend está construido con **Django** y **Django REST Framework**. Sigue estos pasos para configurar y ejecutar el backend.

### Pasos para iniciar el backend

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Johanberrio/Prueba_tecnica_Lamba.git
   cd tu_repositorio/backend
   ```


2. **Crear un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   ```


3. **Activar el entorno virtual** :

   * En Linux/Mac:
   
   ```
   source venv/bin/activate
   ```

* En Windows:

   ```
   .\venv\Scripts\activate
   
   ```


4. **Instalar las dependencias del backend** :

   ```
       pip install -r requirements.txt
   ```

5. **Configurar la base de datos** :
    
    Django utiliza **SQLite** por defecto. Si prefieres usar otra base de datos, modifica el archivo `settings.py` para configurarla.

    Para usar SQLite, ejecutar las migraciones de la base de datos:

   ```
   python manage.py migrate 
   ```

6. **Iniciar el servidor de desarrollo** :

   ```
       python manage.py runserver
   ```

El backend debería estar corriendo en `http://127.0.0.1:8000/`.

7. **Configurar Redis para Celery:**
   Para iniciar Redis en la máquina local, ejecutar:

   ```
   redis-server

   ```

Luego, en otro terminal, ejecutar Celery:

   ```
   celery -A backend worker --loglevel=info
   
   ```


## Frontend (React)

El frontend está construido con **React** y utiliza **Axios** para interactuar con el backend. Seguirestos pasos para iniciar el frontend.

### Pasos para iniciar el frontend

1. **Acceder a la carpeta del frontend** :

   ```
   cd ../frontend
   
   ```

2. **Instalar las dependencias del frontend**:

   ```
   npm install
   
   ```

3. **Inicia el servidor de desarrollo**:

   ```
   npm start
   
   ```
## Configuración de CORS
   Para permitir que el frontend (en http://localhost:3000) interactúe con el backend (en http://localhost:8000), se ha configurado el middleware de CORS en el archivo settings.py del     backend. Si es necesario, puedes añadir más dominios permitidos en la lista CORS_ALLOWED_ORIGINS.

## Rutas API

### Registro de Usuario

* **POST /register/** : Registra un nuevo usuario con los datos proporcionados (username, password, name, etc.).
* **POST /login/** : Inicia sesión con las credenciales del usuario generando un Token de inicio de sesión.
* **POST /logout/** : Cierra sesión con las credenciales del usuario.
