def ip_a_binario(ip):
    partes_binarias = [format(int(parte), '08b') for parte in ip.split('.')]
    return '.'.join(partes_binarias)

def ip_a_hexadecimal(ip):
    partes_hexadecimales = [format(int(parte), '02X') for parte in ip.split('.')]
    return '.'.join(partes_hexadecimales)

def ip_a_octal(ip):
    partes_octales = [format(int(parte), '03o') for parte in ip.split('.')]
    return '.'.join(partes_octales)

def determinar_clase_ip(ip):
    primer_octeto = int(ip.split('.')[0])
    if 1 <= primer_octeto <= 126:
        return 'A'
    elif 128 <= primer_octeto <= 191:
        return 'B'
    elif 192 <= primer_octeto <= 223:
        return 'C'
    elif 224 <= primer_octeto <= 239:
        return 'D (Multicast)'
    elif 240 <= primer_octeto <= 255:
        return 'E (Experimental)'

def calcular_mascara_subred(clase_ip):
    if clase_ip == 'A':
        return '255.0.0.0'
    elif clase_ip == 'B':
        return '255.255.0.0'
    elif clase_ip == 'C':
        return '255.255.255.0'
    else:
        return 'N/A'

def calcular_numero_mascara(mascara_subred):
    partes_mascara = mascara_subred.split('.')
    bits_mascara = sum(bin(int(parte)).count('1') for parte in partes_mascara)
    return bits_mascara

direccion_ip = input("Ingrese una dirección IP: ")

ip_binaria = ip_a_binario(direccion_ip)
ip_hexadecimal = ip_a_hexadecimal(direccion_ip)
ip_octal = ip_a_octal(direccion_ip)

clase_ip = determinar_clase_ip(direccion_ip)
mascara_subred = calcular_mascara_subred(clase_ip)
numero_mascara = calcular_numero_mascara(mascara_subred)

print(f"Dirección IP en binario: {ip_binaria}")
print(f"Dirección IP en hexadecimal: {ip_hexadecimal}")
print(f"Dirección IP en octal: {ip_octal}")
print(f"Clase de la dirección IP: {clase_ip}")
print(f"Máscara de subred: {mascara_subred}")
print(f"Número de máscara: /{numero_mascara}")
