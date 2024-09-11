import tkinter as tk
import particion
from contBinario import ContadorBinario  # Asegúrate de que la ruta sea correcta
from operaciones import Operaciones
from funciones import Funciones


# Datos iniciales
memoryDataContenido = [
    "00000101",  # Dirección 0000
    "00010110",  # Dirección 0001
    "00110110",  # Dirección 0010
    "01100111",  # Dirección 0011 (resultado de la operación)
    "01110000",  # Dirección 0100
    "00001000",  # Dirección 0101
    "00000011",  # Dirección 0110
    "00000000",  # Dirección 0111
]

memoryDataDireccion = [
    "0000",
    "0001",
    "0010",
    "0011",
    "0100",
    "0101",
    "0110",
    "0111",
]
memoryData = dict(zip(memoryDataDireccion, memoryDataContenido))

# Dicc con las instrucciones y sus significados
intruccionData = {
    "0000" : "+",
    "0001" : "-",
    "0010" : "*",
    "0011" : "^",
    "0100" : "&",
    "0101" : "|",
    "0110" : "M",
    "0111" : "...",
}

# Crear una instancia del contador binario
contador = ContadorBinario()
operaciones = Operaciones()
funciones = Funciones()

# Variables globales
clickContador = 0

def actualizarTablaMemoria():
    memoryTable.config(state=tk.NORMAL)  # Habilitar edición temporalmente para actualizar texto
    memoryTable.delete(1.0, tk.END)  # Limpiar el contenido actual

    # Encabezado de la tabla
    memoryTable.insert(tk.END, 
        "Dir    | Contenido\n"
        "--------------------\n"
    )

    # Insertar cada par clave-valor del diccionario en la tabla
    for direccion, contenido in memoryData.items():
        memoryTable.insert(tk.END, f"{direccion}   | {contenido}\n")

    memoryTable.config(state=tk.DISABLED)  # Deshabilitar edición para mostrar solo información

def siguientePaso():
    global clickContador

    clickContador += 1  # Incrementar el número de clics

    if clickContador == 1:
        # Paso 1: Mostrar el valor de contPrograma
        valorContador = contador.contador
        contPrograma.config(text=valorContador)
        rDirecciones.config(text=valorContador)  # Opcional, si también quieres actualizar rDirecciones con el valor de contPrograma

    elif clickContador == 2:
        # Paso 2: Actualizar rDatos con el valor del diccionario memory_data
        direccionTabla = rDirecciones.cget("text")  # Obtener el texto actual de rDirecciones
        valorDato = memoryData.get(direccionTabla, "No encontrado")  # Buscar el valor en el diccionario
        rDatos.config(text=valorDato)  # Actualizar rDatos con el valor encontrado

    elif clickContador == 3:
        # Paso 3: Actualizar rInstrucciones con el valor de rDatos
        valorRegistroDatos = rDatos.cget("text")  # Obtener el texto actual de rDatos
        rInstrucciones.config(text=valorRegistroDatos)  # Actualizar rInstrucciones con el valor de rDatos
        
    elif clickContador == 4:
        # Paso 4: Actualizar decodificador con los primeros 4 bits de rInstrucciones
        valorRegistroIntrucciones = rInstrucciones.cget("text")
        valorDecodificador = particion.primeros_4_bits(valorRegistroIntrucciones)
        signoDecodificador = intruccionData.get(valorDecodificador)
        decodificador.config(text=signoDecodificador)
        
        # Verificar si el valor del decodificador es 'F' y deshabilitar el botón si es así
        if signoDecodificador == "...":
            next_button.config(state=tk.DISABLED)
            return  # Detener la ejecución

    elif clickContador == 5:
        # Paso 5: Actualizar rDirecciones con los últimos 4 bits de rInstrucciones
        valorUltimoRegistroInstrucciones = rInstrucciones.cget("text")
        valor2Direcciones = particion.ultimos_4_bits(valorUltimoRegistroInstrucciones)
        rDirecciones.config(text=valor2Direcciones)
        
    elif clickContador == 6:
        # Paso 6: Actualizar rDatos con el valor del diccionario memory_data
        operacion = decodificador.cget("text")
        if operacion != "M":
            direccionTabla = rDirecciones.cget("text")  # Obtener el texto actual de rDirecciones
            valorDato = memoryData.get(direccionTabla, "No encontrado")  # Buscar el valor en el diccionario
            rDatos.config(text=valorDato)  # Actualizar rDatos con el valor encontrado
        else:
            valorAcum = acumulador.cget("text")
            rDatos.config(text=valorAcum)
            claveDiccionario = rDirecciones.cget("text")
            valorDiccionario = rDatos.cget("text")
            memoryData[claveDiccionario] = valorDiccionario
        
        
    elif clickContador == 7:
        # Paso 7: Actualizar rEntrada con el valor de rDatos
        operacion = decodificador.cget("text")
        if operacion != "M":  # Solo actualiza rEntrada si la operación no es M
            valorDato = rDatos.cget("text")
            rEntrada.config(text=valorDato)
        else:
            valorContador = contador.incrementar()  # Incrementar y obtener el nuevo valor
            contPrograma.config(text=valorContador)
            rDirecciones.config(text=valorContador)  # Opcional, si también quieres actualizar rDirecciones con el valor de contPrograma
            
            # Reiniciar el clickContador para repetir los pasos del 2 al 9
            clickContador = 1
        
        
    elif clickContador == 8:
        valorAcumulador = acumulador.cget("text")
        valorEntrada = rEntrada.cget("text")
        operacion = decodificador.cget("text")
       
        if operacion == "+":
            valorResultado = operaciones.sumarBinarios(valorAcumulador, valorEntrada)
        elif operacion == "-":
            valorResultado = operaciones.restarBinarios(valorAcumulador, valorEntrada)
        elif operacion == "^":
            valorResultado = operaciones.exponenteBinario(valorAcumulador, valorEntrada)
        elif operacion == "M":
            valorClave = rDirecciones.cget("text")
            valorValor = acumulador.cget("text")
            valorResultado = funciones.actualizarMemoria(valorClave, valorValor)

        acumulador.config(text=valorResultado)
        
    elif clickContador == 9:
        # Paso 9: Incrementar el contador de programa
        valorContador = contador.incrementar()  # Incrementar y obtener el nuevo valor
        contPrograma.config(text=valorContador)
        rDirecciones.config(text=valorContador)  # Opcional, si también quieres actualizar rDirecciones con el valor de contPrograma
        
        # Reiniciar el clickContador para repetir los pasos del 2 al 9
        clickContador = 1

    print("Click número: ", clickContador)
    actualizarTablaMemoria()  # Actualizar componentes como ejemplo





# Configuración básica de la ventana principal
root = tk.Tk()
root.title("Simulación de Arquitectura Von Neumann")

# Hacer que la ventana sea responsiva
root.rowconfigure(0, weight=1)
root.columnconfigure([0, 1, 2], weight=1)
root.rowconfigure(1, weight=1)

# Unidad de Control (parte superior izquierda)
frame_control = tk.Frame(root, bg="#87CEEB", bd=2, relief="groove", padx=10, pady=10)
frame_control.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frame_control, text="Unidad de Control").pack()

# Decodificador
tk.Label(frame_control, text="Decodificador").pack()
decodificador = tk.Label(frame_control, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
decodificador.pack()

# Contador de Programa
tk.Label(frame_control, text="Contador de Programa").pack()
contPrograma = tk.Label(frame_control, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
contPrograma.pack()

# Instrucciones
tk.Label(frame_control, text="Instrucciones").pack()
rInstrucciones = tk.Label(frame_control, bg="white", width=20, height=4, anchor="center", font=("Helvetica", 16))
rInstrucciones.pack()

# Unidad Aritmético-Lógica (parte superior derecha)
frame_alu = tk.Frame(root, bg="#98FB98", bd=2, relief="groove", padx=10, pady=10)
frame_alu.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
tk.Label(frame_alu, text="Unidad Aritmético-Lógica").pack()

# Acumulador
tk.Label(frame_alu, text="Acumulador").pack()
acumulador = tk.Label(frame_alu, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
acumulador.pack()

# Registro de Entrada
tk.Label(frame_alu, text="Registro de Entrada").pack()
rEntrada = tk.Label(frame_alu, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
rEntrada.pack()

# Memoria (parte inferior)
frame_memory = tk.Frame(root, bg="#FFDAB9" , bd=2, relief="groove", padx=10, pady=10)
frame_memory.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
tk.Label(frame_memory, text="Memoria").pack()

# Registro de Direcciones (parte izquierda)
frame_address = tk.Frame(frame_memory, bd=1, relief="sunken", padx=10, pady=10)
frame_address.pack(side=tk.LEFT, fill=tk.Y)
tk.Label(frame_address, text="Registro de Direcciones").pack()
rDirecciones = tk.Label(frame_address, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
rDirecciones.pack()

# Tabla de Memoria (parte inferior)
memoryTable = tk.Text(frame_memory, bg="white", width=40, height=10, wrap=tk.NONE)
memoryTable.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Registro de Datos (parte derecha)
frame_data = tk.Frame(frame_memory, bd=1, relief="sunken", padx=10, pady=10)
frame_data.pack(side=tk.RIGHT, fill=tk.Y)
tk.Label(frame_data, text="Registro de Datos").pack()
rDatos = tk.Label(frame_data, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
rDatos.pack()

# Inicializar la tabla de memoria
actualizarTablaMemoria()

# Botón "Siguiente" en la parte inferior
next_button = tk.Button(root, text="Siguiente", command=siguientePaso)
next_button.grid(row=2, column=0, columnspan=3, pady=10)

# Loop principal de la aplicación
root.mainloop()