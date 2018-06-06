import sys
MAG = "\u001b[35;1m"
BLU = "\u001b[34;1m"
YLW = "\u001b[93;1m"
RED = "\u001b[31;1m"
RST = "\u001b[0m"

class AST:

    TYPE_PLANE = ['DIVE_BOMBER','TORPEDO_PLANE','FIGHTER_PLANE','BOMBER_PLANE','OBS_PLANE','PATROL_PLANE','TRANSPORT']
    TYPE_TANK = ['TANK']
    TYPE_WEAPON = ['MINE']
    TYPE_ACTION = ['SCOUT','HALT','ATTACK']

    TYPE = TYPE_PLANE + TYPE_TANK + TYPE_WEAPON

    def __init__(self):
        self.list = []
        self.listDecl = []
        self.listUp= []
        self.listDeclName = []
        self.listUpName = []
        self.name = "AST"


    def addObject(self,object):
        self.list.append(object)
        print("\n ====== object",object.name,"of type",object.type,"added to AST")

    def borderedDecl(self,list):

        width = max(len(s) for s in list)
        res = []
        for s in list:
            res.append('┌' + '─' * width + '┐')
        ''.join(res)
        res.append('\n')
        for s in list:
            res.append('│' + (s + ' ' * width)[:width] + '│')
            ''.join(res)
        res.append('\n')
        for s in list:
            res.append('└' + '─' * width + '┘')
        return ''.join(res)

    def __repr__(self):
        print("==== Représentation de l'arbre de Syntaxe Abstraite ====\n")
        i=0

        res = []
        listText =[]
        listTextUp =[]

        for obj in self.listDecl:
            listText.append(MAG + obj.name+ RST + ">>> "+ RED + obj.type+ RST +' at '+ YLW + str(obj.val) + RST)
        for up in self.listUp:
                listTextUp.append(BLU + "UPDATE" + RST + " >>> " + MAG +up.name + RST)

        print(self.borderedDecl(listText))
        print(self.borderedDecl(listTextUp))


        return("")


class Context():

    #classe réalisant l'analyse contextuelle de L'AST
    #regle de base -> deux variable ne peuvent pas avoir le meme nom (aucune circonstance)
    #une variable ne peut pas être updatée avant

    def __init__(self,ast):
        self.ast = ast
        self.DicoAST = {}
        self.verifDeclaration()
        self.verifNoDecl()
        self.Decl2times()
        self.link()

    def __repr__(self):
        #TODO: printer le nouvel AST de maniere élégante
        #TODO: parcourir le dictionnaire pour printer tous les sous arbres correspondants aux objets
        print("==== Représentation de l'arbre de Syntaxe Abstraite Décoré ====\n")
        for obj in self.ast.listDeclName:
            print(self.DicoAST[obj])
            print("\t\t =======\n")

        return('')

    def verifNoDecl(self):
        #vérifie si une variable n'a pas été déclarée
        intersect = set(self.ast.listDeclName) and set(self.ast.listUpName)
        if intersect != set(self.ast.listUpName):
            print("ERROR: variable referenced without prior assignment")
            sys.exit(1)
    def Decl2times(self):
        if (len(set(self.ast.list)) != len(self.ast.list)):
            print("ERROR: variable declared twice")
            sys.exit(1)

    def verifDeclaration(self):
        #vérifie que les variables sont déclarée avant d'être UPDATE
        print("Test de la bonne déclaration des variables")
        for obj in self.ast.listDecl:
            print(RED,"obj ---->",RST,MAG,obj.name,RST,"<")
            for up in self.ast.listUp:
                print(BLU,"up ----->",RST,MAG,up.name,RST,"<")
                if obj.name == up.name and obj.position > up.position:
                    print("ERROR: object updated before being declared")
                    sys.exit(1)

    def link(self):
        #fait le lien entre les objets déclaré et leurs UPDATES



        for obj in set(self.ast.listDecl):
            #set élimine les doublons de déclaration
            print(">>>>>",obj.name)
            #création d'un élément disctinct pour chaque déclaration au nom différent
            self.DicoAST[obj.name] = SubTree(self.ast,obj.name+'_tree')
            #ajout de la déclaration dans le sous arbre nouvellement créé
            self.DicoAST[obj.name].listDecl.append(obj)

        for obj in self.ast.listUp:
            self.DicoAST[obj.name].listUp.append(obj)



        #print(self.DicoAST['trans '].listUp)
        #for obj in self.ast.list:
        #    obj.name.list.append(obj)

class SubTree():
    #défini un sous arbre associé à un objet il contiendra sa déclaration ainsi que tous ses updates propres
    def __init__(self,ast,name):
        self.name = name
        self.listDecl = []
        self.listUp = []

    def borderedDecl(self,list):

        if len(list)>0:
            width = max(len(s) for s in list)
        else:
            width = 0
        res = []
        for s in list:
            res.append('┌' + '─' * width + '┐')
        ''.join(res)
        res.append('\n')
        for s in list:
            res.append('│' + (s + ' ' * width)[:width] + '│')
            ''.join(res)
        res.append('\n')
        for s in list:
            res.append('└' + '─' * width + '┘')
        return ''.join(res)



    def __repr__(self):

        #représentation du sous arbre


        res = []
        listText =[]
        listTextUp =[]
        liste =[]


        for obj in self.listDecl:
            listText.append(MAG + obj.name+ RST + ">>> "+ RED + obj.type+ RST + ' at '+ YLW + str(obj.val) + RST)
        for up in self.listUp:
            listTextUp.append(BLU + "UPDATE >>> "+ RST + MAG + up.name + RST)
        liste = listText + listTextUp

        print(self.borderedDecl(liste))
        #print(self.borderedDecl(listText))
        #print(self.borderedDecl(listTextUp))


        return("")

    """
    def astDeco(self):
        #créer un AST décoré

    """

class Program(AST):

    def __init__(self,name,declarations,statements):
        self.name = "nom"
        self.declarations = declarations
        self.statements =  statements
        print("\n ====== création d'un objet Programme:",name)

    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")


class Declaration:

    def __init__(self,ast,name,typ,nb,action,val,pos):
        self.ast = ast
        self.name = name
        self.type = typ
        self.val = val
        self.position = pos
        self.nb = nb
        self.action = action
        print("\n ======= création d'un objet déclaration:",name,typ,val)
        self.addObject()


    def addObject(self):
        self.ast.list.append(self)
        self.ast.listDecl.append(self)
        self.ast.listDeclName.append(self.name)
        print("\n ====== object",self.name,"of type",self.type,"updated to AST")

    def acceptVisitor(visitor):
        print("le visiteur est accepté")
        visitor.visitDeclaration(self)


class update:

    def __init__(self,ast,name,action,x,y,pos):
        self.name = name
        self.coordx = x
        self.coordy = y
        self.ast = ast
        self.action = action
        self.type = "UPDATE"
        self.position = pos
        self.addObject()
        print("\n ====== création d'un objet update:",name)

    def addObject(self):
        self.ast.list.append(self)
        self.ast.listUp.append(self)
        self.ast.listUpName.append(self.name)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")

    def acceptVisitor(visitor):
        print("le visiteur est accepté")
        visitor.visitUpdate(self)

class If:
    def __init__(self,ast,pos):
        print("\n ====== création d'un IF Statement:")
        self.name = "IF"
        self.ast = ast
        self.type = "IF"
        self.position = pos
        self.addObject()

    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")

    def acceptVisitor(visitor):
        print("le visiteur est accepté")
        visitor.visitIf(self)

class Add:

    def __init__(self,ast):
        self.name = name
        self.ast = ast
        self.type = "ADD"
        self.addObject()


    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")

    def acceptVisitor(visitor):
        print("le visiteur est accepté")
        visitor.visitAdd(self)

class While:
    def __init__(self,ast):
        self.name = "WHILE"
        self.ast = ast
        self.type = "WHILE"
        self.addObject()

        print("\n ====== création d'un IF Statement:")


    def addObject(self):
        self.ast.list.append(self)
        print("\n ====== object",self.name,"of type",self.type,"added to AST")

    def acceptVisitor(visitor):
        print("le visiteur est accepté")
        visitor.visitWhile(self)

class Visitor:

    def __init__(self,ast):
        print("===== Initialisation du visiteur ===== ")
        self.ast = ast
        self.name ="visitor"


    def visitUpdate(self,update):
        print("==== Visiting Update ====")

    def visitIf(self,ifStatement):
        print("==== Visiting If ====")

    def visitWhile(self,whileStatement):
        print("==== Visiting While ====")

    def visitAdd(self,addStatement):
        print("==== Visiting Add ====")
