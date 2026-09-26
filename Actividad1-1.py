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

    def __repr__(self):
        return (
            f"Cliente(cedula={self.cedula}, nombre={self.nombre}, "
            f"tipo_cliente={self.tipo_cliente}, "
            f"tipo_atencion={self.tipo_atencion}, "
            f"cantidad={self.cantidad}, "
            f"valor_total={self.valor_total})"
        )


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


def obtener_valor_total(cliente):
    return cliente.valor_total


def buscar_cliente(clientes, cedula):

    for cliente in clientes:

        if cliente.cedula == cedula:
            return cliente

    return None


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
    fecha_cita = input("Fecha de la cita: ")

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


total_clientes = len(clientes)

ingresos_totales = 0
clientes_extraccion = 0

for cliente in clientes:

    ingresos_totales = ingresos_totales + cliente.valor_total

    if cliente.tipo_atencion == "Extraccion":
        clientes_extraccion = clientes_extraccion + 1


# Ordenar de mayor a menor por el valor total
clientes.sort(key=obtener_valor_total, reverse=True)


print()
print("RESULTADOS")
print("Total de clientes:", total_clientes)
print("Ingresos totales:", ingresos_totales)
print("Clientes para extraccion:", clientes_extraccion)


print()
print("CLIENTES ORDENADOS POR VALOR TOTAL")

for cliente in clientes:
    print(cliente)


print()
cedula_buscar = input("Ingrese la cedula del cliente que desea buscar: ")

cliente_encontrado = buscar_cliente(clientes, cedula_buscar)

if cliente_encontrado != None:

    print()
    print("Cliente encontrado:")
    print(cliente_encontrado)

else:

    print()
    print("Cliente no encontrado")