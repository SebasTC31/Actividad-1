from datetime import datetime

def obtener_fecha_hora_actual():
    ahora = datetime.now()

    fecha_hora_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_hora_formateada

print("Hello, World!")
print(obtener_fecha_hora_actual())
