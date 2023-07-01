def solicitar_codigo_acceso():
    codigo_acceso = input("Ingrese el código de acceso: ")
    return codigo_acceso

def verificar_codigo_acceso(codigo_ingresado):
    codigo_correcto = "abcd1234"  # Código de acceso correcto (puedes cambiarlo)
    return codigo_ingresado == codigo_correcto

def acceder_funcionalidad():
    print("Accediendo a la funcionalidad protegida...")
    # Aquí puedes colocar el código de la funcionalidad que se desea proteger

# Ejemplo de uso
codigo_ingresado = solicitar_codigo_acceso()
if verificar_codigo_acceso(codigo_ingresado):
    acceder_funcionalidad()
else:
    print("Código de acceso incorrecto. Acceso denegado.")