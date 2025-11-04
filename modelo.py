from modeloBaseDatos import hacerConexion

# ===================== MODELO GENERAL =====================
class ModeloGeneral:
    def __init__(self):
        self.usuario = UsuarioModel()
        self.invernadero = InvernaderoModel()
        self.enfermedad = EnfermedadModel()

    # ===================== MÉTODOS DE USUARIO =====================
    def verificarUsuario(self, nombreUsuario, contrasena):
        return self.usuario.verificarUsuario(nombreUsuario, contrasena)

    # ===================== MÉTODOS DE INVERNADERO =====================
    def agregarInvernadero(self, *args):
        self.invernadero.agregarInvernadero(*args)

    def consultarInvernaderos(self):
        return self.invernadero.consultarInvernaderos()

    def actualizarInvernadero(self, *args):
        self.invernadero.actualizarInvernadero(*args)

    def eliminarInvernadero(self, idInvernadero):
        self.invernadero.eliminarInvernadero(idInvernadero)

    def filtrarPorEstado(self, estado):
        return self.invernadero.filtrarPorEstado(estado)

    # ===================== MÉTODOS DE ENFERMEDAD =====================
    def agregarEnfermedad(self, nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad):
        self.enfermedad.agregarEnfermedad(nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad)

    def actualizarEnfermedad(self, idEnfermedad, nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad):
        self.enfermedad.actualizarEnfermedad(idEnfermedad, nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad)

    def eliminarEnfermedad(self, idEnfermedad):
        self.enfermedad.eliminarEnfermedad(idEnfermedad)

    def consultarEnfermedades(self):
        return self.enfermedad.consultarEnfermedades()

    def filtrarEnfermedades(self, tipoCultivo):
        return self.enfermedad.filtrarPorCultivo(tipoCultivo)


# ===================== MODELO DE USUARIO =====================
class UsuarioModel:
    def __init__(self):
        self.conexion = hacerConexion()

    def verificarUsuario(self, nombreUsuario, contrasena):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT rol FROM usuario WHERE nombreUsuario = %s AND contrasena = %s"
            cursor.execute(sql, (nombreUsuario, contrasena))
            resultado = cursor.fetchone()
        except:
            resultado = None
        finally:
            cursor.close()

        if resultado:
            return True, resultado[0]
        return False, None


# ===================== MODELO DE INVERNADERO =====================
class InvernaderoModel:
    def __init__(self):
        self.conexion = hacerConexion()

    def agregarInvernadero(self, nombre, capacidad, superficie, tipoCultivo, sistemaRiego, fechaCreacion, responsable, estado):
        try:
            cursor = self.conexion.cursor()
            sql = """INSERT INTO invernadero 
                     (nombreInvernadero, capacidadProduccion, superficie, tipoCultivo, sistemaRiego, fechaCreacion, responsable, estado)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nombre, capacidad, superficie, tipoCultivo, sistemaRiego, fechaCreacion, responsable, estado))
            self.conexion.commit()
        except Exception as e:
            print("Error al agregar invernadero:", e)
        finally:
            cursor.close()

    def consultarInvernaderos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM invernadero")
            datos = cursor.fetchall()
        except:
            datos = []
        finally:
            cursor.close()
        return datos

    def actualizarInvernadero(self, idInvernadero, nombre, capacidad, superficie, tipoCultivo, sistemaRiego, fechaCreacion, responsable, estado):
        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE invernadero SET 
                        nombreInvernadero=%s, 
                        capacidadProduccion=%s, 
                        superficie=%s, 
                        tipoCultivo=%s, 
                        sistemaRiego=%s, 
                        fechaCreacion=%s, 
                        responsable=%s, 
                        estado=%s 
                     WHERE idInvernadero=%s"""
            cursor.execute(sql, (nombre, capacidad, superficie, tipoCultivo, sistemaRiego, fechaCreacion, responsable, estado, idInvernadero))
            self.conexion.commit()
        except Exception as e:
            print("Error al actualizar invernadero:", e)
        finally:
            cursor.close()

    def eliminarInvernadero(self, idInvernadero):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM invernadero WHERE idInvernadero=%s"
            cursor.execute(sql, (idInvernadero,))
            self.conexion.commit()
        except Exception as e:
            print("Error al eliminar invernadero:", e)
        finally:
            cursor.close()

    def filtrarPorEstado(self, estado):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM invernadero WHERE estado=%s"
            cursor.execute(sql, (estado,))
            datos = cursor.fetchall()
        except:
            datos = []
        finally:
            cursor.close()
        return datos


# ===================== MODELO DE ENFERMEDAD =====================
class EnfermedadModel:
    def __init__(self):
        self.conexion = hacerConexion()

    def agregarEnfermedad(self, nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad):
        try:
            cursor = self.conexion.cursor()
            sql = """INSERT INTO enfermedad 
                     (nombreEnfermedad, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad)
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad))
            self.conexion.commit()
        except Exception as e:
            print("Error al agregar enfermedad:", e)
        finally:
            cursor.close()

    def consultarEnfermedades(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM enfermedad")
            datos = cursor.fetchall()
        except:
            datos = []
        finally:
            cursor.close()
        return datos

    def actualizarEnfermedad(self, idEnfermedad, nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad):
        try:
            cursor = self.conexion.cursor()
            sql = """UPDATE enfermedad SET 
                        nombreEnfermedad=%s, 
                        descripcion=%s, 
                        tipoCultivo=%s, 
                        fechaDeteccion=%s, 
                        nivelGravedad=%s 
                     WHERE idEnfermedad=%s"""
            cursor.execute(sql, (nombre, descripcion, tipoCultivo, fechaDeteccion, nivelGravedad, idEnfermedad))
            self.conexion.commit()
        except Exception as e:
            print("Error al actualizar enfermedad:", e)
        finally:
            cursor.close()

    def eliminarEnfermedad(self, idEnfermedad):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM enfermedad WHERE idEnfermedad=%s"
            cursor.execute(sql, (idEnfermedad,))
            self.conexion.commit()
        except Exception as e:
            print("Error al eliminar enfermedad:", e)
        finally:
            cursor.close()

    def filtrarPorCultivo(self, tipoCultivo):
        try:
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM enfermedad WHERE tipoCultivo = %s"
            cursor.execute(sql, (tipoCultivo,))
            datos = cursor.fetchall()
        except:
            datos = []
        finally:
            cursor.close()
        return datos
