

class AST:

    def __init__(self):
        self.list = []

    def addObject(self,object):
        self.list.append(object)
        print("\n ====== object",object.name,"of type",object.type,"added to AST")

    def __repr__(self):
        print("==== Représentation de l'arbre de syntaxe Abstraite ====\n")
        for obj in self.list:
                print(object.name)
                print("\n|\n|\n|\n")


class Program(AST):

    def __init__(self,name,declarations,statements):
        self.name = name
        self.declarations = declarations
        self.statements =  statements
        print("\n ====== création d'un objet Programme:",name)


    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")




class Declaration:

    def __init__(self,ast,name,typ,val):
        self.ast = ast
        self.name = name
        self.type = typ
        self.val = val
        print("\n ======= création d'un objet déclaration:",name,typ,val)
        self.addObject()


    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")


class Statement:

    def __init__(self,name):
        self.name = name
        print("\n ====== création d'un objet Statement:",name)

    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")

class If:
    def __init__(self,name):
        print("\n ====== création d'un IF Statement:")

    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")
class Add:

    def __init__(self,name):
        self.name = name

    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")
