from tkinter import StringVar, Tk,Label,Entry,Button,Frame
import tkinter
from tkinter import messagebox


class Años(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        etiqueta = Label(ventana, text="Ferretería El tornillo Feliz", font=("Century", 14) , bg="#56CD63", fg="white")
        etiqueta.pack(fill= tkinter.X)
        ventana.resizable( False, False)
        self.master=master
        self.pack()
        self.config(background= "sky blue")
        self.crearControles()
        

    def Calculo(self):
        
        canti1=int(self.Cantidad1.get())
        canti2=int(self.Cantidad2.get())
        canti3=int(self.Cantidad3.get())
        preci1=float(self.Precio1.get())
        preci2=float(self.Precio2.get())
        preci3=float(self.Precio3.get())
        
        subto1= canti1 * preci1
        subto2= canti2 * preci2
        subto3= canti3 * preci3

        totl = subto1 + subto2 + subto3  
        self.Subtotal1.set(str(subto1))
        self.Subtotal2.set(str(subto2))
        self.Subtotal3.set(str(subto3))
        self.Total1.set(str(totl))

        Dni = self.Dni1.get() 
        dniii = len(Dni)
        telefono = self.Telefono1.get()
        teleee = len(telefono)
        
        if self.Telefono1.get() == teleee > 1 or teleee < 10:
            telefono = telefono

        else:
            messagebox.showwarning("Número Celular incorrecto!!!")
            

        if self.Dni1.get() == dniii > 1 or dniii < 9:
            Dni = Dni
            
        else: 
            messagebox.showwarning("DNI incorrecto!!!")
        

        self.Dni1.set(str(Dni))
        self.Telefono1.set(str(telefono))
        
        print("----------------------------------------------------------")
        print("********Ferreteria El tornillo Feliz:)********************")
        print("\n")
        print(">El cliente: ",  self.t_Nombre.get(),self.t_Apellido.get())
        print("               DNI: ",            self.t_Dni.get())
        print(">Dirección_d_Cliente: ", self.t_Direccion.get())
        print(">Telefono_d_Cliente: ",  self.t_Tel.get())
        print(">Codigo_d_Prodcuto1: ",  self.t_Codigo1.get())
        print(">Codigo_d_Prodcuto2: ",  self.t_Codigo2.get())
        print(">Codigo_d_Producto3: ",  self.t_Codigo3.get())
        print(">Descripción1_Prodc: ",  self.t_Des1.get())
        print(">Descripción2_Prodc: ",  self.t_Des2.get())
        print(">Descripción3_Prodc: ",  self.t_Des3.get())
        print(">Unidad1_d_Producto: ",  self.t_Uni1.get())
        print(">Unidad2_d_Producto: ",  self.t_Uni2.get())
        print(">Unidad3_d_Producto: ",  self.t_Uni3.get())
        print(">Cantidad1_Producto: ",  self.t_Cantidad1.get())
        print(">Cantidad2_Prodcuto: ",  self.t_Cantidad2.get())
        print(">Cantidad3_Prodcuto: ",  self.t_Cantidad3.get())
        print(">Precio1_d_Producto: ",  self.t_Precio1.get())
        print(">Precio2_d_Prodcuto: ",  self.t_Precio2.get())
        print(">Precio3_d_Producto: ",  self.t_Precio3.get())
        print(">Subtotal1_Producto: ",  subto1)
        print(">Subtotal2_Producto: ",  subto2)
        print(">Subtotal3_Prodcuto: ",  subto3)
        print(">>Total a pagar : ",  totl)
        print("-----------------------------------------------------------")
        print("             Muchas gracias por su compra :)")
        print("-----------------------------------------------------------")
        self.t_Dni.delete(0,"end")
        self.t_Nombre.delete(0, "end")
        self.t_Apellido.delete(0, "end")
        self.t_Direccion.delete(0, "end")
        self.t_Tel.delete(0, "end")

    
    def Resultados(self):

        codgo1=int(self.Codigo1.get())
        codgo2=int(self.Codigo2.get())
        codgo3=int(self.Codigo3.get())
        desc1=self.Descripcion1.get()
        desc2=self.Descripcion2.get()
        desc3=self.Descripcion3.get()

        preci1=self.Precio1.get()
        preci2=self.Precio2.get()
        preci3=self.Precio3.get()

        uni=self.Unidad1.get()
        uni1=self.Unidad2.get()
        uni2=self.Unidad3.get()


        if codgo1 >= 1 and codgo1 <= 10:
            desc1 = "Stock"
            preci1 = 15
            uni = "tornillos"
        elif codgo1 > 10 and codgo1 < 30:
            desc1 = "sin oferta"
            preci1 = 30
            uni = "Madera"
        else:
            desc1 = "oferta"
            preci1 =50
            uni = "Clavos"


        if codgo2 > 1 and codgo1 < 10:
            desc2 = "Stock"
            preci2 = 60
            uni1 = "Martillo"
        elif codgo2 > 10 and codgo1 < 30:
            desc2 = "sin oferta"
            preci2 = 80
            uni1 = "Cinta"
        else:
            desc2= "oferta"
            preci2= 90
            uni1 ="Lampa"


        if codgo3 > 1 and codgo1 < 10:
            desc3 = "Stock"
            preci3 = 90
            uni2 = "Puas"
        elif codgo3 > 10 and codgo1 < 30:
            desc3 = "sin oferta"
            preci3 = 120
            uni2 = "Cemento"
        else:
            desc3 = "oferta"
            preci3 = 190
            uni2 = "mayas"

        self.Precio1.set(str(preci1))
        self.Precio2.set(str(preci2))
        self.Precio3.set(str(preci3))
        
        self.Descripcion1.set(str(desc1))
        self.Descripcion2.set(str(desc2))
        self.Descripcion3.set(str(desc3))

        self.Codigo1.set(str(codgo1))
        self.Codigo2.set(str(codgo2))
        self.Codigo3.set(str(codgo3))

        self.Unidad1.set(str(uni))
        self.Unidad2.set(str(uni1))
        self.Unidad3.set(str(uni2))

    def limpiezaTodo(self):

        self.Codigo1.set("")
        self.Codigo2.set("")
        self.Codigo3.set("")
        self.Descripcion1.set("")
        self.Descripcion2.set("")
        self.Descripcion3.set("")
        self.Unidad1.set("")
        self.Unidad2.set("")
        self.Unidad3.set("")
        self.Cantidad1.set("")
        self.Cantidad2.set("")
        self.Cantidad3.set("")
        self.Precio1.set("")
        self.Precio2.set("")
        self.Precio3.set("")
        self.Subtotal1.set("")
        self.Subtotal2.set("")
        self.Subtotal3.set("")
        self.Total1.set("")
        self.Dni1.set("")
        self.Apellido1.set("")
        self.Nombre1.set("")
        self.Direccion1.set("")
        self.Telefono1.set("")
        self.t_Dni.focus()
    

    def crearControles(self):
        
        self.Dni1=StringVar() 
        self.Dni10 = Label(self, text="DNI")
        self.Dni10.grid(row=5, column=0, sticky='e', pady=5, padx=5)
        self.t_Dni = Entry(self,textvariable=self.Dni1)
        self.t_Dni.grid(row=5, column=1, pady=5, padx=5)

        self.Apellido1=StringVar() 
        self.Apellido10 = Label(self, text="Nombres")
        self.Apellido10.grid(row=6, column=0, sticky='e', pady=5, padx=5)
        self.t_Apellido = Entry(self,textvariable=self.Apellido1)
        self.t_Apellido.grid(row=6, column=1, pady=5, padx=5)
        
        self.Nombre1=StringVar()
        self.Nombre10 = Label(self, text="Apellidos")
        self.Nombre10.grid(row=6, column=2, sticky='e', pady=5, padx=5)
        self.t_Nombre = Entry(self,textvariable= self.Nombre1)
        self.t_Nombre.grid(row=6, column=3, pady=5, padx=5)
        
        self.Direccion1=StringVar() 
        self.Direccion10 = Label(self, text="Dirección")
        self.Direccion10.grid(row=7, column=0, sticky='e', pady=5, padx=5)
        self.t_Direccion = Entry(self,textvariable=self.Direccion1)
        self.t_Direccion.grid(row=7, column=1, columnspan=3, sticky='we',pady=5, padx=5)
        
        self.Telefono1 = StringVar() 
        self.Telefono10 = Label(self, text="Teléfono")
        self.Telefono10.grid(row=8, column=0, sticky='e', pady=5, padx=5)
        self.t_Tel = Entry(self,textvariable=self.Telefono1)
        self.t_Tel.grid(row=8, column=1,columnspan=3, sticky='we', pady=5, padx=5)
        
        
        self.Codigo1 = StringVar()
        self.Codigo2 = StringVar()
        self.Codigo3 = StringVar()

        self.Codigo10 = Label(self, text="Cod_Prod")
        self.Codigo10.grid(row=9, column=0,sticky='e', pady=5, padx=5)
        self.t_Codigo1 = Entry(self, width=7, textvariable =self.Codigo1)
        self.t_Codigo1.grid(row=10, column=0, pady=5, padx=5)
        self.t_Codigo2 = Entry(self, width=7,textvariable =self.Codigo2)
        self.t_Codigo2.grid(row=11, column=0, pady=5, padx=5)
        self.t_Codigo3 = Entry(self, width=7,textvariable =self.Codigo3)
        self.t_Codigo3.grid(row=12, column=0, pady=5, padx=5)


        self.Descripcion1 = StringVar() 
        self.Descripcion2 = StringVar()
        self.Descripcion3 = StringVar()

        self.Des10 = Label(self, text="Descripción")
        self.Des10.grid(row=9, column=1,sticky='ew', pady=5, padx=5)
        self.t_Des1 = Entry(self, width=10, state="readonly",textvariable = self.Descripcion1)
        self.t_Des1.grid(row=10, column=1, pady=5, padx=5)
        self.t_Des2 = Entry(self, width=10, state="readonly",textvariable = self.Descripcion2)
        self.t_Des2.grid(row=11, column=1, pady=5, padx=5)
        self.t_Des3 = Entry(self, width=10, state="readonly",textvariable = self.Descripcion3)
        self.t_Des3.grid(row=12, column=1, pady=5, padx=5)


        self.Unidad1 = StringVar() 
        self.Unidad2 = StringVar()
        self.Unidad3 = StringVar()

        self.Uni10 = Label(self, text='Unidad')
        self.Uni10.grid(row=9, column=2,sticky='ew', pady=5, padx=5)
        self.t_Uni1 = Entry(self, width=16, state="readonly", textvariable = self.Unidad1)
        self.t_Uni1.grid(row=10, column=2, pady=5, padx=5)
        self.t_Uni2 = Entry(self, width=16, state="readonly",textvariable = self.Unidad2 )
        self.t_Uni2.grid(row=11, column=2, pady=5, padx=5)
        self.t_Uni3 = Entry(self, width=16, state="readonly",textvariable = self.Unidad3)
        self.t_Uni3.grid(row=12, column=2, pady=5, padx=5)


        self.Cantidad1 = StringVar()
        self.Cantidad2 = StringVar()
        self.Cantidad3 = StringVar()

        self.Cantidad10 = Label(self, text='Cantidad')
        self.Cantidad10.grid(row=9, column=3,sticky='ew', pady=5, padx=5)
        self.t_Cantidad1 = Entry(self, width=7, textvariable = self.Cantidad1)
        self.t_Cantidad1.grid(row=10, column=3, pady=5, padx=5)
        self.t_Cantidad2 = Entry(self, width=7, textvariable = self.Cantidad2)
        self.t_Cantidad2.grid(row=11, column=3, pady=5, padx=5)
        self.t_Cantidad3 = Entry(self, width=7, textvariable = self.Cantidad3)
        self.t_Cantidad3.grid(row=12, column=3, pady=5, padx=5)


        self.Precio1 = StringVar()
        self.Precio2 = StringVar()
        self.Precio3 = StringVar()

        self.Precio10 = Label(self, text='Precio')
        self.Precio10.grid(row=9, column=4,sticky='ew', pady=5, padx=5)
        self.t_Precio1 = Entry(self, width=7,textvariable = self.Precio1 )
        self.t_Precio1.grid(row=10, column=4, pady=5, padx=5)
        self.t_Precio2 = Entry(self, width=7,textvariable = self.Precio2)
        self.t_Precio2.grid(row=11, column=4, pady=5, padx=5)
        self.t_Precio3 = Entry(self, width=7,textvariable = self.Precio3)
        self.t_Precio3.grid(row=12, column=4, pady=5, padx=5)


        self.Subtotal1 = StringVar()
        self.Subtotal2 = StringVar()
        self.Subtotal3 = StringVar()

        self.Subtotal10 = Label(self, text='Subtotal')
        self.Subtotal10.grid(row=9, column=5,sticky='ew', pady=5, padx=5)
        self.t_Subtotal1 = Entry(self, width=7, state="readonly",textvariable =self.Subtotal1)
        self.t_Subtotal1.grid(row=10, column=5, pady=5, padx=5)
        self.t_Subtotal2 = Entry(self, width=7, state="readonly",textvariable = self.Subtotal2)
        self.t_Subtotal2.grid(row=11, column=5, pady=5, padx=5)
        self.t_Subtotal3 = Entry(self, width=7, state="readonly",textvariable = self.Subtotal3)
        self.t_Subtotal3.grid(row=12, column=5, pady=5, padx=5)


        self.Total1 = StringVar() 
        self.Total10 = Label(self, text='Total',font=("calibri", 12),bg= "#A4D8D4")
        self.Total10.grid(row=12, column=6,sticky='ew', pady=5, padx=5)
        self.t_Total = Entry(self, width=7, textvariable = self.Total1)
        self.t_Total.grid(row=12, column=7, pady=5, padx=5)

        self.aviso = Label(self, text="Escoger Cod_Prod del 1 al 30!!!", bg= "sky blue")
        self.aviso.grid(row=13, column=2, sticky='e', pady=5, padx=5)

        self.aviso = Label(self, text="Despues del Cod_Prod poner = informacion!!!", bg= "sky blue")
        self.aviso.grid(row=14, column=2, sticky='e', pady=5, padx=5)

        guardar=Button(self, text='Calcular',font=("calibri", 15),bg= "#A4D8D4", command=self.Calculo)
        guardar.grid(row=13, column=5, pady=10, padx=10)


        guardar=Button(self, text='Informacion',font=("calibri", 12),bg= "#A4D8D4", command= self.Resultados )
        guardar.grid(row=13, column=1, pady=5, padx=5)


        guardar=Button(self, text='Limpiar', font=("calibri", 12),bg= "yellow", command= self.limpiezaTodo )
        guardar.grid(row=13, column=0, pady=5, padx=5)


ventana=Tk()
ventana.title("Ferretería El tornillo Feliz")
operacion=Años(ventana)
ventana.mainloop()