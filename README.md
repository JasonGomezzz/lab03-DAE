# CINESPOILERS - API REST PROFESIONAL 🎬
**Desarrollador:** Jason Gomez Mancha  
**Institución:** Tecsup (Diseño y Desarrollo de Software)

## 🚀 Descripción
Evolución del sistema Cinespoilers a una arquitectura de **API RESTful** utilizando **Django Rest Framework**, permitiendo la gestión completa (CRUD) de la base de datos de películas.

---

## 📡 Evidencias del CRUD (Pruebas de Integración)

| Operación | Método | Endpoint | Resultado |
| :--- | :--- | :--- | :--- |
| **CREATE** | `POST` | `/api/movies/` | ![POST](./docs/api-post.png) |
| **READ ALL** | `GET` | `/api/movies/` | ![GET ALL](./docs/api-get-all.png) |
| **READ ONE** | `GET` | `/api/movies/2/` | ![GET ONE](./docs/api-get-single.png) |
| **UPDATE** | `PATCH`| `/api/movies/1/` | ![PATCH](./docs/api-update.png) |
| **DELETE** | `DELETE`| `/api/movies/2/` | ![DELETE](./docs/api-delete.png) |

### 🖥️ Interfaz Web (Browsable API)
Visualización de los recursos desde el navegador:
![Web View](./docs/api-web-view.png)

### 📊 Logs de Actividad del Servidor
Registro técnico de las peticiones HTTP (200, 201, 204) procesadas en tiempo real:
![Logs](./docs/Server-logs.png)

---

## ⚙️ Instalación y Ejecución
1. Crear ambiente: `python -m venv venv`
2. Activar: `.\venv\Scripts\activate`
3. Instalar: `pip install -r requirements.txt`
4. Correr: `python manage.py runserver`