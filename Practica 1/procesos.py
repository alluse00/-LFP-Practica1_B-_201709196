from tkinter import filedialog, ttk, messagebox
import os

class cursos():

    def __init__(self, codigo, nombre, prerequisito, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisito = prerequisito
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    '''GET'''

    def getCodigo(self):
        return self.codigo
    
    def getNombre(self):
        return self.nombre

    def getPrerequisito(self):
        return self.prerequisito

    def getObligatorio(self):
        if self.obligatorio == '1':
            return "Obligatorio"
        elif self.obligatorio == '0':
            return "Opcional"

    def getSemestre(self):
        return self.semestre

    def getCreditos(self):
        return self.creditos

    def getEstado(self):
        if self.estado == '0\n' or self.estado == '0':
            return "Aprobado"
        elif self.estado == '1\n' or self.estado == '1':
            return "Cursando"
        elif self.estado == '-1\n' or self.estado == '-1':
            return "Pendiente"

    '''SET'''

    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrerequisito(self, prerequisito):
        self.prerequisito = prerequisito

    def setObligatorio(self, obligatorio):
        self.obligatorio = obligatorio

    def setSemestre(self, semestre):
        self.semestre = semestre

    def setCreditos(self, creditos):
        self.creditos = creditos

    def setEstado(self, estado):
        self.estado = estado

class analizador():
        
    def selecDoc(archivo):
        datos = open(archivo, encoding='utf-8')  
        lineas = datos.readlines()
        datos.close() 

        curs = []
        for linea in lineas:
            data = linea.split(',')
            curso = cursos(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            curs.append(curso) 
        return curs
