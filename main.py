import configparser
import os

# Función para mostrar la configuración actual
def ver_configuracion(config):
    for section in config.sections():
        print(f"--- {section} ---")
        for key, value in config.items(section):
            print(f"{key}: {value}")
        print()

# Función para cargar la configuración desde un archivo
def cargar_configuracion():
    archivo_config = input("Introduce el nombre del archivo de configuración: ")
    config = configparser.ConfigParser()
    try:
        config.read(archivo_config)
        print("¡Configuración cargada con éxito!")
        return config
    except FileNotFoundError:
        print("Error: el archivo de configuración no existe.")
        return None
    except configparser.Error as e:
        print("Error al leer el archivo de configuración:", e)
        return None

# Función para cambiar un parámetro de configuración
def cambiar_parametro(config):
    seccion = input("Introduce la sección del parámetro que quieres cambiar: ")
    parametro = input("Introduce el nombre del parámetro que quieres cambiar: ")
    valor_actual = config.get(seccion, parametro)
    print(f"El valor actual de {parametro} es: {valor_actual}")
    nuevo_valor = input("Introduce el nuevo valor: ")
    config.set(seccion, parametro, nuevo_valor)
    print("¡Valor cambiado con éxito!")
    return config

# Función para guardar la configuración en un archivo
def guardar_configuracion(config):
    archivo_nuevo = input("Introduce el nombre del archivo de configuración a crear: ")
    confirmacion = input(f"¿Estás seguro que quieres guardar la configuración en {archivo_nuevo}? (S/N): ")
    if confirmacion.upper() == 'S':
        with open(archivo_nuevo, 'w') as configfile:
            config.write(configfile)
        print("¡Configuración guardada con éxito!")

# Función para crear un nuevo archivo de configuración con valores ingresados por el usuario
def crear_configuracion():
    config = configparser.ConfigParser()
    config['PARAMETROS'] = {}
    print("Introduce los valores para los siguientes parámetros:")
    for parametro in ['DIR_INIT', 'DIR_DST', 'in_in', 'MIDA_PETITA', 'MIDA_MITJANA', 'EXTENSIO_FILTRADA', 'DIR_QUARANTENA', 'ZIP_FILE', 'REPORT_FILE']:
        valor = input(f"{parametro}: ")
        config['PARAMETROS'][parametro] = valor
    print("¡Configuración creada con éxito!")
    return config

# Función principal del menú de configuración
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
                config = cambiar_parametro(config)
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

def crear_directorios(config):
    dir_dst = config.get('PARAMETROS', 'DIR_DST')

    try:
        # Crear el directorio principal si no existe
        if not os.path.exists(dir_dst):
            os.makedirs(dir_dst)
            print(f"Directorio principal {dir_dst} creado correctamente.")

        # Crear subdirectorios para cada usuario y tamaño
        for user in [f"tusinicales1", f"tusinicales2", f"tusinicales13"]:
            user_dir = os.path.join(dir_dst, user)
            for size in ['petit', 'mitja', 'gran']:
                size_dir = os.path.join(user_dir, size)
                if not os.path.exists(size_dir):
                    os.makedirs(size_dir)
                    print(f"Directorio {size_dir} creado correctamente para el usuario {user}.")
    except Exception as e:
        print(f"Error al crear directorios: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    config = None
    # Ejecuta el menú de configuración
    menu_configuracion(config)
