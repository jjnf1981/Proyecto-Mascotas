# ============================================
# CLASE MASCOTA
# ============================================

class Mascota:
    def __init__(self, nombre, especie, edad):
        #Inicializa los atributos de la mascota        
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        #Se presenta los datos de la mascota por pantalla
        print("=== DATOS DE LA MASCOTA ===")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print("============================\n")
    
    def hacer_sonido(self):
        #Hace un sonido dependiendo de la especie de la mascota        
        if self.especie == "Perro":
            print(f"🔊 {self.nombre} dice: ¡Guau! 🐕")
        elif self.especie == "Gato":
            print(f"🔊 {self.nombre} dice: ¡Miau! 🐈")