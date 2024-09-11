def primeros_4_bits(bin_num):
    # Asegurarse de que el número binario sea de 8 bits
    bin_num = bin_num.zfill(8)
    
    # Obtener los primeros 4 bits
    primeros_4 = bin_num[:4]
    
    return primeros_4


def ultimos_4_bits(bin_num):
    # Asegurarse de que el número binario sea de 8 bits
    bin_num = bin_num.zfill(8)
    
    # Obtener los últimos 4 bits
    ultimos_4 = bin_num[-4:]
    
    return ultimos_4