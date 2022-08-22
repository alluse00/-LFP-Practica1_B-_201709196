from tkinter import *
from tkinter import filedialog, ttk
import sys
from procesos import *

listaGlobal = []

'''Principal'''
class prime():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Practica 1 LFP B+')
        self.center(self.window, 600, 500)
        self.window.resizable(False,False)
        self.lista_global = []
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=500, width=600)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        Label(self.frame, text='Lenguajes Formales y de Programación B+', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=15, y=10)
        Label(self.frame, text='Allan Josué Rafael Morales', font=('Courier',10), fg='#ffffff', bg='#000a12').place(x=15, y=30)
        Label(self.frame, text='201709196', font=('Courier',10), fg='#ffffff', bg='#000a12').place(x=15, y=45)
        Button(self.frame, text='Abrir', font=('Century Gothic',20), fg='#ffffff', bg='#0d47a1', activebackground = '#002171',command = self.cargarDoc).place(x= 270, y=120)
        Button(self.frame, text='Gestionar Cursos', font=('Century Gothic',20), fg='#ffffff', bg='#0d47a1', activebackground = '#002171',command = self.goGest).place(x= 190, y=190)
        Button(self.frame, text='Conteo de Créditos', font=('Century Gothic',20), fg='#ffffff', bg='#0d47a1', activebackground = '#002171', command= self.goCounting).place(x= 165, y=260)
        Button(self.frame, text='Salir', font=('Century Gothic',20), fg='#ffffff', bg='#880e4f', activebackground = '#bc477b',command = self.Exit).place(x= 275, y=330)
        self.frame.mainloop()

    def goGest(self):
        self.window.destroy()
        gest()
    
    def goCounting(self):
        self.window.destroy()
        counting()

    def Exit(self):
        sys.exit()

    def cargarDoc(self):
        global listaGlobal
        try:
            archivo = filedialog.askopenfilename(title = 'Seleccionar archivo LFP', filetypes=[('LFP files', '*.lfp')])
            lista = analizador.selecDoc(archivo)

            for i in lista:
                listaGlobal.append(i)
        except:
            pass

'''Gestión'''
class gest():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Gestionar Cursos')
        self.center(self.window, 600, 500)
        self.window.resizable(False,False)
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=500, width=600)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        Label(self.frame, text='Opciones:', font=('Courier',24), fg='#ffffff', bg='#000a12').place(x=15, y=10)
        Label(self.frame, text='.', font=('Courier',50), fg='#ffffff', bg='#000a12').place(x=180, y=35)
        Label(self.frame, text='.', font=('Courier',50), fg='#ffffff', bg='#000a12').place(x=180, y=95)
        Label(self.frame, text='.', font=('Courier',50), fg='#ffffff', bg='#000a12').place(x=180, y=155)
        Label(self.frame, text='.', font=('Courier',50), fg='#ffffff', bg='#000a12').place(x=180, y=215)
        Label(self.frame, text='.', font=('Courier',50), fg='#ffffff', bg='#000a12').place(x=180, y=275)
        Button(self.frame, text='Listar Cursos', font=('Century Gothic',18), fg='#ffffff', bg='#006064', activebackground = '#00363a', command= self.goList).place(x= 220, y=60)
        Button(self.frame, text='Mostrar Cursos', font=('Century Gothic',18), fg='#ffffff', bg='#006064', activebackground = '#00363a', command= self.goShow).place(x= 220, y=120)
        Button(self.frame, text='Agregar Curso', font=('Century Gothic',18), fg='#ffffff', bg='#006064', activebackground = '#00363a', command= self.goAdd).place(x= 220, y=180)
        Button(self.frame, text='Editar Curso', font=('Century Gothic',18), fg='#ffffff', bg='#006064', activebackground = '#00363a', command= self.goEdit).place(x= 220, y=240)
        Button(self.frame, text='Eliminar Curso', font=('Century Gothic',18), fg='#ffffff', bg='#006064', activebackground = '#00363a', command= self.goDelet).place(x= 220, y=300)
        Button(self.frame, text='Regresar', font=('Century Gothic',16), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command= self.goPrime).place(x= 440, y=420)
        self.frame.mainloop()

    def goPrime(self):
        self.window.destroy()
        prime()

    def goList(self):
        self.window.destroy()
        list()

    def goShow(self):
        self.window.destroy()
        show()
        
    def goAdd(self):
        self.window.destroy()
        add()

    def goEdit(self):
        self.window.destroy()
        edit()

    def goDelet(self):
        self.window.destroy()
        delet()

'''Listado de Cursos'''
class list():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Listar Cursos')
        self.center(self.window, 700, 450)
        self.window.geometry('700x450')
        self.window.resizable(False,False)
        self.window.configure(bg='#000a12')
        global listaGlobal
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=450, width=700)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        Button(self.frame, text='Regresar', font=('Century Gothic',16), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command= self.goGest).place(x= 560, y=375)
        
        tabla = ttk.Treeview(self.frame, columns=('codigo','nombre','prereq','opcion','semestre','creditos','estado'), show='headings')
        tabla.place(x=70,y=50)
        
        tabla.column('codigo',width=50,anchor=CENTER)
        tabla.column('nombre',width=140,anchor=CENTER)
        tabla.column('prereq',width=80,anchor=CENTER)
        tabla.column('opcion',width=80,anchor=CENTER)
        tabla.column('semestre',width=65,anchor=CENTER)
        tabla.column('creditos',width=55,anchor=CENTER)
        tabla.column('estado',width=80,anchor=CENTER)

        tabla.heading('codigo',text='Código',anchor = CENTER)
        tabla.heading('nombre',text='Nombre',anchor = CENTER)
        tabla.heading('prereq',text='Pre-Requisito',anchor = CENTER)
        tabla.heading('opcion',text='Opcionalidad',anchor = CENTER)
        tabla.heading('semestre',text='Semestre',anchor = CENTER)
        tabla.heading('creditos',text='Creditos',anchor = CENTER)
        tabla.heading('estado',text='Estado',anchor = CENTER)

        curso = []

        for i in range(len(listaGlobal)):

            valores = (listaGlobal[i].getCodigo(), listaGlobal[i].getNombre(), listaGlobal[i].getPrerequisito(), listaGlobal[i].getObligatorio(), listaGlobal[i].getSemestre(), listaGlobal[i].getCreditos(), listaGlobal[i].getEstado())
            curso.append(valores)

        for x in curso:
            tabla.insert("", END, values = x)

        style = ttk.Style()
        style.configure('Treeview', background = '#90caf9', foreground = 'black', rowheight = 20)
        style.map('Treeview', background= [('selected', '#03a9f4')])
        
        self.frame.mainloop()

    def goGest(self):
        self.window.destroy()
        gest()

'''Agregar Cursos'''
class show():

    global codigoEntrada

    def __init__(self):
        self.window = Tk()
        self.window.title('Mostrar Curso')
        self.center(self.window, 600, 500)
        self.window.resizable(False,False)
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=500, width=600)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)

        Label(self.frame, text='Código:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=40)
        codigoEntrada = Entry(self.frame, width='30', font=('Century Gothic',12))
        codigoEntrada.place(x=225, y=40)
        Label(self.frame, text='Nombre:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=80)
        labelNombre = Label(self.frame, width='30', font=('Century Gothic',12))
        labelNombre.place(x=225, y=80)
        Label(self.frame, text='Pre-requisito:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=120)
        labelPrereq = Label(self.frame, width='30', font=('Century Gothic',12))
        labelPrereq.place(x=225, y=120)
        Label(self.frame, text='Semestre:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=160)
        labelSemestre = Label(self.frame, width='30', font=('Century Gothic',12))
        labelSemestre.place(x=225, y=160)
        Label(self.frame, text='Opcionalidad:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=200)
        labelOpcionalidad = Label(self.frame, width='30', font=('Century Gothic',12))
        labelOpcionalidad.place(x=225, y=200)
        Label(self.frame, text='Créditos:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=240)
        labelCreditos = Label(self.frame, width='30', font=('Century Gothic',12))
        labelCreditos.place(x=225, y=240)
        Label(self.frame, text='Estado:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=280)
        labelEstado = Label(self.frame, width='30', font=('Century Gothic',12))
        labelEstado.place(x=225, y=280)

        def viewCurso():
            temporal = False
            for i in range(len(listaGlobal)):
                if codigoEntrada.get() == listaGlobal[i].getCodigo():

                    nombre = StringVar()
                    prereq = StringVar()
                    semestre = StringVar()
                    opcional = StringVar()
                    creditos = StringVar()
                    estado = StringVar()

                    nombre.set(listaGlobal[i].getNombre())
                    prereq.set(listaGlobal[i].getPrerequisito())
                    semestre.set(listaGlobal[i].getSemestre())
                    opcional.set(listaGlobal[i].getObligatorio())                        
                    creditos.set(listaGlobal[i].getCreditos())
                    estado.set(listaGlobal[i].getEstado())

                    labelNombre.config(textvariable = nombre)
                    labelPrereq.config(textvariable = prereq)
                    labelSemestre.config(textvariable = semestre)
                    labelOpcionalidad.config(textvariable = opcional)
                    labelCreditos.config(textvariable = creditos)
                    labelEstado.config(textvariable = estado)

                    temporal = True

            if temporal == False:
                messagebox.showinfo(message='El codigo de curso no existe en el registro', title='Código Incorrecto')

        Button(self.frame, text='Mostrar', font=('Century Gothic',16), fg='#ffffff', bg='#8bc34a', activebackground = '#5a9216', command= viewCurso).place(x= 300, y=420)
        Button(self.frame, text='Regresar', font=('Century Gothic',16), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command= self.goGest).place(x= 465, y=420)

        self.frame.mainloop()
        return codigoEntrada

    def goGest(self):
        self.window.destroy()
        gest()

'''Agregar Cursos'''
class add():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Agregar Curso')
        self.center(self.window, 600, 500)
        self.window.resizable(False,False)
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=500, width=600)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        codigo = StringVar()
        nombre = StringVar()
        prereq = StringVar()
        semestre = StringVar()
        opcional = StringVar()
        credito = StringVar()
        estado = StringVar()

        Label(self.frame, text='Código:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=40)
        codigo_entry = Entry(textvariable= codigo, width='35', font=('Century Gothic',12))
        codigo_entry.place(x=225, y=40)
        Label(self.frame, text='Nombre:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=80)
        nombre_entry = Entry(textvariable= nombre, width='35', font=('Century Gothic',12))
        nombre_entry.place(x=225, y=80)
        Label(self.frame, text='Pre-requisito:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=120)
        prereq_entry = Entry(textvariable= prereq, width='35', font=('Century Gothic',12))
        prereq_entry.place(x=225, y=120)
        Label(self.frame, text='Semestre:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=160)
        semestre_entry = Entry(textvariable= semestre, width='35', font=('Century Gothic',12))
        semestre_entry.place(x=225, y=160)
        Label(self.frame, text='Opcionalidad:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=200)
        opcional_entry = Entry(textvariable= opcional, width='35', font=('Century Gothic',12))
        opcional_entry.place(x=225, y=200)
        Label(self.frame, text='Créditos:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=240)
        credito_entry = Entry(textvariable= credito, width='35', font=('Century Gothic',12))
        credito_entry.place(x=225, y=240)
        Label(self.frame, text='Estado:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=280)
        estado_entry = Entry(textvariable= estado, width='35', font=('Century Gothic',12))
        estado_entry.place(x=225, y=280)

        def addCurso():
            if opcional_entry.get() != '1' and opcional_entry.get() != '0' or estado_entry.get() != '0' and estado_entry.get() != '1' and estado_entry.get() != '-1':
                messagebox.showerror(message = 'Verifique que este ingresando bien sus datos', title = 'Valor Incorrecto')
            else:
                
                curso = cursos(
                    codigo_entry.get(), 
                    nombre_entry.get(), 
                    prereq_entry.get(), 
                    semestre_entry.get(),
                    opcional_entry.get(),  
                    credito_entry.get(),
                    estado_entry.get())

                listaGlobal.append(curso)

                messagebox.showinfo(message = 'Curso agregado', title = 'Curso Añadido')

                codigo_entry.delete(0, END)
                nombre_entry.delete(0, END) 
                prereq_entry.delete(0, END)
                semestre_entry.delete(0, END)
                opcional_entry.delete(0, END)
                credito_entry.delete(0, END)
                estado_entry.delete(0, END)

        Button(self.frame, text='Agregar', font=('Century Gothic',16), fg='#ffffff', bg='#8bc34a', activebackground = '#5a9216', command= addCurso).place(x= 300, y=420)
        Button(self.frame, text='Regresar', font=('Century Gothic',16), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command= self.goGest).place(x= 465, y=420)

        self.frame.mainloop()

    def goGest(self):
        self.window.destroy()
        gest()

'''Editar de Cursos'''
class edit():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Editar Curso')
        self.center(self.window, 600, 500)
        self.window.resizable(False,False)
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=500, width=600)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        codigo = StringVar()
        nombre = StringVar()
        prereq = StringVar()
        semestre = StringVar()
        opcional = StringVar()
        credito = StringVar()
        estado = StringVar()

        Label(self.frame, text='Código:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=40)
        codigo_entry = Entry(textvariable= codigo, width='35', font=('Century Gothic',12))
        codigo_entry.place(x=225, y=40)
        Label(self.frame, text='Nombre:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=80)
        nombre_entry = Entry(textvariable= nombre, width='35', font=('Century Gothic',12))
        nombre_entry.place(x=225, y=80)
        Label(self.frame, text='Pre-requisito:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=120)
        prereq_entry = Entry(textvariable= prereq, width='35', font=('Century Gothic',12))
        prereq_entry.place(x=225, y=120)
        Label(self.frame, text='Semestre:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=160)
        semestre_entry = Entry(textvariable= semestre, width='35', font=('Century Gothic',12))
        semestre_entry.place(x=225, y=160)
        Label(self.frame, text='Opcionalidad:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=200)
        opcional_entry = Entry(textvariable= opcional, width='35', font=('Century Gothic',12))
        opcional_entry.place(x=225, y=200)
        Label(self.frame, text='Créditos:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=240)
        credito_entry = Entry(textvariable= credito, width='35', font=('Century Gothic',12))
        credito_entry.place(x=225, y=240)
        Label(self.frame, text='Estado:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x=30, y=280)
        estado_entry = Entry(textvariable= estado, width='35', font=('Century Gothic',12))
        estado_entry.place(x=225, y=280)

        def editCurso():

            temporal = False
            for i in range(len(listaGlobal)):

                if codigo_entry.get() == listaGlobal[i].getCodigo():

                    listaGlobal[i].nombre = nombre_entry.get()
                    listaGlobal[i].prerequisito = prereq_entry.get()
                    listaGlobal[i].semestre = semestre_entry.get()
                    listaGlobal[i].creditos = credito_entry.get()

                    if opcional_entry.get() != '0' and opcional_entry.get() != '1':
                        messagebox.showerror(message='La opcionalidad es incorrecta', title='Dato erroneo')
                        opcional_entry.delete(0, END)
                        temporal = True
                        break
                    else:
                        listaGlobal[i].obligatorio = opcional_entry.get() 

                    if estado_entry.get() != '0' and estado_entry.get() != '1' and estado_entry.get() != '-1':
                        messagebox.showerror(message='El estado es incorrecto', title='Dato erroneo')
                        estado_entry.delete(0, END)
                        temporal = True
                        break
                        
                    else: 
                        listaGlobal[i].estado = estado_entry.get()

                    codigo_entry.delete(0, END)
                    nombre_entry.delete(0, END)
                    prereq_entry.delete(0, END) 
                    semestre_entry.delete(0, END)
                    opcional_entry.delete(0, END)
                    credito_entry.delete(0, END)
                    estado_entry.delete(0, END)

                    messagebox.showinfo(message='Curso editado correctamente', title='Curso Editado')

                    temporal = True

            if temporal == False:
                messagebox.showinfo(message='El curso no existe', title='Código Incorrecto')

        Button(self.frame, text='Editar', font=('Century Gothic',16), fg='#ffffff', bg='#8bc34a', activebackground = '#5a9216', command= editCurso).place(x= 300, y=420)
        Button(self.frame, text='Regresar', font=('Century Gothic',16), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command= self.goGest).place(x= 465, y=420)

        self.frame.mainloop()

    def goGest(self):
        self.window.destroy()
        gest()

'''Eliminar Curso'''
class delet():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Eliminar Curso')
        self.center(self.window, 500, 250)
        self.window.resizable(False,False)
        self.window.configure(bg='#000a12')
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=250, width=500)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        codigo = StringVar()

        codigo_entry = Entry(textvariable= codigo, width='15', font=('Century Gothic',12))
        codigo_entry.place(x=200, y=60)
        Label(self.frame, text='Código:', font=('Courier',16), fg='#ffffff', bg='#000a12').place(x= 80, y=60)

        def deleteCurso():
            temporal = False
            
            for i in range(len(listaGlobal)):

                if codigo_entry.get() == listaGlobal[i].getCodigo():

                    listaGlobal.pop(i)
                    codigo_entry.delete(0, END)

                    messagebox.showinfo(message='Curso eliminado correctamente', title='Eliminado')
                    temporal = True
                    break

            if temporal == False:
                messagebox.showinfo(message='Código de curso no existe', title='Código Incorrecto')

        Button(self.frame, text='Eliminar', font=('Century Gothic',16), fg='#ffffff', bg='#880e4f', activebackground = '#560027', command= deleteCurso).place(x= 225, y=177)
        Button(self.frame, text='Regresar', font=('Century Gothic',12), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command= self.goGest).place(x= 360, y=180)
        
        
        self.frame.mainloop()

    def goGest(self):
        self.window.destroy()
        gest()

'''Conteo de Creditos'''
class counting():
    
    def __init__(self):
        self.window = Tk()
        self.window.title('Conteo de Créditos')
        self.center(self.window, 600, 500)
        self.window.resizable(False,False)
        self.Window()

    def center(self, r, width, height):
        alto = r.winfo_screenheight()
        ancho = r.winfo_screenwidth()
        x = (ancho // 2) - (width // 2)
        y = (alto // 2) - (height // 2)
        r.geometry(f'+{x}+{y}')

    def Window(self):
        self.frame = Frame(height=500, width=600)
        self.frame.config(bg='#000a12')
        self.frame.pack(padx=0, pady=0)
        
        Label(self.frame, text='Créditos Aprobados:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=30, y=40)
        Label(self.frame, text='Créditos Cursando:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=30, y=90)
        Label(self.frame, text='Créditos Pendientes:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=30, y=140)
        Label(self.frame, text='Créditos Obligatorios hasta semestre N:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=30, y=190)
        Label(self.frame, text='Semestre:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=60, y=240)
        Label(self.frame, text='Créditos del Semestre:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=30, y=290)
        Label(self.frame, text='Semestre:', font=('Courier',12), fg='#ffffff', bg='#000a12').place(x=60, y=340)

        labelAprobados = Label(self.frame, font=('Courier',12), fg='#ffffff', bg='#000a12')
        labelAprobados.place(x=250, y=40)
        labelCursando = Label(self.frame,  font=('Courier',12), fg='#ffffff', bg='#000a12')
        labelCursando.place(x=250, y=90)
        labelPendientes = Label(self.frame,  font=('Courier',12), fg='#ffffff', bg='#000a12')
        labelPendientes.place(x=250, y=140)

        semestre01_entry = Entry( width='3', font=('Century Gothic',12))
        semestre01_entry.place(x=165, y=240)

        semestre02_entry = Entry( width='3', font=('Century Gothic',12))
        semestre02_entry.place(x=165, y=340)

        def countCreditos():
            aprobados = 0
            cursando = 0
            pendientes = 0
            
            for i in range(len(listaGlobal)):
                
                if listaGlobal[i].getEstado() == 'Aprobado': 
                    aprobados += int(listaGlobal[i].creditos)
                elif listaGlobal[i].getEstado() == 'Cursando':
                    cursando += int(listaGlobal[i].creditos)
                elif listaGlobal[i].getEstado() == 'Pendiente':  
                    pendientes += int(listaGlobal[i].creditos)

            aprobadoss = StringVar()
            cursandoss = StringVar()
            pendientess = StringVar()
            
            aprobadoss.set(str(aprobados))
            cursandoss.set(str(cursando))
            pendientess.set(str(pendientes))
            
            labelAprobados.config(textvariable=aprobadoss)
            labelCursando.config(textvariable=cursandoss)
            labelPendientes.config(textvariable=pendientess)

        
        Button(self.frame, text='Contar', font=('Century Gothic',10), fg='#ffffff', bg='#004d40', activebackground = '#00251a').place(x= 225, y=240)
        Button(self.frame, text='Contar', font=('Century Gothic',10), fg='#ffffff', bg='#004d40', activebackground = '#00251a', command=countCreditos).place(x= 225, y=340)
        Button(self.frame, text='Regresar', font=('Century Gothic',16), fg='#ffffff', bg='#b71c1c', activebackground = '#7f0000', command=self.goPrime).place(x= 465, y=420)

        self.frame.mainloop()

    def goPrime(self):
        self.window.destroy()
        prime()

prime()