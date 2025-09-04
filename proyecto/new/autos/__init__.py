# ============================================
# Este archivo hace que la carpeta "autos" sea
# tratada como un módulo en Python.
# 
# Aquí se importan las clases principales para
# que puedan usarse con solo hacer:
#    from autos import Auto, AutoNuevo, AutoUsado, AutoElectrico
# ============================================

from .base import Auto
from .tipos import AutoNuevo, AutoUsado, AutoElectrico

# __all__ define explícitamente qué clases estarán disponibles
# al hacer un import *
__all__ = ["Auto", "AutoNuevo", "AutoUsado", "AutoElectrico"]
