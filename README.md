# Instrucciones para Ejecutar el Dashboard de Empleados

Antes de comenzar, asegúrate de tener instalado:

- Python 3.x
- MySQL (puedes usar XAMPP)

## Pasos para Ejecutar el Proyecto

1. **Crea una base de datos**:
   - Abre tu entorno de MySQL y crea una nueva base de datos a la que te puedas conectar.

   ```sql
   CREATE DATABASE nombre_de_tu_base_de_datos;
   ```

2. **Clona el repositorio**:

   Clona el repositorio del proyecto:

   ```bash
   git clone https://github.com/smenaquispe/prueba-tecnica-dashboard
   cd prueba-tecnica-dashboard
   ```

3. **Configura el archivo `.env`**:
   - Crea un archivo llamado `.env` en la raíz del proyecto y agrega la siguiente información:

   ```plaintext
   DB_HOST=localhost
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_NAME=nombre_de_tu_base_de_datos
   ```

   Asegúrate de reemplazar `tu_usuario`, `tu_contraseña`, y `nombre_de_tu_base_de_datos` con tus propios valores.

4. **Instala las dependencias**:

   Instala los paquetes necesarios desde el archivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta la aplicación**:

   Finalmente, ejecuta el archivo `app.py`:

   ```bash
   python app.py
   ```

   La aplicación estará disponible en `http://127.0.0.1:5000/` (puedes abrirlo en tu navegador).

