# mail_Crawler

* Estos scripts ingresan a un listado de cuentas de correo y busca correos con información confidencial para imprimirlos

* Al interior del script Gmail_Crawler esta definido un array con palabras claves a buscar, busca correos que coincidan con las   palabras claves: 
    - clave
    - usuario
    - password
    - pass
    - vpn
    - user
    - username
    - acceso
    - pwd
    - passwd
  
* El procedimiento anterior permite sacar rapidamente la informacion de caracter confidencial que este en un listado grande de correos lo que puede dar acceso a otros sitios, otros servidores, accesos de terminal, otras cuentas de correo, vpn's, etc, si la información de acceso a algún sitio fué compartida por correo se vera reflejada alli


# Los scripts están en pares:

* Archivo Gmail_Crawler.py y su archivo de configuración Correos_Gmail.conf
* Archivo Estado_Carpetas_hotmail.py y su archivo de configuración Correos_Hotmail.conf

# Procedimiento de ejecucion:

* Se debe tener instalado python 2.7.x en la maquina
* Descargar el script y su archivo de configuración a una carpeta en la máquina
  Gmail_Crawler.py
  Correos_Gmail.conf
* Modificar el archivo Correos_Gmail.conf para poner alli el listado de correos y contrseñas a las que se quiere ingresar
* Abrir una ventana de CMD, e ir a la carpeta donde se descargaron los archivos.
* Ejecutar el script ejm: c:\scripts\Gmail_Crawler.py
* Si se desea que el script ingrese a otras cuentas de correo de otro servidor IMAP, modificar las seccion del servidor IMAP en   el archivo Correos_Gmail.conf

* El procedimiento anterior tambien aplica para el script Estado_Carpetas_Hotmail.py y su correspondiente archivo de 
  configuracion.

# Post que explica su funcionamiento:
http://kr1shn4murt1.blogspot.com.co/2016/04/mailcrawler-intrusion-y-revision-masiva.html

# Video explicativo de cada linea de codigo del script y muestra de su ejecucion:
https://www.youtube.com/watch?v=EoXC4c_0zAA



