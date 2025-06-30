class ShapeException(Exception):
    """Excepción base para errores de figuras geométricas."""
    pass

class NegativeDimensionError(ShapeException):
    def __init__(self, message="Error: Las dimensiones deben ser positivas."):
        super().__init__(message)

class InvalidPointError(ShapeException):
    def __init__(self, message="Error: Coordenadas del punto no válidas."):
        super().__init__(message)

class InvalidShapeError(ShapeException):
    def __init__(self, message="Error: La figura no es válida. Verifique los datos."):
        super().__init__(message)

class ShapeNotInitializedError(ShapeException):
    def __init__(self, message="Error: La figura no está completamente inicializada."):
        super().__init__(message)

class UndefinedPropertyError(ShapeException):
    def __init__(self, message="Error: La propiedad geométrica solicitada no está definida."):
        super().__init__(message)
