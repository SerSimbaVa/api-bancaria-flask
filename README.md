# API Bancaria con Flask, MongoDB y Docker
Esta es una API RESTful bancaria desarrollada con **Flask**, **MongoDB** y **Docker**. Permite a los usuarios crear cuentas, actualizar saldos y listar todas las cuentas disponibles.

## Endpoints
"/accounts" GET y POST
"accounts/<account_id>" PATCH

### Crear cuenta
- POST `/accounts`
- Body (JSON):
  ```json
  {
    "name": "Nombre"
    "balance": "Balance inicial $200"
  }

### Actualizar saldo
- PATCH `/accounts/id`
- Body (JSON):
  ```json
  {
    "amount": "Balance inicial $200 +- Balance nuevo $100"
  }

### Listar usuarios
- GET `/accounts`

### Patrones de diseño
1. Separación de responsabilidades
Cada módulo tiene un propósito claro:

router.py: maneja las rutas HTTP (controlador).

services.py: contiene la lógica de negocio.

db.py: gestiona la base de datos.

2. Factory Pattern para la app
Se usa un patrón de factoría para crear la instancia de Flask (create_app()), permitiendo flexibilidad para distintos entornos.

3. Configuración desacoplada con .env
Uso de python-dotenv para manejar variables sensibles como credenciales de base de datos.

4. Patrón de Servicios
La lógica de negocio se encapsula en services.py.
