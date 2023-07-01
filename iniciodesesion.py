def autenticar_usuario(username, password):
    # Lista de usuarios y contraseñas permitidos
    usuarios = {
        "usuario1": "contraseña1",
        "usuario2": "contraseña2",
        "usuario3": "contraseña3"
    }

    if username in usuarios and usuarios[username] == password:
        return True
    else:
        return False

def iniciar_sesion():
    print("Sistema de Autenticación")
    print("-----------------------")

    while True:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if autenticar_usuario(username, password):
            print("Inicio de sesión exitoso. ¡Bienvenido!")
            break
        else:
            print("Credenciales incorrectas. Inténtelo nuevamente.")

iniciar_sesion()