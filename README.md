# 🎬 CINESPOILERS - API RESTFUL PROFESIONAL
**Desarrollador:** Jason Gomez Mancha  
**Especialidad:** Diseño y Desarrollo de Software (Tecsup)

---

## 📡 Fase 2: Documentación de la API (Actual)
Evolución a servicios web con **Django Rest Framework**. A continuación, se detalla la estructura y el ciclo CRUD verificado.

### 🌐 Interfaz Navegable (Browsable API)
La API cuenta con una interfaz web autogenerada para facilitar la inspección de recursos.
* **API Root:** Punto de entrada principal.
    ![API Root](./docs/api-root.png)
* **API Movie List:** Vista de lista desde el navegador.
    ![API List Web](./docs/api-list.png)

---

### 📊 Tabla de Operaciones CRUD (Thunder Client)
| Operación | Método | Endpoint | Evidencia Visual |
| :--- | :---: | :--- | :--- |
| **CREATE** | `POST` | `/api/movies/` | ![POST](./docs/api-post.png) |
| **READ ALL** | `GET` | `/api/movies/` | ![GET ALL](./docs/api-get-all.png) |
| **READ ONE** | `GET` | `/api/movies/2/` | ![GET ONE](./docs/api-get-single.png) |
| **UPDATE** | `PATCH`| `/api/movies/1/` | ![PATCH](./docs/api-update.png) |
| **DELETE** | `DELETE`| `/api/movies/2/` | ![DELETE](./docs/api-delete.png) |

---

### 🖥️ Registro Técnico y Logs
Evidencia de las peticiones procesadas (Status 200, 201 y 204) en la terminal del servidor.
![Logs](./docs/Server-logs.png)

---

## 🏗️ Fase 1: Estructura y Base del Proyecto
Historial de la construcción inicial del entorno y administración.

### 1. Preparación del Entorno
![Repositorio](./docs/o1-repository.png)
![Ambiente](./docs/o2-environment.png)

### 2. Levantamiento y Admin
![Servidor](./docs/o3-run.png)
![Admin](./docs/o4-admin.png)

---

## 🚀 Guía de Instalación Rápida
```bash
# 1. Activar entorno virtual
.\venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Correr el servidor
python manage.py runserver