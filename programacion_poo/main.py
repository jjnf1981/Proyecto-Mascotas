# ============================================
# PROGRAMA POO - GESTIÓN DE MASCOTAS
# ============================================

# Importar la clase Mascota
from mascota import Mascota

print("\n🐾 Bienvenido al programa de gestión de mascotas 🐾")
print("===================================================\n")

#Creamos los objetos de tipo Mascota
print("--- Creando mascotas ---\n")
mascota1 = Mascota("Firulais", "Perro", 5)
mascota2 = Mascota("Michi", "Gato", 3)

#Mostramos la información de las mascotas
print("--- Mostrando información de las mascotas ---\n")
mascota1.mostrar_informacion()
mascota2.mostrar_informacion()

#Hacemos que las mascotas hagan sonidos
print("--- Sonidos de las mascotas ---\n")
mascota1.hacer_sonido()
mascota2.hacer_sonido()

print("\nGracias por usar el programa de gestión de mascotas")
print("===================================================")