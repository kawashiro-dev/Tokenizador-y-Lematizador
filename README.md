# Tokenizador y Lematizador Web

Este proyecto consiste en una aplicación web que permite tokenizar y lematizar texto en español e inglés. El frontend está desarrollado en JavaScript y el backend en Python utilizando Flask y spaCy.

## Funcionalidades

* Permite ingresar texto en un área de texto.
* Detecta automáticamente el idioma del texto (español o inglés).
* Realiza la tokenización del texto ingresado.
* Realiza la lematización del texto, excluyendo caracteres especiales y palabras no alfabéticas.
* Muestra los resultados de la tokenización y la lematización en la interfaz web.
* Manejo de errores en caso de problemas con el servidor o entrada inválida.

## Tecnologías Utilizadas

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask, spaCy, flask-cors, langdetect

## Requisitos

Asegúrate de tener instalado lo siguiente:

* Python 3.x
* pip (gestor de paquetes de Python)
* Node.js y npm (opcional, si deseas gestionar dependencias del frontend de forma más avanzada)

## Instalación y Ejecución

**Backend (Python/Flask):**

1.  Clona este repositorio:
    ```bash
    git clone [URL_DEL_REPOSITORIO]
    cd nombre-del-repositorio/backend
    ```
2.  Crea un entorno virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    python -m spacy download es_core_news_sm
    python -m spacy download en_core_web_sm
    ```
4.  Ejecuta la aplicación Flask:
    ```bash
    python app.py
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000/`.

**Frontend (JavaScript/HTML):**

1.  Navega al directorio `frontend`:
    ```bash
    cd ../frontend
    ```
2.  Abre el archivo `index.html` en tu navegador web.

    *Nota: El frontend está configurado para comunicarse con el backend en `/procesar_texto`. Asegúrate de que tu backend esté corriendo en la misma dirección o ajusta la URL en `frontend/script.js` si es necesario.*

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## Uso

1.  Abre el archivo `frontend/index.html` en tu navegador.
2.  Ingresa el texto que deseas analizar en el campo de texto proporcionado.
3.  Haz clic en el botón "Analizar".
4.  Los resultados de la tokenización y lematización se mostrarán debajo del botón.
5.  En caso de error (texto vacío o error del servidor), se mostrará un mensaje de error.

## Próximas Mejoras

* Implementar soporte para más idiomas.
* Permitir al usuario seleccionar el idioma explícitamente.
* Mejorar la interfaz de usuario y la presentación de los resultados.
* Añadir pruebas unitarias para el backend.
* Considerar la implementación de un sistema de build para el frontend.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

MIT License

Copyright (c) 2025 Mitsunori Kawashiro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Mitsunori Kawashiro**

* Sitio web: [https://kawashiro.dev/](https://kawashiro.dev/)
* Correo electrónico: [contact@kawashiro.dev](mailto:contact@kawashiro.dev)

## Agradecimientos a la Comunidad

Quisiera expresar mi sincero agradecimiento a la comunidad de código abierto por las valiosas herramientas, librerías y conocimientos compartidos que han hecho posible la creación de este proyecto. En particular, me gustaría destacar y agradecer a los desarrolladores y contribuyentes de los siguientes proyectos:

* **Flask:** Por proporcionar un framework web robusto y flexible para Python.
* **spaCy:** Por su potente biblioteca de procesamiento de lenguaje natural que facilita la tokenización y lematización.
* **flask-cors:** Por simplificar la gestión de peticiones Cross-Origin Resource Sharing (CORS) en aplicaciones Flask.
* **langdetect:** Por su útil librería para la detección automática del idioma.
* A la vasta comunidad de desarrolladores de JavaScript y Python por sus innumerables tutoriales, documentación y respuestas en foros que han sido de gran ayuda durante el desarrollo.

¡Su dedicación a compartir conocimiento y recursos es fundamental para el crecimiento y la innovación en el mundo del desarrollo de software!
