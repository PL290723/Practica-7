# Práctica 7 - Tópicos Avanzados de Programación

## Descripción
Esta práctica implementa un sistema de inicio de sesión con validación de roles de usuario (administrador, estudiante y maestro), utilizando el patrón de diseño MVP (Model-View-Presenter). Dependiendo del rol del usuario, el sistema redirige a una vista específica.

## Características
- Inicio de sesión con validación de credenciales.
- Soporte para tres roles de usuario:
  - **Administrador**: Accede a la vista principal.
  - **Estudiante**: Accede a una vista exclusiva para estudiantes.
  - **Maestro**: Accede a una vista exclusiva para maestros.
- Navegación entre ventanas utilizando `QStackedWidget`.

## Credenciales de Acceso
El sistema cuenta con los siguientes usuarios predefinidos para pruebas:

| Rol | Usuario | Contraseña |
| --- | --- | --- |
| Administrador | `admin` | `1234` |
| Estudiante | `estudiante` | `1234` |
| Maestro | `maestro` | `1234` |

## Requisitos
- Python 3.x
- PyQt5

## Ejecución
Para iniciar la aplicación, ejecute el siguiente comando en la terminal:

```bash
python app.py
```
