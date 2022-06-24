# FinalProjectBlog
Este blog es parte del proyecto final del curso de Python de CoderHouse, donde usamos Django como framework.

# Integrantes
Nahuel Pablo Lim
Miguel Serrudo

# Link a video explicativo del la app.
https://youtu.be/HjoqtoYplk0

### Instrucciones:
Instalar Python desde la [web oficial](https://www.python.org/downloads/)

1.  Clonar el proyecto (o descargar el archivo comprimido)

        -    *git clone https://github.com/nahuelim/ProyectoFinal.git

2.  Instalar las dependencias del proyecto:

        -    *pip install django*
        -    *pip install Pillow*
        -    *pip install django-ckeditor*

3. Entrar a la carpeta del proyecto

        -    *cd FinalProjectBlog*

4. Realizar las migraciones para generar la base de datos

        -    *python manage.py makemigrations*
        -    *python manage.py migrate*

5. Podes crear un superusuario (=admin)

        -    *python manage.py createsuperuser*

6. Correr la aplicacion

        -    *python manage.py runserver*

7. Ya podes ingresar a la web
    -    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

***
  
### Acerca del Blog
El proyecto trata de un blog dedicado a informacion sobre tractores agricolas y ganaderas.

Cualquier persona que entra al blog puede visualizar los posteos (tanto la lista de posts como el detalle de cada uno) pero, para poder **editar**, **crear** 
o **eliminar** contenido deberán estar **logueados** o en su defecto, **registrarse**. A su vez, únicamente los autores del posteo podrán **editarlo**.

#### Posts
Cada **post** consta de un título, subtítulo, imagen, contenido, autor y fecha de publicación (que se agrega automáticamente).
Los posts se listan del más reciente al más antiguo.

#### Perfil
Cada **usuario** puede editar su perfil. 
Cada usuario consta de un numbre de usuario, contraseña y un email como datos obligatorios, y si así lo desean pueden agregar su nombre y apellido.  
En el perfil del usuario se lista además la fecha de su último ingreso y la fecha en la que se ha unido (registrado) al blog.  

Los datos de guardan en una base de datos de motor SQLite3 ya provista por Django.  

#### Mensajería
Los usuarios cuentan con un sistema de mensajería a modo de mensaje directo.  
Los mensajes sólo los pueden ver los usuarios a los cuales están destinados y el usuario que envió el mismo.  
Dentro del perfil o desde la barra de navegación el usuario accederá a su **Inbox** donde verá su bandeja de entrada y su bandeja de salida.  
  
#### Layout
El blog cuenta con una **barra de navegación** a la cual se puede acceder a las distintas secciones del mismo -> Home, Posts, About. Y además, en el margen derecho 
podrás ingresar, o registrar un nuevo usuario.  
Al estar logueado en el margen derecho se muestra el nombre de usuario, con un menú desplegable donde se puede acceder al Perfil, 
a sus mensajes y cerrar la sesión.

#### Tecnologías usadas
-    ***Frontend***: HTML (muy básico al no contar con previos conocimientos de frontend)
-    ***Backend***: Python with Django

***

