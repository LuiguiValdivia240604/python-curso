class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = set()

    def asignar_horario(self, horario):
        if horario in self.horarios:
            return False
        self.horarios.add(horario)
        return True

class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = set()
        self.conductor = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        self.horarios.add(horario)

    def asignar_conductor(self, conductor):
        if any(h in conductor.horarios for h in self.horarios):
            return False
        self.conductor = conductor
        conductor.horarios.update(self.horarios)
        return True

class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self, placa):
        self.buses[placa] = Bus(placa)

    def agregar_conductor(self, nombre):
        self.conductores[nombre] = Conductor(nombre)

    def menu(self):
        opciones = {
            "1": lambda: self.agregar_bus(input("Placa: ")),
            "2": lambda: self.agregar_conductor(input("Nombre: ")),
            "3": lambda: self.buses.get(input("Placa: ")).asignar_ruta(input("Ruta: ")) if input("Placa: ") in self.buses else print("Bus no encontrado."),
            "4": lambda: self.buses.get(input("Placa: ")).registrar_horario(input("Horario: ")) if input("Placa: ") in self.buses else print("Bus no encontrado."),
            "5": lambda: self.buses.get(input("Placa: ")).asignar_conductor(self.conductores.get(input("Nombre: "))) if input("Placa: ") in self.buses and input("Nombre: ") in self.conductores else print("Bus o conductor no encontrado."),
            "6": exit
        }
        while True:
            print("\n1. Agregar Bus\n2. Agregar Conductor\n3. Agregar Ruta a Bus\n4. Registrar Horario a Bus\n5. Asignar Conductor a Bus\n6. Salir")
            opciones.get(input("Opción: "), lambda: print("Opción no válida"))()

Admin().menu()
