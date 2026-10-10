from collections import deque
from datetime import datetime


class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente,
                 tipo_atencion, cantidad, prioridad, fecha_cita,
                 valor_cita, valor_atencion, valor_total):

        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        self.valor_cita = valor_cita
        self.valor_atencion = valor_atencion
        self.valor_total = valor_total


def calcular_valor_cita(tipo_cliente):

    if tipo_cliente == "Particular":
        return 80000

    elif tipo_cliente == "EPS":
        return 5000

    elif tipo_cliente == "Prepagada":
        return 30000


def calcular_valor_atencion(tipo_cliente, tipo_atencion):

    if tipo_cliente == "Particular":

        if tipo_atencion == "Limpieza":
            return 60000

        elif tipo_atencion == "Calzas":
            return 80000

        elif tipo_atencion == "Extraccion":
            return 100000

        elif tipo_atencion == "Diagnostico":
            return 50000

    elif tipo_cliente == "EPS":

        if tipo_atencion == "Limpieza":
            return 0

        elif tipo_atencion == "Calzas":
            return 40000

        elif tipo_atencion == "Extraccion":
            return 40000

        elif tipo_atencion == "Diagnostico":
            return 0

    elif tipo_cliente == "Prepagada":

        if tipo_atencion == "Limpieza":
            return 0

        elif tipo_atencion == "Calzas":
            return 10000

        elif tipo_atencion == "Extraccion":
            return 10000

        elif tipo_atencion == "Diagnostico":
            return 0


def obtener_fecha_cita(cliente):
    return datetime.strptime(cliente.fecha_cita, "%d/%m/%Y")


# LISTA INICIAL DE CLIENTES

clientes = []

cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))

for i in range(cantidad_clientes):

    print()
    print("Cliente", i + 1)

    cedula = input("Cedula: ")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")

    tipo_cliente = input(
        "Tipo de cliente (Particular, EPS, Prepagada): "
    )

    tipo_atencion = input(
        "Tipo de atencion (Limpieza, Calzas, Extraccion, Diagnostico): "
    )

    cantidad = int(input("Cantidad: "))

    prioridad = input("Prioridad (Normal, Urgente): ")

    fecha_cita = input("Fecha de la cita (DD/MM/AAAA): ")

    valor_cita = calcular_valor_cita(tipo_cliente)

    valor_atencion = calcular_valor_atencion(
        tipo_cliente,
        tipo_atencion
    )

    valor_total = valor_cita + (valor_atencion * cantidad)

    cliente = Cliente(
        cedula,
        nombre,
        telefono,
        tipo_cliente,
        tipo_atencion,
        cantidad,
        prioridad,
        fecha_cita,
        valor_cita,
        valor_atencion,
        valor_total
    )

    clientes.append(cliente)


# CONSTRUIR LA PILA DE CONTINGENCIA

pila_urgentes = deque()

clientes_urgentes = []

for cliente in clientes:

    if cliente.tipo_atencion == "Extraccion" and cliente.prioridad == "Urgente":
        clientes_urgentes.append(cliente)


# ORDENAR LOS CLIENTES URGENTES DE LA FECHA MAS LEJANA A LA MAS CERCANA

clientes_urgentes.sort(key=obtener_fecha_cita, reverse=True)

# AGREGAR LOS CLIENTES A LA PILA

for cliente in clientes_urgentes:
    pila_urgentes.append(cliente)


# INFORME DE LA PILA

print()
print("======================================")
print("INFORME DE LA PILA DE CONTINGENCIA")
print("======================================")

if pila_urgentes:

    print("Clientes con extraccion y prioridad urgente:")
    print()

    numero = 1

    for cliente in reversed(pila_urgentes):

        print("Cliente:", numero)
        print("Cedula:", cliente.cedula)
        print("Nombre:", cliente.nombre)
        print("Telefono:", cliente.telefono)
        print("Tipo de atencion:", cliente.tipo_atencion)
        print("Prioridad:", cliente.prioridad)
        print("Fecha de la cita:", cliente.fecha_cita)
        print()

        numero += 1

else:
    print("No hay clientes que cumplan las condiciones de la pila.")


# CONSTRUIR LA COLA DE ATENCION

cola_agenda = deque()

# ORDENAR TODOS LOS CLIENTES POR FECHA DE CITA

clientes.sort(key=obtener_fecha_cita)

# AGREGAR LOS CLIENTES A LA COLA RESPETANDO LA AGENDA

for cliente in clientes:
    cola_agenda.append(cliente)


# INFORME DE LA COLA DE ATENCION

print()
print("======================================")
print("AGENDA DE ATENCION DEL CONSULTORIO")
print("======================================")

if cola_agenda:

    for cliente in cola_agenda:

        print(
            "Fecha:", cliente.fecha_cita,
            "| Nombre:", cliente.nombre,
            "| Atencion:", cliente.tipo_atencion,
            "| Prioridad:", cliente.prioridad
        )

else:
    print("No hay clientes registrados en la agenda.")


# ATENDER LOS CLIENTES SEGUN EL ORDEN DE LA COLA

print()
print("======================================")
print("ATENCION DE CLIENTES")
print("======================================")

while cola_agenda:

    cliente_atendido = cola_agenda.popleft()

    print(
        "Atendiendo a:",
        cliente_atendido.nombre,
        "| Fecha de cita:",
        cliente_atendido.fecha_cita
    )

print()
print("Todos los clientes de la agenda han sido atendidos.")