# API_IEI_171_N2
Consumo de API en python con POO

<h1>Modularización de un Proyecto POO</h1>

<p>
La modularización en un proyecto de Programación Orientada a Objetos consiste en dividir el sistema en partes bien definidas y organizadas, cada una con responsabilidades específicas. 
Esto favorece la reutilización, el mantenimiento, la escalabilidad y la claridad del código.
</p>

<h2>Módulos del Proyecto</h2>

<h3>1. Módulo: auxiliares</h3>
<ul>
  <li>Contiene clases y funciones de apoyo que no pertenecen directamente a la lógica principal del negocio pero que resultan necesarias para el correcto funcionamiento del sistema.</li>
  <li>Ejemplos: validaciones, conversiones de formatos, manejo de fechas, utilidades matemáticas o de cadenas.</li>
  <li>Su objetivo es centralizar la lógica de apoyo para evitar duplicación de código.</li>
</ul>

<h3>2. Módulo: datos</h3>
<ul>
  <li>Encargado de la persistencia y acceso a Base de Datos.</li>
  <li>Implementa clases y métodos para la conexión a bases de datos, lectura/escritura de archivos o interacción con servicios externos de almacenamiento.</li>
  <li>Aísla el manejo de datos de las demás capas, lo que permite cambiar la fuente de información sin afectar la lógica de negocio.</li>
</ul>

<h3>3. Módulo: negocio</h3>
<ul>
  <li>Contiene la lógica de negocios que impulsa el desarrollo del sistema.</li>
  <li>Implementa reglas de negocio, cálculos, procesos y flujos que definen cómo funciona la aplicación.</li>
  <li>Se apoya en los módulos de datos y auxiliares, pero mantiene independencia de la interfaz de usuario.</li>
</ul>

<h3>4. Módulo: modelos</h3>
<ul>
  <li>Define las clases que representan las entidades principales del dominio del problema.</li>
  <li>Cada modelo encapsula atributos y comportamientos propios de la entidad (por ejemplo: Cliente, Producto, Pedido).</li>
  <li>Sirven como base para la comunicación entre los diferentes módulos, especialmente entre la lógica de negocio y los datos.</li>
</ul>

<h3>5. Módulo: iu (Interfaces de Usuario)</h3>
<ul>
  <li>Proporciona la interacción con el usuario mediante comandos de consola.</li>
  <li>Se comunica con el módulo de negocio para ejecutar acciones y mostrar resultados.</li>
  <li>Debe ser lo más independiente posible de la lógica interna, para facilitar cambios en la presentación sin afectar al resto del sistema.</li>
</ul>

<h1>Librerías útiles para un proyecto en Python</h1>

<p>
Para implementar el proyecto de Programación Orientada a Objetos en Python, se recomienda el uso de las siguientes librerías, organizadas por su función en la modularización:
</p>

<h2>📦 Librerías recomendadas</h2>

<h3>🔹 Base de Datos</h3>
<ul>
  <li><b>mysql-connector-python</b> → Conexión con MySQL desde Python.
    <pre><code>pip install mysql-connector-python</code></pre>
  </li>
  <li>(Opcional) <b>SQLAlchemy</b> → ORM para trabajar con bases de datos de forma orientada a objetos.
    <pre><code>pip install SQLAlchemy</code></pre>
  </li>
</ul>

<h3>🔹 Presentación de datos</h3>
<ul>
  <li><b>prettytable</b> → Mostrar tablas en la terminal de manera ordenada.
    <pre><code>pip install prettytable</code></pre>
  </li>
  <li><b>tabulate</b> → Alternativa ligera para mostrar datos en tablas.
    <pre><code>pip install tabulate</code></pre>
  </li>
</ul>

<h3>🔹 Interfaz gráfica (GUI)</h3>
<ul>
  <li><b>tkinter</b> → Incluido en la mayoría de distribuciones de Python, sirve para GUIs simples.</li>
  <li><b>PyQt5</b> → Framework potente para GUIs avanzadas.
    <pre><code>pip install PyQt5</code></pre>
  </li>
  <li><b>customtkinter</b> → Mejora el aspecto visual de tkinter.
    <pre><code>pip install customtkinter</code></pre>
  </li>
</ul>

<h3>🔹 Auxiliares / Utilidades</h3>
<ul>
  <li><b>python-dateutil</b> → Manejo avanzado de fechas.
    <pre><code>pip install python-dateutil</code></pre>
  </li>
  <li><b>pandas</b> → Procesamiento y manipulación de datos estructurados.
    <pre><code>pip install pandas</code></pre>
  </li>
  <li><b>requests</b> → Para consumir servicios web o APIs REST.
    <pre><code>pip install requests</code></pre>
  </li>
</ul>

<h3>🔹 Pruebas y depuración</h3>
<ul>
  <li><b>pytest</b> → Para pruebas unitarias.
    <pre><code>pip install pytest</code></pre>
  </li>
  <li><b>pylint</b> / <b>flake8</b> → Análisis estático y buenas prácticas de código.
    <pre><code>pip install pylint flake8</code></pre>
  </li>
</ul>

<h2>📂 Ejemplo de <code>requirements.txt</code></h2>

<p>
Para ejecutar la isntalación de todas las dependencias definidas previamente para cada proyecto, debemos crear un archivo <code>requirements.txt</code>, como el que se observa a continuación y luego, mediante el terminal, navegar hasta la ubicación del archivo, para ejecutar el siguiente comando:
  <pre><code>pip install -r requirements.txt</code></pre>
</p>

<p>
Este debiera ser el contenido del archivo <code>requirements.txt</code>, considerando que incluiremos sólo las librerías definidas para el proyecto:
</p>

<pre><code>mysql-connector-python
prettytable
python-dateutil
pandas
requests
pytest
</code></pre>

<p>
(Puedes añadir <b>PyQt5</b> o <b>customtkinter</b> si decides usar una GUI más avanzada).
</p>

<p>Para crear automáticamente un archivo de requerimientos con todas las librerías instaladas en su máquina, ejecutamos en terminal:</p>
<code>pip freeze > requirements.txt</code>

<p>Para instalar las librerías desde el archivo requerimientos, ejecutamos en terminal:</p>
<code>pip install -r requirements.txt</code>