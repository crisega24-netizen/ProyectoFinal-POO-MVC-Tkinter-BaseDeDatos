import tkinter as tk

# ===================== VISTA DE SESIÓN =====================
class VistaSesion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Vivero Vital - Inicio de Sesión")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="#F7F5D7")

        tk.Label(self.ventana, bg="#7AC74F", width=90, height=2).pack(pady=5)
        tk.Label(self.ventana, text="Iniciar Sesión", bg="#F7F5D7", fg="#3B3B3B",
                 font=("Arial", 22, "bold")).pack(pady=20)

        tk.Label(self.ventana, text="Usuario:", bg="#F7F5D7", font=("Arial", 12)).pack()
        self.entryUsuario = tk.Entry(self.ventana, width=30)
        self.entryUsuario.pack(pady=5)

        tk.Label(self.ventana, text="Contraseña:", bg="#F7F5D7", font=("Arial", 12)).pack()
        self.entryContrasena = tk.Entry(self.ventana, width=30, show="*")
        self.entryContrasena.pack(pady=5)

        self.btnConfirmar = tk.Button(self.ventana, text="Confirmar", bg="#7AC74F", fg="black",
                                      font=("Arial", 12, "bold"), width=15, command=None)
        self.btnConfirmar.pack(pady=10)

        self.lblMensaje = tk.Label(self.ventana, text="", bg="#F7F5D7", fg="red", font=("Arial", 11))
        self.lblMensaje.pack(pady=10)

        tk.Label(self.ventana, bg="#FFD166", width=90, height=2).pack(side="bottom")

    def getUsuario(self):
        return self.entryUsuario.get()

    def getContrasena(self):
        return self.entryContrasena.get()

    def mostrarMensaje(self, texto):
        self.lblMensaje.config(text=texto)

    def limpiarCampos(self):
        self.entryUsuario.delete(0, 'end')
        self.entryContrasena.delete(0, 'end')


# ===================== VISTA DE MENÚ =====================
class VistaMenu:
    COLOR_LABEL = "#FFD166"  

    def __init__(self, master, rol):
        self.rol = rol
        self.ventana = tk.Toplevel(master)
        self.ventana.title("Vivero Vital - Menú Principal")
        self.ventana.geometry("900x600")
        self.ventana.configure(bg="#F7F5D7")

        tk.Label(self.ventana, text="🌿 Vivero Vital 🌿", font=("Arial", 20, "bold"),
                 bg="#7AC74F", fg="black", width=80).pack(pady=15)

        self.btnRegistrarInv = tk.Button(self.ventana, text="Registrar Invernadero", bg="#E4C988",
                                         fg="black", width=25, font=("Arial", 12), command=None)
        self.btnRegistrarInv.pack(pady=5)

        self.btnControlInv = tk.Button(self.ventana, text="Control de Invernaderos", bg="#E4C988",
                                       fg="black", width=25, font=("Arial", 12), command=None)
        self.btnControlInv.pack(pady=5)

        self.btnControlEnf = tk.Button(self.ventana, text="Control de Enfermedades", bg="#E4C988",
                                       fg="black", width=25, font=("Arial", 12), command=None)
        self.btnControlEnf.pack(pady=5)

        self.lblImagenMenu = tk.Label(self.ventana, bg=self.COLOR_LABEL, width=40, height=10)
        self.lblImagenMenu.place(x=650, y=100)

        tk.Label(self.ventana, bg="#7AC74F", width=90, height=2).pack(side="bottom")
        tk.Label(self.ventana, bg="#FFD166", width=90, height=2).pack(side="bottom")

    def mostrarMensaje(self, texto):
        tk.Label(self.ventana, text=texto, bg="#F7F5D7", fg="black").pack(pady=10)


# ===================== VISTA DE FORMULARIOS =====================
class VistaFormulario:
    COLOR_LABEL = "#FFD166"  
    
    def __init__(self, master, tipo):
        self.tipo = tipo
        self.ventana = tk.Toplevel(master)
        self.ventana.geometry("950x600")
        self.ventana.configure(bg="#D7F2B8")

        if tipo == "invernadero":
            self.ventana.title("Registrar Invernadero")
            self._interfazInvernadero()
        elif tipo == "enfermedad":
            self.ventana.title("Control de Enfermedades")
            self._interfazEnfermedad()
        elif tipo == "control_invernadero":
            self.ventana.title("Control de Invernaderos")
            self._interfazControlInvernadero()

        self.lblResultado = tk.Label(self.ventana, text="", bg="#D7F2B8", fg="black")
        self.lblResultado.place(x=50, y=500)

    # ===================== FORMULARIO INVERNADERO =====================
    def _interfazInvernadero(self):
        tk.Label(self.ventana, text="REGISTRAR INVERNADERO", bg="#7AC74F",
                 fg="black", font=("Arial", 18, "bold"), width=90).pack(pady=10)

        self.lblImagenInvernadero = tk.Label(self.ventana, bg=self.COLOR_LABEL, width=40, height=10)
        self.lblImagenInvernadero.place(x=650, y=80)

        campos = [
            ("Nombre del invernadero:", "entryNombre"),
            ("Capacidad de producción:", "entryCapacidad"),
            ("Superficie (m²):", "entrySuperficie"),
            ("Tipo de cultivo:", "entryTipoCultivo"),
            ("Sistema de riego:", "entrySistemaRiego"),
            ("Fecha de creación:", "entryFechaCreacion"),
            ("Responsable:", "entryResponsable"),
            ("Estado:", "entryEstado")
        ]

        y_pos = 80
        for texto, attr in campos:
            tk.Label(self.ventana, text=texto, bg="#D7F2B8", anchor="w").place(x=50, y=y_pos)
            setattr(self, attr, tk.Entry(self.ventana, width=30))
            getattr(self, attr).place(x=250, y=y_pos)
            y_pos += 40

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", bg="green", fg="white", width=12, command=None)
        self.btnGuardar.place(x=250, y=450)

        self.btnCancelar = tk.Button(self.ventana, text="Cancelar", bg="red", fg="white", width=12, command=None)
        self.btnCancelar.place(x=370, y=450)

        self.btnRegresar = tk.Button(self.ventana, text="Regresar", bg="#6CCECB", fg="white", width=12, command=None)
        self.btnRegresar.place(x=820, y=540)

    # ===================== FORMULARIO CONTROL DE INVERNADEROS =====================
    def _interfazControlInvernadero(self):
        tk.Label(self.ventana, text="CONTROL DE INVERNADEROS", bg="#7AC74F",
                 fg="black", font=("Arial", 18, "bold"), width=90).pack(pady=10)

        self.lblImagenControl = tk.Label(self.ventana, bg=self.COLOR_LABEL, width=40, height=10)
        self.lblImagenControl.place(x=650, y=50)

        tk.Label(self.ventana, text="ID del invernadero:", bg="#D7F2B8").place(x=50, y=50)
        self.entryIdSeleccionado = tk.Entry(self.ventana, width=10)
        self.entryIdSeleccionado.place(x=180, y=50)

        tk.Label(self.ventana, text="Buscar por estado:", bg="#D7F2B8").place(x=50, y=90)
        self.entryBuscar = tk.Entry(self.ventana, width=30)
        self.entryBuscar.place(x=200, y=90)

        self.btnFiltrar = tk.Button(self.ventana, text="Filtrar", bg="lightgreen", command=None)
        self.btnFiltrar.place(x=450, y=87)
        self.btnMostrar = tk.Button(self.ventana, text="Mostrar todos", bg="lightblue", command=None)
        self.btnMostrar.place(x=530, y=87)

        self.lblLista = tk.Label(self.ventana, text="", bg="#D7F2B8", fg="black", justify="left", anchor="nw")
        self.lblLista.place(x=50, y=130, width=600, height=350)

        self.btnEditar = tk.Button(self.ventana, text="Editar", bg="orange", fg="black", width=12, command=None)
        self.btnEditar.place(x=150, y=500)
        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", bg="red", fg="white", width=12, command=None)
        self.btnEliminar.place(x=280, y=500)
        self.btnDetalles = tk.Button(self.ventana, text="Detalles", bg="green", fg="white", width=12, command=None)
        self.btnDetalles.place(x=410, y=500)

        self.lblResultado = tk.Label(self.ventana, text="", bg="#D7F2B8", fg="black")
        self.lblResultado.place(x=50, y=680)

        self.btnRegresar = tk.Button(self.ventana, text="Regresar", bg="#6CCECB", fg="white", width=12, command=None)
        self.btnRegresar.place(x=820, y=540)

    # ===================== FORMULARIO CONTROL DE ENFERMEDADES =====================
    def _interfazEnfermedad(self):
        tk.Label(self.ventana, text="CONTROL DE ENFERMEDADES", bg="#7AC74F",
                 fg="black", font=("Arial", 18, "bold"), width=90).pack(pady=10)

        self.lblImagenEnfermedad = tk.Label(self.ventana, bg=self.COLOR_LABEL, width=40, height=10)
        self.lblImagenEnfermedad.place(x=650, y=80)

        campos = [
            ("ID Enfermedad:", "entryIdEnfermedad"),
            ("Nombre:", "entryNombreEnfermedad"),
            ("Descripción:", "entryDescripcion"),
            ("Tipo de cultivo:", "entryTipoCultivo"),
            ("Fecha de detección:", "entryFechaDeteccion"),
            ("Nivel de gravedad:", "entryNivelGravedad")
        ]

        y_pos = 120
        for texto, attr in campos:
            tk.Label(self.ventana, text=texto, bg="#D7F2B8").place(x=50, y=y_pos)
            setattr(self, attr, tk.Entry(self.ventana, width=30))
            getattr(self, attr).place(x=250, y=y_pos)
            y_pos += 45

        tk.Label(self.ventana, text="Filtrar por tipo de cultivo:", bg="#D7F2B8").place(x=50, y=y_pos)
        self.entryFiltrar = tk.Entry(self.ventana, width=20)
        self.entryFiltrar.place(x=250, y=y_pos)
        self.btnFiltrar = tk.Button(self.ventana, text="Filtrar", bg="lightgreen", width=12, command=None)
        self.btnFiltrar.place(x=420, y=y_pos)
        y_pos += 50

        self.btnAgregar = tk.Button(self.ventana, text="Agregar", bg="green", fg="white", width=12, command=None)
        self.btnAgregar.place(x=250, y=y_pos)
        self.btnActualizar = tk.Button(self.ventana, text="Actualizar", bg="orange", fg="black", width=12, command=None)
        self.btnActualizar.place(x=370, y=y_pos)
        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", bg="red", fg="white", width=12, command=None)
        self.btnEliminar.place(x=490, y=y_pos)
        self.btnConsultar = tk.Button(self.ventana, text="Consultar", bg="lightblue", fg="black", width=12, command=None)
        self.btnConsultar.place(x=610, y=y_pos)

        self.lblLista = tk.Label(self.ventana, text="", bg="#D7F2B8", fg="black", justify="left", anchor="nw")
        self.lblLista.place(x=50, y=y_pos+90, width=850, height=300)

        self.btnRegresar = tk.Button(self.ventana, text="Regresar", bg="#6CCECB", fg="white", width=12, command=None)
        self.btnRegresar.place(x=820, y=540)

    # ===================== MÉTODOS COMUNES =====================
    def limpiarCampos(self):
        for attr in dir(self):
            if attr.startswith("entry"):
                entry = getattr(self, attr)
                entry.delete(0, 'end')

    def mostrarMensaje(self, texto):
        if hasattr(self, "lblResultado"):
            self.lblResultado.config(text=texto)
        elif hasattr(self, "lblLista"):
            self.lblLista.config(text=texto)
        else:
            tk.Label(self.ventana, text=texto, bg="#D7F2B8", fg="black").pack(pady=10)

    # ===================== VENTANA DE EDICIÓN PARA INVERNADERO =====================
    def abrirVentanaEditarInvernadero(self, invernadero, callback_guardar):
        ventana_edit = tk.Toplevel(self.ventana)
        ventana_edit.title("Editar Invernadero")
        ventana_edit.geometry("500x400")
        ventana_edit.configure(bg="#D7F2B8")

        campos = [
            ("Nombre del invernadero:", "nombreInvernadero"),
            ("Capacidad de producción:", "capacidadProduccion"),
            ("Superficie (m²):", "superficie"),
            ("Tipo de cultivo:", "tipoCultivo"),
            ("Sistema de riego:", "sistemaRiego"),
            ("Fecha de creación:", "fechaCreacion"),
            ("Responsable:", "responsable"),
            ("Estado:", "estado")
        ]

        entries = {}
        y_pos = 30
        for texto, key in campos:
            tk.Label(ventana_edit, text=texto, bg="#D7F2B8", anchor="w").place(x=20, y=y_pos)
            ent = tk.Entry(ventana_edit, width=30)
            ent.insert(0, invernadero.get(key, ""))
            ent.place(x=200, y=y_pos)
            entries[key] = ent
            y_pos += 35

        def guardar_cambios():
            datos_actualizados = {k: e.get() for k, e in entries.items()}
            datos_actualizados["idInvernadero"] = invernadero["idInvernadero"]
            callback_guardar(datos_actualizados)
            ventana_edit.destroy()

        tk.Button(ventana_edit, text="Guardar cambios", bg="green", fg="white",
                  command=guardar_cambios).place(x=180, y=y_pos+20)

    # ===================== VENTANA DE EDICIÓN PARA ENFERMEDAD =====================
    def abrirVentanaEditarEnfermedad(self, enfermedad, callback_guardar):
        ventana_edit = tk.Toplevel(self.ventana)
        ventana_edit.title("Editar Enfermedad")
        ventana_edit.geometry("500x350")
        ventana_edit.configure(bg="#D7F2B8")

        campos = [
            ("Nombre:", "nombre"),
            ("Descripción:", "descripcion"),
            ("Tipo de cultivo:", "tipoCultivo"),
            ("Fecha de detección:", "fechaDeteccion"),
            ("Nivel de gravedad:", "nivelGravedad")
        ]

        entries = {}
        y_pos = 20
        for texto, key in campos:
            tk.Label(ventana_edit, text=texto, bg="#D7F2B8", anchor="w").place(x=20, y=y_pos)
            ent = tk.Entry(ventana_edit, width=30)
            ent.insert(0, enfermedad.get(key, ""))
            ent.place(x=200, y=y_pos)
            entries[key] = ent
            y_pos += 40

        def guardar_cambios():
            datos_actualizados = {k: e.get() for k, e in entries.items()}
            datos_actualizados["idEnfermedad"] = enfermedad["idEnfermedad"]
            callback_guardar(datos_actualizados)
            ventana_edit.destroy()

        tk.Button(ventana_edit, text="Guardar cambios", bg="green", fg="white",
                  command=guardar_cambios).place(x=180, y=y_pos+20)
