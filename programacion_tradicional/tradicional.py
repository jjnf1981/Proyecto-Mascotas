# ============================================
# PROGRAMA TRADICIONAL - GESTIÓN DE MASCOTAS
# ============================================

def registrar_mascota():
    #Solicita los datos de la mascota por teclado
    print("\n=== REGISTRO DE MASCOTA ===")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota (perro, gato, etc): ")
    edad = input("Ingrese la edad de la mascota: ")
    print("============================")
    return nombre, especie, edad

def mostrar_mascota(nombre, especie, edad):
    #Se presenta los datos de la mascota por pantalla
    print("\n=== DATOS DE LA MASCOTA ===")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad} años")
    print("============================")

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

print("\n🐾 Bienvenido al programa de gestión de mascotas 🐾")
print("===================================================\n")

#Registrar la mascota
nombre, especie, edad = registrar_mascota()
    
#Mostrar los datos de la mascota
mostrar_mascota(nombre, especie, edad)
    
print("\nGracias por usar el programa de gestión de mascotas")
print("===================================================")