class PrettyPrinter:

    #on défini un dictionnaire faisant le lien kind -> value
    #afin de retrouver le code en focntion des values de l'AST













    def __init__(self,ast):

        self.ast = ast

        self.dicoReg = { 'DIVE_BOMBER':'GINI ',
        'TORPEDO_PLANE':'TAS-CHIZZIE ',
        'FIGHTER_PLANE':'DA-HE-TIH-HI ',
        'BOMBER_PLANE':'JAY-SHO',
        'OBS_PLANE':'NE-AS-JAH',
        'PATROL_PLANE':'GA-GIH',
        'TRANSPORT':'ASTAH ',
        'BATTLESHIP':'LO-TSO ',
        'TANK':'CHAY-DA-GAHI ',
        'CORPS':'DIN-NEH-IH ',
        'BATTALION':'TACHEENE ',
        'SQUAD':'DEBEH-LI-ZINI ',
        'CONCENTRATION':'TA-LA-HI-JIH ',
        'HALT':'TA-AKWAI-I ',
        'SCOUT':'HA-A-SID-AL-SIZI-GIH ',
        'RADAR':'ESAT-TSANH ',
        'ATTACK':'A-NAH-NE-DZIN ',
        'MINE':'HA-GADE ',

        }
        self.codeGeneration()




    def codeGeneration(self):
        #Ouverture du fichier a creer
        codeGen = open("prettyCode.ASTAH",'w')


        for obj in self.ast.listDecl:

            codeGen.write("BAH-DEH-TAHN "+ obj.name + self.dicoReg[obj.type] + obj.nb+' '+ self.dicoReg[obj.action] + str(obj.val[0])+' '+str(obj.val[1])+'\n')
        for obj in self.ast.listUp:
            codeGen.write("THLA-GO-A-NAT-ZAH " + obj.name + self.dicoReg[obj.action]+ ' ' +obj.coordx+' '+obj.coordy+'\n')

        codeGen.close()
