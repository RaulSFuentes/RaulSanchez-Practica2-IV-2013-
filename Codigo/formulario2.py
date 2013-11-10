#!/usr/bin/python
#Raúl Sánchez Fuentes Practica 2 IV
#Copyright (C) 2013  Raúl

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from borrar import *
from web import form
import os.path
from time import time


formulariop = form.Form( 

    form.Textbox("nombre", description = "Nombre:", value=""),
    form.Textarea("sugerencia", description = "Haz una sugerencia para la asignatura de IV:", value=""),
    form.Button("Enviar"),
) 


class Formulario:        
   
    def GET(self):
        form = formulariop()  
        html = """
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>PON TUS SUGERENCIAS PARA IV</title>
            <link rel="stylesheet" href="static/comun.css">
            <link rel="stylesheet" href="static/estilo.css">
            <link rel="stylesheet" href="static/formulario.css">
          </head>
          <body>
            <h1>Formularios Avanzados</h1>
            
            <p>Tu nombre en .</p>
            
            <form method="POST">
            %s
            </form>
          </body>
        </html>""" % (form.render())  
        
        return html
      
    def POST(self): 
        form = formulariop() 
        
        form.validates() 
                    
        f = open ("sugerencias.txt", "a")
 	f.write("%s : \n" % (form.d.nombre))
	f.write("%s \n\n --- \n" % (form.d.sugerencia))
 	f.close()
 	f=open("sugerencias.txt")
 	texto = f.read()
 	f.close()
        html = """
        <html>
          <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Avanzado</title>
            <link rel="stylesheet" href="static/comun.css">
            <link rel="stylesheet" href="static/moonchild.css">
            <link rel="stylesheet" href="static/formulario.css">
          </head>
          <body>
            <h1>Gracias</h1>
	    <p>En breve se enviara la informacion</p>
            <p>Sugerencias hasta el momento</p>
	    <p>%s</p>
            
          
          </body>
        </html>""" % texto 
        
        return html
