import socket
print("=" * 45)
print("       ESCÁNER DE PUERTOS TCP EN PYTHON")
print("=" * 45)

ip = input("Ingrese la dirección IP a escanear: ")
try:
    socket.inet_aton(ip)
except socket.error:
    print("Error: la dirección IP ingresada no es válida.")
    exit()
try:
    puerto_inicial = int(input("Ingrese el puerto inicial: "))
    puerto_final = int(input("Ingrese el puerto final: "))

    if puerto_inicial < 1 or puerto_final > 65535 or puerto_inicial > puerto_final:
        print("Error: el rango de puertos no es válido.")
        exit()

except ValueError:
    print("Error: los puertos deben ser números enteros.")
    exit()

puertos_abiertos = []

for puerto in range(puerto_inicial, puerto_final + 1):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    resultado = cliente.connect_ex((ip, puerto))

    if resultado == 0:
        print(f"Puerto {puerto} ABIERTO")
        puertos_abiertos.append(puerto)

    cliente.close()
print("\n--- RESUMEN DEL ESCANEO ---")
print(f"IP analizada: {ip}")
print(f"Rango analizado: {puerto_inicial} - {puerto_final}")
print(f"Total de puertos abiertos: {len(puertos_abiertos)}")

if puertos_abiertos:
    print(f"Puertos abiertos encontrados: {puertos_abiertos}")
else:
    print("No se encontraron puertos abiertos.")    