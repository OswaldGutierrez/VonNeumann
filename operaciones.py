class Operaciones:
    
    def sumarBinarios(self, bin1, bin2):
        bin1 = bin1.zfill(8)
        bin2 = bin2.zfill(8)
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        resultado_decimal = num1 + num2
        resultado_decimal = resultado_decimal % 256
        resultado_binario = bin(resultado_decimal)[2:].zfill(8)
        return resultado_binario

    def restarBinarios(self, bin1, bin2):
        bin1 = bin1.zfill(8)
        bin2 = bin2.zfill(8)
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        resultado_decimal = num1 - num2
        resultado_decimal = resultado_decimal % 256
        resultado_binario = bin(resultado_decimal)[2:].zfill(8)
        return resultado_binario

    def exponenteBinario(self, bin_num, bin_exp):
        bin_num = bin_num.zfill(8)
        bin_exp = bin_exp.zfill(8)
        num = int(bin_num, 2)
        exponente = int(bin_exp, 2)
        resultado_decimal = num ** exponente
        resultado_decimal = resultado_decimal % 256
        resultado_binario = bin(resultado_decimal)[2:].zfill(8)
        return resultado_binario
