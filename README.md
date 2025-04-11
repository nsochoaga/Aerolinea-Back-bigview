# ✈️ Sistema de Reservas de Aerolínea

Este proyecto es una API RESTful para gestionar reservas de vuelos, desarrollada con Django y Django REST Framework.

## 🚀 Funcionalidades

- Buscar vuelos por origen, destino y fecha
- Crear reservas (usuarios autenticados)
- Consultar y cancelar reservas propias
- Autenticación con JWT
- Documentación automática con Swagger y ReDoc
- Pruebas unitarias para endpoints clave

## 🛠️ Tecnologías

- Python 3.12.7
- Django
- Django REST Framework
- SimpleJWT
- SQLite (puedes cambiar fácilmente a PostgreSQL)
- drf-spectacular (Swagger)

## ▶️ Cómo ejecutar

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## ▶️ Cómo agregar datos de prueba:

Con el comando:

```bash
python manage.py loaddata reservas/fixtures/reservas_iniciales.json
```

Se agregan datos previamente preparados.

Si se desean agregar nuevos datos manualmente:

```bash
python manage.py createsuperuser
```

ingresar a la ruta:

- http://localhost:8000/admin/

Con credenciales de superusuario y agregar manualmente.
