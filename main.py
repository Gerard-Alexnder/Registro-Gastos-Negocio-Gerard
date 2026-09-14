gastos_negocio = [

    {"descripcion" : "Renta del local", "monto": 15000.00, "categoria" : "Renta"},
    {"descripcion" : "Compra de insumos", "monto": 3500.00, "categoria" : "Insumos"},
    {"descripcion" : "Publicidad en redes", "monto": 1200.00, "categoria" : "Marketing"},

]

#Mostrar los Gastos del Negocio
# print("Gastos del negocio:")
# for gasto in gastos_negocio:
#     print(f"Descripcion: {gasto['descripcion']}, Monto: {gasto['monto']}, Categoria: {gasto['categoria']}")

class GestorGastos:
    def __init__(self, gastos):
        self.gastos = gastos

    def ver_gastos(self):
        for gasto in self.gastos:
            print(f"{gasto['descripcion']} ({gasto['categoria']}) : ${gasto['monto']}")

    def buscar_por_categoria(self, categoria_buscada):
        categoria_normalizada = categoria_buscada.lower()
        resultado = []
    
        for gasto in self.gastos:
            if gasto["categoria"].lower() == categoria_normalizada:
                resultado.append(gasto)
    
        return resultado

    def total_por_categoria(self, categoria_busqueda):
        categoria_normalizada = categoria_busqueda.lower()
        total = 0

        for gasto in self.gastos:
            if gasto["categoria"].lower() == categoria_normalizada:
                total += gasto["monto"]

        return total

    def agregar_gasto(self, descripcion, monto_texto, categoria):
        try:
            monto = float(monto_texto)
        except ValueError:
            print("El monto debe ser un numero. Gasto no agregado.")
            return None

        nuevo_gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
        self.gastos.append(nuevo_gasto)
        return nuevo_gasto



   



# print("\n-----Gastos del negocio-----")
# ver_gastos(gastos_negocio)
# agregar_gasto(gastos_negocio, "Compra de tijeras", 800.00, "Insumos")
# print("\n-----Gastos del negocio despues de agregar un nuevo gasto-----")
# ver_gastos(gastos_negocio)

# print("\n-----Resultados de busqueda por categoria-----")
# print(buscar_por_categoria(gastos_negocio, "INSUMOS"))

# print("\n-----Resultados del Total por categoria-----")
# print(total_por_categoria(gastos_negocio, "insumos"))

gestor_gastos = GestorGastos(gastos_negocio)

while True:
    print("\nMenu:")
    print("0. Salir")
    print("1. Ver todos los gastos")
    print("2. Agregar un gasto nuevo")
    print("3. Buscar gastos por categoria")
    print("4. Ver el total gastado en una categoria")
    opcion = input("Ingrese una opción: ")

    if opcion == "0":
        print("Hasta luego!")
        break
    elif opcion == "1":
        gestor_gastos.ver_gastos()
    elif opcion == "2":
        descripcion = input("Ingrese la descripción: ")
        monto_texto = input("Ingrese el monto: ")
        categoria = input("Ingrese la categoría: ")
        gestor_gastos.agregar_gasto(descripcion, monto_texto, categoria)
    elif opcion == "3":
        categoria = input("Ingrese la categoría a buscar: ")
        resultados = gestor_gastos.buscar_por_categoria(categoria)

        if not resultados:
            print(f"No se encontraron gastos en la categoría '{categoria}'.")
        else:
            for gasto in resultados:
                print(f"{gasto['descripcion']} ({gasto['categoria']}) : ${gasto['monto']}")
    elif opcion == "4":
        categoria = input("Ingrese la categoría para ver el total: ")
        total = gestor_gastos.total_por_categoria(categoria)
        print(f"El total gastado en la categoría '{categoria}' es: ${total:,.2f}")
