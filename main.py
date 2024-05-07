import configparser
import os


def menu_configuracion(config):
    while True:
        print("\n--- Menú de Configuración ---")
        print("1. Ver Configuración")
        print("2. Cargar Configuración")
        print("3. Cambiar Parámetros")
        print("4. Guardar Configuración")
        print("5. Crear Nuevo Archivo de Configuración")
        print("6. Crear directorios")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            if config:
                ver_configuracion(config)
            else:
                print("No se ha cargado ninguna configuración.")
        elif opcion == '2':
            config = cargar_configuracion()
        elif opcion == '3':
            if config:
                config = cambiar_parametros(config)
            else:
                print("No se ha cargado ninguna configuración.")
        elif opcion == '4':
            if config:
                guardar_configuracion(config)
            else:
                print("No se ha cargado ninguna configuración.")
        elif opcion == '5':
            config = crear_configuracion()
        elif opcion == '6':
            crear_directorios(config)
        elif opcion == '0':
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


def ver_configuracion(config):
    for section in config.sections():
        print()
        print(f"--- {section} ---")
        print()
        for key, value in config.items(section):
            print(f"{key}: {value}")
        print()


def cargar_configuracion():
    archivo_config = input("Introduce el nombre del archivo de configuración: ")
    config = configparser.ConfigParser()
    try:
        config.read(archivo_config)
        print("¡Configuración cargada")
        return config
    except FileNotFoundError:
        print("El archivo de configuración no existe.")
        return None
    except configparser.Error as e:
        print("Error al leer el archivo de configuración:", e)
        return None


def cambiar_parametros(config):
    seccion = input("Introduce la sección del parámetro que quieres cambiar: ")
    parametro = input("Introduce el nombre del parámetro que quieres cambiar: ")
    valor_actual = config.get(seccion, parametro)
    print(f"El valor actual de {parametro} es: {valor_actual}")
    nuevo_valor = input("Introduce el nuevo valor: ")
    config.set(seccion, parametro, nuevo_valor)
    print("¡Valor cambiado con éxito!")
    return config


def crear_configuracion():
    config = configparser.ConfigParser()
    config['PARAMETROS'] = {}
    print("Introduce los valores para los siguientes parámetros:")
    for parametro in ['DIR_INIT', 'DIR_DST', 'MIDA_PETITA', 'MIDA_MITJANA', 'EXTENSIO_FILTRADA', 'DIR_QUARANTENA', 'ZIP_FILE', 'REPORT_FILE']:
        valor = input(f"{parametro}: ")
        config['PARAMETROS'][parametro] = valor
    print("¡Configuración creada con éxito!")
    #Guardar configuración
    archivo_nuevo = input("Introduce el nombre del archivo de configuración a crear o sobrescribir: ")
    confirmacion = input(f"¿Estás seguro que quieres guardar la configuración en {archivo_nuevo}? (S/N): ")
    if confirmacion.upper() == 'S':
        with open(archivo_nuevo, 'w') as configfile:
            config.write(configfile)
        print("¡Configuración guardada con éxito!")


def crear_directorios(config):
    dir_dst = config.get('PARAMETROS', 'DIR_DST')
    iniciales = input("Pon tus iniciales para dar nombre a los directorios: ")
    try:
        if not os.path.exists(dir_dst):
            os.makedirs(dir_dst)
            print(f"Directorio principal {dir_dst} creado correctamente.")
        for user in [f"{iniciales}1", f"{iniciales}2", f"{iniciales}3"]:
            user_dir = os.path.join(dir_dst, user)
            for size in ['petit', 'mitja', 'gran']:
                size_dir = os.path.join(user_dir, size)
                if not os.path.exists(size_dir):
                    os.makedirs(size_dir)
                    print(f"Directorio {size_dir} creado correctamente para el usuario {user}.")
    except Exception as e:
        print(f"Error al crear directorios: {e}")


if __name__ == "__main__":
    config = None
    menu_configuracion(config)
