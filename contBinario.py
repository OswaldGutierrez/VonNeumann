class ContadorBinario:
    def __init__(self):
        # Inicializar el contador en '0000'
        self.contador = '0000'
    
    def incrementar(self):
        # Convertir el contador binario a decimal
        num = int(self.contador, 2)
        
        # Incrementar el valor
        num += 1
        
        # Asegurarse de que el valor no exceda 7 (0111 en binario)
        if num > 7:
            num = 0
        
        # Convertir el valor de vuelta a binario y asegurarse de que tenga 4 bits
        self.contador = bin(num)[2:].zfill(4)
        
        return self.contador