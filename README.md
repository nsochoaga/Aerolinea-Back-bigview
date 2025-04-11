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

## ▶️ Instalación y ejecución

```bash
# 1. Clona el repositorio
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo

# 2. Crea entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta migraciones
python manage.py migrate

# 5. Crea superusuario
python manage.py createsuperuser

# 6. Corre el servidor
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

## 🔍 Acceso a la API

Documentación Swagger: http://localhost:8000/docs/ (swagger)

Documentación Redoc: http://localhost:8000/redoc/

## 🧪 Ejecutar pruebas

Este proyecto incluye pruebas para los endpoints principales de vuelos y reservas.

```bash
python manage.py test
```

Esto ejecutará los tests en reservas/tests/ para verificar que la API funcione correctamente.

## 🧪 Ejemplos de uso de la API

### 📥 Obtener todos los vuelos disponibles

```bash
GET /vuelos/
```

Filtro por origen, destino y fecha:

```bash
GET /vuelos/?origen=Bogotá&destino=Medellín&fecha=2025-04-15
```

## 🔒 Autenticación (JWT)

### Login:

```bash
POST /auth/token/
{
  "username": "usuario",
  "password": "contraseña"
}
```

Respuesta:

```bash
json
{
  "refresh": "refreshtoken",
  "access": "TOKEN_JWT"
}
```

### 📝 Crear una reserva

```bash
POST /reservas/
Authorization: Bearer TOKEN_JWT
Content-Type: application/json

{
  "vueloId": 1
}
```

### 📄 Ver reservas propias

```bash
GET /reservas/
Authorization: Bearer TOKEN_JWT
```

### ❌ Cancelar una reserva

```bash
DELETE /reservas/{id}/
Authorization: Bearer TOKEN_JWT
```

## 📂 Estructura del proyecto

```bash
reservas/
├── fixtures/                 # Datos iniciales en JSON
├── migrations/
├── models.py                 # Modelos: Vuelo, Reserva
├── serializers.py
├── views.py
├── urls.py
├── tests.py     # Pruebas unitarias
```
