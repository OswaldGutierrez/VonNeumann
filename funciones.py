class Funciones:
 
    def obtener_contenido(self, direccion_binaria):
        import principal  # Importación local para evitar importación circular
        if direccion_binaria in principal.memoryData:
            return principal.memoryData[direccion_binaria]
        else:
            return "Dirección no encontrada"

    def actualizarMemoria(self, clave, valor):
        import principal  # Importación local para evitar importación circular
        if len(clave) != 4 or len(valor) != 8:
            raise ValueError("La dirección debe ser un binario de 4 bits y el valor debe ser un binario de 8 bits.")
        principal.memoryData[clave] = valor
