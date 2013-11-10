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

import os

        
def borrar(directorio, prefijo, fechaAntiguedad):
    cadena = ""
    for filename in os.listdir(directorio):
        if filename.startswith(prefijo):
            if (os.stat(directorio + filename).st_mtime < fechaAntiguedad):
                os.remove(directorio + filename)

    return cadena
