# ============================================
# Este archivo inicializa el módulo "schemas".
# Reexporta los modelos de Pydantic para que
# se puedan usar fácilmente en el proyecto:
#
#   from schemas import AutoCreate, AutoOut
# ============================================

from .auto_schema import AutoBase, AutoCreate, AutoOut

# __all__ limita lo que se exporta al usar import *
__all__ = ["AutoBase", "AutoCreate", "AutoOut"]
