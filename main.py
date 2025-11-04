from modelo import ModeloGeneral
from vista import VistaSesion
from controlador import Controlador

# ==================== ZONA DE CÓDIGO PRINCIPAL ====================

objModelo = ModeloGeneral()
objVista = VistaSesion()
objControlador = Controlador(objVista, objModelo)


objVista.ventana.mainloop()
