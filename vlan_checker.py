def verificar_vlan():
    try:
        vlan = int(input("Ingresa el número de VLAN: "))
        if 1 <= vlan <= 1005:
            print("La VLAN pertenece al rango normal.")
        elif 1006 <= vlan <= 4094:
            print("La VLAN pertenece al rango extendido.")
        else:
            print("La VLAN está fuera del rango válido.")
    except ValueError:
        print("Debes ingresar un número válido.")

if __name__ == "__main__":
    verificar_vlan()
