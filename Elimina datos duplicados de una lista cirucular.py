
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Creacion de clases de la Lista Circular 
class ListaCircular:

    def __init__(self):
        self.head = None

    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # Condiciono para el primer nodo

        self.head = ptr1
  # Funcion para imprimir nodos en la lista circular
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print("%d" % (temp.data)),
                temp = temp.next
                if (temp == self.head):
                    break
# Funcion para eliminar los elementos duplicados de la lista circular
def remover_duplicados(ListaCircular1):
    no_duplicados=[]

    for c in ListaCircular1:
        if c not in no_duplicados:
            no_duplicados.append(c)
    return no_duplicados

# Inicio las lista
cllist = ListaCircular()
cllist.push(87)
cllist.push(54)
cllist.push(54)
cllist.push(54)
cllist.push(91)
cllist.push(91)
# Resultados esperados de la lista circular
# 91 -> 91 ->  54 -> 54 -> 54 -> 87 ->

print( "        Ilustracion Grafica del Ejercicio        ")
print( "-------------------------------------------------")
print( "|     |  87  |  54  |  54  |  54  |  91  |  91  |")
print( "-------------------------------------------------")
print( "         ↑                                   ↑   ")
print( "       FRENTE                               FINAL")

cllist.printList()
print("Lista circular del ejercicio antes de eliminar duplicados")
ListaCircular1 = [ 87 , 54 ,  54 , 54 ,  91 ,  91 ]

print(ListaCircular1)

resultado = remover_duplicados(ListaCircular1)
print("Lista Circular luego de eliminar duplicados")
print(resultado)




