<h1>Una guía rápida para crear nuestro proyecto en Local con Django</h1>

<h2>Creación del proyecto</h2>
En primer lugar abre una ventana de comandos/terminal, navega hasta donde quieres almacenar tus apps Django y crea una carpeta para tu nuevo sitio web. Entra en el directorio a continuación.
Crear el nuevo proyecto usando el comando <strong>django-admin startproject</strong> <i>seguido del nombre de tu proyecto</i> y navega luego dentro de la carpeta.

<h2>Creación de la aplicación</h2>
A continuación, ejecuta <strong> python manage.py startapp</strong> <i>seguido del nombre de tu nueva aplicación</i> para crear la aplicación catalog que vivirá dentro de nuestro proyecto (éste debe ejecutarse en la misma carpeta que el manage.py de tu proyecto)

<h2>Registro de la aplicación</h2> 
Ahora que se ha creado la aplicación tenemos que registrarla en el proyecto de manera que sea incluida cuando cualquiera de las herramientas se ejecute (por ejemplo, para añadir modelos a la base de datos). Las aplicaciones se registran añadiéndolas a la lista de INSTALLED_APPS en los ajustes del proyecto.

Abre el fichero de ajustes del proyecto settings.py (se encuentra dentro de la subcarpeta con el mismo nombre que nuestro proyecto) y encuentra la definición de la lista INSTALLED_APPS. Añade a continuación una nueva linea al final de la lista. 

Por ejemplo, si nuestra aplicación se llamase 'productos' deberíamos añadir 'productos' al final de la lista INSTALLED_APPS. 
(No te olvides de la coma al final de la línea)


<h3>Y se acabó</h3>
Hasta aquí ya tendríamos nuestro proyecto, aunque vacío, operativo. 
La podemos iniciar con <strong>python manage.py runserver</strong> lo cual nos dará la dirección en local de nuestro proyecto. 
El resto sería crear nuestros modelos para dar forma a nuestra api y darle una vista ya sea siguiente con Django o, como hice yo mismo, conectandola con Vue. 

Aquí les dejo un tutorial que me ayudó a darle algo de forma: https://www.youtube.com/watch?v=uu98pqiUJU8&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=1 


