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

print("Gastos del negocio:")
ver_gastos(gastos_negocio)
agregar_gasto(gastos_negocio, "Compra de tijeras", 800.00, "Insumos")
print("\nGastos del negocio despues de agregar un nuevo gasto:")
ver_gastos(gastos_negocio)