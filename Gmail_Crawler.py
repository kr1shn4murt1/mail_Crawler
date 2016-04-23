#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Nombre: Tamano_Carpetas_correo.py
#Autor: sthevens Zuluaga
#Referencias: http://www.velocityreviews.com/forums/t335621-imap-get-size-of-mailboxes.html , http://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
#http://docs.python.org/library/imaplib.html , http://tools.ietf.org/html/rfc3501
#Dependencias: archivo "Correos_Gmail.conf" el cual debe estar en la misma carpeta que el script
#Propósito: Éste script imprime los mensajes que cumplen con un criteio de busqueda de las cuentas de correo definidas en el archivo
#"Tamano_Carpetas.conf" estableciendo una conexión imap con cada una.
#Para guardar el reporte en un archivo ejecutar el script desde la linea de comandos así: Tamano_Carpetas_Gmail.py >> Reporte_Tamano_Carpetas[fecha].txt

import sys, os, string, imaplib, re, ConfigParser, sys
#from email.Utils import formatdate

file = 'Correos_Gmail.conf' # Se define el archivo de configuracion
config = ConfigParser.RawConfigParser()
config.read(file) # Se lee el archivo de configuracion
imap_host=config.get('setup','imap_host') # Se define el servidor IMAP tomandolo del archivo .conf    verbose=config.getboolean('setup','verbose')
userlist=config.options('accounts') # Se define la lista de correos tomandolos del archivo .conf

for imap_user in userlist:
    try:
        # Se crea el objeto imap de conexion al servidor de Gmail
        M = imaplib.IMAP4_SSL(imap_host)
        imap_pswd=config.get('accounts', imap_user) # Se le asigna el atributo de contraseña al objeto IMAP
        M.login(imap_user, imap_pswd) # Se logea el objeto al servidor IMAP


        print "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        print "*","CUENTA: ",(imap_user),""
        print ""

        palabrasABuscar =['clave','usuario','password','pass','vpn','user','username','acceso','pwd','passwd','contrase'] #Aqui hay un problema con la ñ de contraseña
        M.select()

        for palabra in palabrasABuscar:
            #print "Palabra buscada es:", palabra.encode("utf-42")
            #print "Palabra buscada es:", palabra
            #typ, data = M.search(None,'TEXT',palabra.encode("utf-8")) #Se busca en todos los mensajes la palabra clave y se guardan en un array los mensajes encontrados
            typ, data = M.search(None,'TEXT',palabra)
            for num in data[0].split(): #Por cada mensaje en el array
                typ, data = M.fetch(num, '(RFC822)') #Se obtiene el mensaje completo con todos sus headers
                print 'Message %s\n%s\n' % (num, data[0][1]) # Se imprime el mensaje completo en crudo

        print "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        M.logout()# Se cierra la conexión de la cuenta de coreo

    except: # Se atrapan todos los errores para que el programa no termine su ejecución al encontrar un usuario o contraseña incorrectos y se imprimen en pantalla
        e = sys.exc_info()[1]
        print "Error : %s" % e

