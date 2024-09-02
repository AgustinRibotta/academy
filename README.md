# Academia Online

Este es el repositorio de un proyecto de Academia Online, una plataforma desarrollada con Python y Django donde los usuarios pueden registrarse, navegar por los cursos disponibles, inscribirse en ellos y acceder a información sobre las clases. Los administradores tienen la capacidad de cargar y gestionar cursos, así como de asignar información sobre las clases.

## Funcionalidades

### Usuarios

1. **Registro e inicio de sesión**: 
   - Los usuarios pueden registrarse con un nombre de usuario, correo electrónico y contraseña.
   - Los usuarios registrados pueden iniciar sesión en la plataforma.

2. **Navegación de cursos**:
   - Los usuarios pueden ver una lista de cursos disponibles.
   - Pueden filtrar y buscar cursos según diferentes criterios como categoría, nivel, y modalidad (presencial o virtual).

3. **Inscripción en cursos**:
   - Los usuarios pueden inscribirse en los cursos de su interés.
   - Pueden ver los cursos en los que están inscritos desde su perfil.

4. **Perfil de usuario**:
   - Los usuarios pueden actualizar su información de perfil.
   - Pueden ver el historial de cursos en los que han participado.

### Administradores

1. **Gestión de cursos**:
   - Los administradores pueden añadir nuevos cursos, incluyendo el nombre del curso, descripción, categoría, nivel, y duración.
   - Pueden editar o eliminar cursos existentes.

2. **Gestión de clases**:
   - Los administradores pueden asignar fechas y horarios a las clases de cada curso.
   - Pueden definir si las clases son presenciales (incluyendo la dirección) o virtuales (incluyendo el enlace de la clase).

3. **Gestión de usuarios**:
   - Los administradores pueden ver la lista de usuarios registrados.
   - Pueden gestionar el acceso de los usuarios y actualizarlos a roles administrativos si es necesario.

## Tecnologías Utilizadas

- **Backend**: [Django](https://www.djangoproject.com/) (Python)
- **Frontend**: HTML5, CSS3, [Bootstrap](https://getbootstrap.com/), JavaScript
- **Base de Datos**: [SQLite](https://www.sqlite.org/index.html) (por defecto) o cualquier base de datos compatible con Django
- **Autenticación**: Sistema de autenticación de Django
- **Estilos**: [Bootstrap](https://getbootstrap.com/) y CSS personalizado

## Instalación y Configuración

Sigue los siguientes pasos para instalar y ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/academia-online.git
   cd academia
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**:

   Crea un archivo `.env` en la carpeta raíz del proyecto y define las siguientes variables:
   ```plaintext
   SECRET_KEY=<Tu clave secreta de Django>
   DEBUG=True  # Cambiar a False en producción
   ALLOWED_HOSTS=localhost, 127.0.0.1
   ```

5. **Realizar migraciones de la base de datos**:
   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario** (para acceder al panel de administración de Django):
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar la aplicación**:
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**:

   Una vez iniciado el servidor, puedes acceder a la aplicación en tu navegador web en `http://localhost:8000`.



## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna idea o encuentras un problema, por favor abre un issue o envía un pull request. Asegúrate de seguir las buenas prácticas de desarrollo y de documentar adecuadamente tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.


