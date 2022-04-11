
class Node(object):  #třída Node, dědí od objektu
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        #fce id vrátí unikátní id vrcholu
        return f"Node {id(self)}: {self.data}, left: {id(self.left)}, right: {id(self.right)}, parent: {id(self.parent)}"
    
class BinaryTree(object):
    def __init__(self) -> None:
        self.root : Node = None

    def __str__(self) -> str:
        return f"BinaryTree {id(self)}: root: {id(self.root)}"

class BinarySearchTree(BinaryTree):
    def insert(self, data) -> None:
        # pokud kořen neexistuje, vytvořím ho a jsem hotov
        if self.root == None:
            self.root = Node(data)
            return

        # pokud kořen existuje, držím si aktuální vrchol a podle jeho hodnoty se pochybuji stromem
        # když se mám pohnout do neexistujícího syna, vyrobím nový vrchol a připojím ho do stromu
        vrchol = self.root
        while True:
            if data == vrchol.data:
                return
            elif data < vrchol.data:
                if vrchol.left:
                    vrchol = vrchol.left
                else:
                    vrchol.left = Node(data)
                    vrchol.left.parent = vrchol
                    return
            elif data > vrchol.data:
                if vrchol.right:
                    vrchol = vrchol.right
                else:
                    vrchol.right = Node(data)
                    vrchol.right.parent = vrchol
                    return
            else: return
        

    def query(self, data) -> bool:
        # pokud kořen neexistuje, vracím false
        if self.root == None:
            return False
        
        # pokud kořen existuje, držím si aktuální vrchol a podle jeho hodnoty se pochybuji stromem
        # když najdu hledanou hodnotu, vrátím True
        # když najdu prázdného syna, vrátím False
        vrchol = self.root
        while True:
            if data == vrchol.data:
                return True
            elif data < vrchol.data:
                if vrchol.left:
                    vrchol = vrchol.left
                else: return False
            elif data > vrchol.data:
                if vrchol.right:
                    vrchol = vrchol.right
                else: return False
            else: return

n1 = Node(1)
n2 = Node(2)

print(f"id None: {id(None)}")
print(n1)
print(n2)

n1.right = n2
n2.parent = n1
print(n1)
print(n2)

# tree = BinaryTree()
# tree.root = n1
# print(tree)

tree = BinarySearchTree()
print(tree)

tree.insert(3)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(2)
tree.insert(11)

print(tree.query(4))