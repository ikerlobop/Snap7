import snap7
from snap7.util import *
from snap7.type import Areas


client = snap7.client.Client()
client.connect("192.168.228.27", 0, 1)

if client.get_connected():
    print("Conectado al PLC.")

    # Lectura de la marca 120.0
    data = client.read_area(Areas.MK, 0, 120, 1)
    marca_120_0 = get_bool(data, 0, 0)

    print(f"El estado de la marca 120.0 es: {'1' if marca_120_0 else '0'}")


    # Importante: Desactivar el acceso optimizado en el bloque de datos.

    # Lectura del entero en la DB1, posición 0
    try:
        data_entero = client.read_area(Areas.DB, 1, 0, 2)
        entero = get_int(data_entero, 0)
        print(f"El entero almacenado en DB1, posición 0 es: {entero}")

    # Lectura del real en la DB1, posición 2
        data_real = client.read_area(Areas.DB, 1, 2, 4)
        valor_real = get_real(data_real, 0)
        print(f"El valor real almacenado en DB1, posición 2 es: {valor_real}")

    except RuntimeError as e:
        print(f"Error al leer la DB: {e}")

    # Escritura del entero en la DB1, posición 0

    nuevo_valor_entero = int(input("Introduce un nuevo valor para el entero: "))
    set_int(data_entero, 0, nuevo_valor_entero)
    client.write_area(Areas.DB, 1, 0, data_entero)  # Escritura de 2 bytes en la posición 0

    print(f"Se ha escrito el nuevo valor {nuevo_valor_entero} en el entero en DB1, posición 0.")

    # Escritura del real en la DB1, posición 2

    nuevo_valor_real = float(input("Introduce un nuevo valor para el real: "))
    set_real(data_real, 0, nuevo_valor_real)
    client.write_area(Areas.DB, 1, 2, data_real )

    print(f"Se ha escrito el nuevo valor {nuevo_valor_real} en el entero en DB1, posicion 2.")


    # Escritura en la marca 120.1
    try:
        while True:

            user_input = input("Introduce el valor para la marca 120.1 (0 o 1, o 'q' para salir): ")

            if user_input.lower() == 'q':
                print("Saliendo...")
                break

            if user_input == '1':
                value = True
            elif user_input == '0':
                value = False
            else:
                print("Por favor, introduce '0' o '1'.")
                continue

            data = client.read_area(Areas.MK, 0, 120, 1)
            set_bool(data, 0, 1, value)
            client.write_area(Areas.MK, 0, 120, data)

            print(f"Se ha escrito {'1' if value else '0'} en la marca 120.1.")

    except KeyboardInterrupt:
        print("Programa interrumpido.")

    finally:
        client.disconnect()

else:
    print("No se pudo conectar al PLC.")
