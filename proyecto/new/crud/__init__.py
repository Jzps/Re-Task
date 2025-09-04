# ============================================
# Este archivo inicializa el módulo "crud"
# Aquí reexportamos las funciones principales
# para que se puedan usar fácilmente con:
#
#   from crud import crear_auto, obtener_autos, eliminar_auto
# ============================================

from .auto_crud import crear_auto, obtener_autos, eliminar_auto

# __all__ limita lo que se exporta cuando se usa import *
__all__ = ["crear_auto", "obtener_autos", "eliminar_auto"]
