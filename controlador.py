from vista import VistaMenu, VistaFormulario
import datetime

# ===================== CONTROLADOR PRINCIPAL (SESION) =====================
class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.rol_actual = None
        self.vista.btnConfirmar.config(command=self.iniciarSesion)

    def iniciarSesion(self):
        usuario = self.vista.getUsuario()
        contrasena = self.vista.getContrasena()
        valido, rol = self.modelo.verificarUsuario(usuario, contrasena)
        if valido:
            self.rol_actual = rol
            self.vista.mostrarMensaje(f"Bienvenido {usuario} ({rol})")
            self.vista.ventana.after(300, self.abrirMenu)
        else:
            self.vista.mostrarMensaje("Usuario o contraseña incorrectos")

    def abrirMenu(self):
        master = self.vista.ventana
        self.vista.ventana.withdraw()
        vista_menu = VistaMenu(master, self.rol_actual)
        ControladorMenu(vista_menu, self.modelo, self.rol_actual, master)


# ===================== CONTROLADOR MENÚ =====================
class ControladorMenu:
    def __init__(self, vista, modelo, rol, master):
        self.vista = vista
        self.modelo = modelo
        self.rol = rol
        self.master = master

        self.vista.btnRegistrarInv.config(command=lambda: self.abrirModulo("invernadero"))
        self.vista.btnControlInv.config(command=lambda: self.abrirModulo("control_invernadero"))
        self.vista.btnControlEnf.config(command=lambda: self.abrirModulo("enfermedad"))

    def abrirModulo(self, tipo):
        vista_form = VistaFormulario(self.master, tipo)
        ControladorFormulario(vista_form, self.modelo, self.rol, self.master)
        self.vista.ventana.withdraw()


# ===================== CONTROLADOR FORMULARIO =====================
class ControladorFormulario:
    def __init__(self, vista, modelo, rol, master):
        self.vista = vista
        self.modelo = modelo
        self.rol = rol
        self.master = master

        self.invernaderos = []
        self.enfermedades = []

        # ==================== Botones ====================
        if vista.tipo == "invernadero":
            self.vista.btnGuardar.config(command=self.agregarInvernadero)
            self.vista.btnCancelar.config(command=self.vista.limpiarCampos)
            self.vista.btnRegresar.config(command=self._regresarMenu)

        elif vista.tipo == "control_invernadero":
            self.vista.btnFiltrar.config(command=self.filtrarInvernaderos)
            self.vista.btnMostrar.config(command=self.mostrarTodosInvernaderos)
            self.vista.btnEditar.config(command=self.editarInvernadero)
            self.vista.btnEliminar.config(command=self.eliminarInvernadero)
            self.vista.btnDetalles.config(command=self.detallesInvernadero)
            self.vista.btnRegresar.config(command=self._regresarMenu)
            self.mostrarTodosInvernaderos()

        elif vista.tipo == "enfermedad":
            self.vista.btnAgregar.config(command=self.agregarEnfermedad)
            self.vista.btnActualizar.config(command=self.actualizarEnfermedad)
            self.vista.btnEliminar.config(command=self.eliminarEnfermedad)
            self.vista.btnConsultar.config(command=self.consultarEnfermedades)
            self.vista.btnFiltrar.config(command=self.filtrarEnfermedades)
            self.vista.btnRegresar.config(command=self._regresarMenu)
            self.consultarEnfermedades()

    # ===================== MÉTODO AUXILIAR =====================
    def mostrarTexto(self, texto):
        """Muestra texto en lblLista si existe, si no usa lblResultado."""
        if hasattr(self.vista, "lblLista"):
            self.vista.lblLista.config(text=texto)
        else:
            self.vista.lblResultado.config(text=texto)

    # ===================== MÉTODOS INVERNADERO =====================
    def agregarInvernadero(self):
        datos = (
            self.vista.entryNombre.get(),
            self.vista.entryCapacidad.get(),
            self.vista.entrySuperficie.get(),
            self.vista.entryTipoCultivo.get(),
            self.vista.entrySistemaRiego.get(),
            self.vista.entryFechaCreacion.get(),
            self.vista.entryResponsable.get(),
            self.vista.entryEstado.get()
        )
        self.modelo.agregarInvernadero(*datos)
        self.vista.mostrarMensaje("✅ Invernadero agregado")
        self.vista.limpiarCampos()
        self.mostrarTodosInvernaderos()

    def mostrarTodosInvernaderos(self):
        self.invernaderos = self.modelo.consultarInvernaderos()
        texto = "\n".join([f"{i[0]} - {i[1]} ({i[7]})" for i in self.invernaderos])
        self.mostrarTexto(texto)

    def filtrarInvernaderos(self):
        estado = self.vista.entryBuscar.get().strip()
        if not estado:
            self.vista.mostrarMensaje("⚠️ Ingresa un estado para filtrar")
            return
        self.invernaderos = self.modelo.filtrarPorEstado(estado)
        texto = "\n".join([f"{i[0]} - {i[1]} ({i[7]})" for i in self.invernaderos])
        self.mostrarTexto(texto)

    def editarInvernadero(self):
        seleccionado = self._obtenerInvernaderoSeleccionado()
        if seleccionado:
            invernadero_dict = {
                "idInvernadero": seleccionado[0],
                "nombreInvernadero": seleccionado[1],
                "capacidadProduccion": seleccionado[2],
                "superficie": seleccionado[3],
                "tipoCultivo": seleccionado[4],
                "sistemaRiego": seleccionado[5],
                "fechaCreacion": seleccionado[6],
                "responsable": seleccionado[7],
                "estado": seleccionado[8]
            }
            self.vista.abrirVentanaEditarInvernadero(invernadero_dict, self._guardarEdicion)

    def _guardarEdicion(self, datos_actualizados):
        idInv = datos_actualizados.pop("idInvernadero")
        self.modelo.actualizarInvernadero(idInv, *datos_actualizados.values())
        self.vista.mostrarMensaje("✅ Invernadero actualizado")
        self.mostrarTodosInvernaderos()

    def eliminarInvernadero(self):
        seleccionado = self._obtenerInvernaderoSeleccionado()
        if seleccionado:
            self.modelo.eliminarInvernadero(seleccionado[0])
            self.vista.mostrarMensaje("🗑️ Invernadero eliminado")
            self.mostrarTodosInvernaderos()

    def detallesInvernadero(self):
        seleccionado = self._obtenerInvernaderoSeleccionado()
        if seleccionado:
            texto = "\n".join([f"{k}: {v}" for k, v in zip(
                ["ID","Nombre","Capacidad","Superficie","Tipo Cultivo","Sistema Riego","Fecha Creación","Responsable","Estado"],
                seleccionado)])
            self.mostrarTexto(texto)

    def _obtenerInvernaderoSeleccionado(self):
        id_sel = self.vista.entryIdSeleccionado.get().strip()
        for inv in self.invernaderos:
            if str(inv[0]) == id_sel:
                return inv
        self.vista.mostrarMensaje("⚠️ ID de invernadero no válido")
        return None

    # ===================== MÉTODOS ENFERMEDAD =====================
    def agregarEnfermedad(self):
        nombre = self.vista.entryNombreEnfermedad.get().strip()
        descripcion = self.vista.entryDescripcion.get().strip()
        tipoCultivo = self.vista.entryTipoCultivo.get().strip()
        fechaDeteccion = self.vista.entryFechaDeteccion.get().strip()
        nivelGravedad = self.vista.entryNivelGravedad.get().strip()

        if not nombre or not tipoCultivo or not fechaDeteccion:
            self.vista.mostrarMensaje("⚠️ Nombre, Tipo de Cultivo y Fecha son obligatorios")
            return
        try:
            datetime.datetime.strptime(fechaDeteccion, "%Y-%m-%d")
        except ValueError:
            self.vista.mostrarMensaje("⚠️ Fecha inválida. Formato: YYYY-MM-DD")
            return
        try:
            self.modelo.agregarEnfermedad(nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad)
            self.vista.mostrarMensaje("✅ Enfermedad agregada")
            self.vista.limpiarCampos()
            self.consultarEnfermedades()
        except Exception as e:
            print("Error al agregar enfermedad:", e)
            self.vista.mostrarMensaje("❌ Error al agregar enfermedad. Revisar consola")

    def editarEnfermedad(self):
        seleccionado = self._obtenerEnfermedadSeleccionada()
        if seleccionado:
            enf_dict = {
                "idEnfermedad": seleccionado[0],
                "nombre": seleccionado[1],
                "descripcion": seleccionado[2],
                "tipoCultivo": seleccionado[3],
                "fechaDeteccion": seleccionado[4],
                "nivelGravedad": seleccionado[5]
            }
            self.vista.abrirVentanaEditarEnfermedad(enf_dict, self._guardarEdicionEnfermedad)

    def _guardarEdicionEnfermedad(self, datos_actualizados):
        idEnf = datos_actualizados.pop("idEnfermedad")
        original = next((e for e in self.enfermedades if str(e[0]) == str(idEnf)), None)
        if not original:
            self.vista.mostrarMensaje("⚠️ ID no encontrado")
            return
        nombre = datos_actualizados.get("nombre") or original[1]
        descripcion = datos_actualizados.get("descripcion") or original[2]
        tipoCultivo = datos_actualizados.get("tipoCultivo") or original[3]
        fechaDeteccion = datos_actualizados.get("fechaDeteccion") or original[4]
        nivelGravedad = datos_actualizados.get("nivelGravedad") or original[5]

        try:
            self.modelo.actualizarEnfermedad(idEnf, nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad)
            self.vista.mostrarMensaje("✅ Enfermedad actualizada")
            self.consultarEnfermedades()
        except Exception as e:
            print("Error al actualizar enfermedad:", e)
            self.vista.mostrarMensaje("❌ Error al actualizar enfermedad. Revisar consola")

    def actualizarEnfermedad(self):
        self.editarEnfermedad()

    def eliminarEnfermedad(self):
        idEnf = self.vista.entryIdEnfermedad.get().strip()
        if not idEnf:
            self.vista.mostrarMensaje("⚠️ Debes ingresar el ID para eliminar")
            return
        try:
            self.modelo.eliminarEnfermedad(idEnf)
            self.vista.mostrarMensaje("🗑️ Enfermedad eliminada")
            self.consultarEnfermedades()
        except Exception as e:
            print("Error al eliminar enfermedad:", e)
            self.vista.mostrarMensaje("❌ Error al eliminar enfermedad. Revisar consola")

    def consultarEnfermedades(self):
        try:
            self.enfermedades = self.modelo.consultarEnfermedades()
            texto = "\n".join([f"{e[0]} - {e[1]} ({e[3]})" for e in self.enfermedades])
            self.mostrarTexto(texto)
        except Exception as e:
            print("Error al consultar enfermedades:", e)
            self.vista.mostrarMensaje("❌ Error al consultar enfermedades. Revisar consola")

    def filtrarEnfermedades(self):
        filtro = self.vista.entryFiltrar.get().strip()
        if not filtro:
            self.vista.mostrarMensaje("⚠️ Ingresa un tipo de cultivo para filtrar")
            return
        try:
            lista_filtrada = self.modelo.filtrarEnfermedades(filtro)
            texto = "\n".join([f"{e[0]} - {e[1]} ({e[3]})" for e in lista_filtrada])
            self.mostrarTexto(texto)
        except Exception as e:
            print("Error al filtrar enfermedades:", e)
            self.vista.mostrarMensaje("❌ Error al filtrar. Revisar consola")

    def _obtenerEnfermedadSeleccionada(self):
        idEnf = self.vista.entryIdEnfermedad.get().strip()
        for enf in self.enfermedades:
            if str(enf[0]) == idEnf:
                return enf
        self.vista.mostrarMensaje("⚠️ ID de enfermedad no válido")
        return None

    # ------------------ REGRESAR ------------------
    def _regresarMenu(self):
        from vista import VistaMenu
        from controlador import ControladorMenu

        vista_menu = VistaMenu(self.master, self.rol)
        ControladorMenu(vista_menu, self.modelo, self.rol, self.master)
        self.vista.ventana.destroy()
