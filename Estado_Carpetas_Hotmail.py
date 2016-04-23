#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Nombre: Tamano_Carpetas_correo.py
#Autor: sthevens Zuluaga
#Basado en http://www.velocityreviews.com/forums/t335621-imap-get-size-of-mailboxes.html
#Dependencias: archivo Tamano_Carpetas.conf el cual debe estar en la misma carpeta que el script
#Propósito: Éste script retorna los tamaños de las carpetas de cuentas de correo definidas en el archivo
#"Tamano_Carpetas.conf" estableciendo una conexión imap con cada una.
#Para guardar el reporte en un archivo ejecutar el script desde la linea de comandos así: Tamano_Carpetas_correo.py >> Reporte_Tamano_Carpetas[fecha].txt

import poplib, sys, os, string, re, ConfigParser, sys
#from email.Utils import formatdate


file = 'Correos_Hotmail.conf' # Se define el archivo de configuracion
config = ConfigParser.RawConfigParser()
config.read(file) # Se lee el archivo de configuracion
servidor_Pop=config.get('setup','servidor_Pop') # Se define el servidor IMAP tomandolo del archivo .conf    verbose=config.getboolean('setup','verbose')
userlist=config.options('accounts') # Se define la lista de correos tomandolos del archivo .conf

for pop_User in userlist:
    try:
        # Open a connection to the POP3 server
        M = poplib.POP3_SSL(servidor_Pop,995) #Conección al servidor de hotmail
        imap_pswd=config.get('accounts', pop_User) # Se le asigna el atributo de contrase?a al objeto IMAP
        M.user (pop_User) # Se logea el objeto al servidor IMAP
        M.pass_ (imap_pswd)


        #M.login('correo@hest.com','contraseña')

        # The list of all folders
        print "*","CUENTA:          ", (pop_User),"                                                                                   *"
        print "ESTADO DE LA CUENTA", M.stat()
        print ""
        #print "LISTADO DE MENSAJES"
        #print M.list()
        print "*                                                                                                                             *"
        print "-------------------------------------------------------------------------------------------------------------------------------"



        M.quit()# Close the connection

    except: # catch *all* exceptions5.
        #pass
        e = sys.exc_info()[1]
        print "Error : %s" % e

