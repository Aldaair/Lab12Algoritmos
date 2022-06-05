import time
import random

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insertNode(root, node):
    '''
    Insert a node in BST
    '''
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def findMin(root):
    '''
    Find the minimum value. Recursive mode
    :param root:
    :return:
    '''
    currentNode = root
    if currentNode.left == None:
        return currentNode
    else:
        return findMin(currentNode.left)

def findMax(root):
    '''
    Find the maximum value. Recursive mode
    :param root:
    :return:
    '''
    currentNode = root
    if currentNode.right == None:
        return currentNode
    else:
        return findMax(currentNode.right)
def buildManualBST():
    '''
    Build Binary Search Tree
    :return:
    '''
    root = BSTNode(5)
    insertNode(root, BSTNode(7))
    insertNode(root, BSTNode(3))
    insertNode(root, BSTNode(9))
    insertNode(root, BSTNode(1))
    insertNode(root, BSTNode(12))
    insertNode(root, BSTNode(0))
    return root
def find(root, data):
    currentNode = root
    if currentNode == None:
        return None     
    else:
        if data == currentNode.data:
            return currentNode.data
        if data < currentNode.data:
            return find(currentNode.left,data)
        else:
            return find(currentNode.right,data)
def buildBSTFromArray(list):
    root = None

    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root

if __name__ == "__main__":
    numberss=[]
    numeros_a_buscar=[]
    for i in range (0,10000):
        ran=random.randint(1,500000)
        numberss.append(ran)

    #Escogiendo 50 números aleatorios
    for i in range(0,50):
        ran=random.randint(0,10000)
        index=numberss[ran]
        numeros_a_buscar.append(index)

    #Escribiendo los 10000 números en un archivo txt
    f=open("numeros.txt","w")
    for i in range(0,10000):
        f.write(str(numberss[i])+"\n")
    f.close()

    #Leyendo los números grabados
    f=open("numeros.txt","r")
    newlist=[]
    for linea in f:
        newlist.append(str(linea))
    f.close()
    print(newlist)
    
    #Conviendo la lista a un BST
    tree=buildBSTFromArray(newlist)

    #Midiendo tiempo de busqueda en los datos de la lista numeros_a_buscar 
    inicio = time.time()
    # Código a medir
    for i in range(0,49):
        buscar=numeros_a_buscar[i]
        if buscar in numeros_a_buscar:
            print("El número "+str(buscar)+" se encontró en la lista")

    fin = time.time()
    print("Tiempo de ejecución: ")
    print(fin-inicio)
    
    exit(-1)
    #Midiendo tiempo de buscar un dato en la lista numeros_a_buscar 
    inicio = time.time()
    # Código a medir
    for i in range(0,100):
        buscar=str(random.randint(1,500000))
        if buscar in numeros_a_buscar:
            print("El número "+str(buscar)+" se encontró en la lista")
        else:
            print("No se encontró el número ",str(buscar)," en la lista")
    fin = time.time()
    print("Tiempo de ejecución: ")
    print(fin-inicio) 

        
    

