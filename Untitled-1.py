def hola_mundo(opcion):
    if opcion == 1:
        print("Hola mundo")
    elif opcion == 2:
        print("Hola mundo!")
    else:
        print("Opción no válida")

def main():
    print("Bienvenido al programa")
    print("1. Hola mundo")
    print("2. Hola mundo!")
    opcion = int(input("Seleccione una opción (1 o 2): "))
    hola_mundo(opcion)

if __name__ == "__main__":
    main()