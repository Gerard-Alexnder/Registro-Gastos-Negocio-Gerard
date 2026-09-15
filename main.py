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

    def categoria_mas_costosa(self):
        totales_por_categoria = {}

        for gasto in self.gastos:
            categoria = gasto["categoria"]
            totales_por_categoria[categoria] = (
                totales_por_categoria.get(categoria, 0) + gasto["monto"] #get(categoria, 0) se utiliza para inicializar la categoria en 0 si aun no existe dicha categoria en el diccionario
            )

        if not totales_por_categoria:
            return None

        return max(totales_por_categoria, key=totales_por_categoria.get)
    

    def agregar_gasto(self, descripcion, monto, categoria):
        try:
            monto = float(monto)
        except ValueError:
            print("El monto debe ser un numero. Gasto no agregado.")
            return None

        nuevo_gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
        self.gastos.append(nuevo_gasto)
        return nuevo_gasto

def menu(gestor):
    while True:
        print("\nMenu:")
        print("0. Salir")
        print("1. Ver todos los gastos")
        print("2. Agregar un gasto nuevo")
        print("3. Buscar gastos por categoria")
        print("4. Ver el total gastado en una categoria")
        print("5. Ver la categoria mas costosa")
        opcion = input("Ingrese una opción: ")

        if opcion == "0":
            print("Hasta luego!")
            break
        elif opcion == "1":
            gestor.ver_gastos()
        elif opcion == "2":
            descripcion = input("Ingrese la descripción: ")
            monto_texto = input("Ingrese el monto: ")
            categoria = input("Ingrese la categoría: ")
            gestor.agregar_gasto(descripcion, monto_texto, categoria)
        elif opcion == "3":
            categoria = input("Ingrese la categoría a buscar: ")
            resultados = gestor.buscar_por_categoria(categoria)

            if not resultados:
                print(f"No se encontraron gastos en la categoría '{categoria}'.")
            else:
                for gasto in resultados:
                    print(f"{gasto['descripcion']} ({gasto['categoria']}) : ${gasto['monto']}")
        elif opcion == "4":
            categoria = input("Ingrese la categoría para ver el total: ")
            total = gestor.total_por_categoria(categoria)
            print(f"El total gastado en la categoría '{categoria}' es: ${total:,.2f}")
        elif opcion == "5":
            categoria = gestor.categoria_mas_costosa()
            if categoria is None:
                print("No hay gastos registrados.")
            else:
                print(f"La categoria mas costosa es: {categoria}")


def main():
    gastos_negocio = [
        {"descripcion": "Renta del local", "monto": 15000.00, "categoria": "Renta"},
        {"descripcion": "Compra de insumos", "monto": 3500.00, "categoria": "Insumos"},
        {"descripcion": "Publicidad en redes", "monto": 1200.00, "categoria": "Marketing"},
    ]
    gestor = GestorGastos(gastos_negocio)
    menu(gestor)


if __name__ == "__main__":
    main()
