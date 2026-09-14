gastos_negocio = [

    {"descripcion" : "Renta del local", "monto": 15000.00, "categoria" : "Renta"},
    {"descripcion" : "Compra de insumos", "monto": 3500.00, "categoria" : "Insumos"},
    {"descripcion" : "Publicidad en redes", "monto": 1200.00, "categoria" : "Marketing"},

]

#Mostrar los Gastos del Negocio
# print("Gastos del negocio:")
# for gasto in gastos_negocio:
#     print(f"Descripcion: {gasto['descripcion']}, Monto: {gasto['monto']}, Categoria: {gasto['categoria']}")

#Funcion que agrega un gasto al negocio  usa como parametroos los gatos, la descripcion, el monto y categoria del gasto. 
def agregar_gasto(gastos, descripcion, monto, categoria):

    nuevo_gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
    gastos.append(nuevo_gasto)
    return nuevo_gasto

#funcion que muestra los gastos del negocio, recibe como parametro la lista de diccionario gastos y recorre la lista mostrando la descripcion, categoria y monto de cada gasto.
def ver_gastos(gastos):
    for gasto in gastos:
        print(f"{gasto['descripcion']} ({gasto['categoria']}) : ${gasto['monto']}")

# Busca todos los gastos de una categoria, sin importar mayusculas o minusculas.
def buscar_por_categoria(gastos, categoria_buscada):
    categoria_normalizada = categoria_buscada.lower()
    resultado = []

    for gasto in gastos:
        if gasto["categoria"].lower() == categoria_normalizada:
            resultado.append(gasto)

    return resultado

# Suma el monto de todos los gastos de una categoria, sin importar mayusculas o minusculas.
def total_por_categoria(gastos, categoria_busqueda):
    categoria_normalizada = categoria_busqueda.lower()
    total = 0

    for gasto in gastos:
        if gasto["categoria"].lower() == categoria_normalizada:
            total += gasto["monto"]

    return total

# print("\n-----Gastos del negocio-----")
# ver_gastos(gastos_negocio)
# agregar_gasto(gastos_negocio, "Compra de tijeras", 800.00, "Insumos")
# print("\n-----Gastos del negocio despues de agregar un nuevo gasto-----")
# ver_gastos(gastos_negocio)

# print("\n-----Resultados de busqueda por categoria-----")
# print(buscar_por_categoria(gastos_negocio, "INSUMOS"))

# print("\n-----Resultados del Total por categoria-----")
# print(total_por_categoria(gastos_negocio, "insumos"))

while True:
    print("\nMenu:")
    print("0. Salir")
    print("1. Ver todos los gastos")
    print("2. Agregar un gasto nuevo")
    print("3. Buscar gastos por categoria")
    opcion = input("Ingrese una opción: ")

    if opcion == "0":
        print("Hasta luego!")
        break
    elif opcion == "1":
        ver_gastos(gastos_negocio)
    elif opcion == "2":
        descripcion = input("Ingrese la descripción: ")
        monto = input("Ingrese el monto: ")
        categoria = input("Ingrese la categoría: ")
        agregar_gasto(gastos_negocio, descripcion, monto, categoria)
    elif opcion == "3":
        categoria = input("Ingrese la categoría a buscar: ")
        resultados = buscar_por_categoria(gastos_negocio, categoria)

        if not resultados:
            print(f"No se encontraron gastos en la categoría '{categoria}'.")
        else:
            for gasto in resultados:
                print(f"{gasto['descripcion']} ({gasto['categoria']}) : ${gasto['monto']}")
