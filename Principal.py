from Vista import VistaFormulario
from Modelo import Numero
from Controlador import Controlador

#==================== Zona De Código Principal ====================
objModelo = Numero()
objVista = VistaFormulario()

objControlador = Controlador(objVista, objModelo)
objControlador.hacerPregunta()