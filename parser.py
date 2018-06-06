import sys
from indent import Indent
from AST import *

class Parser:

    TYPE_PLANE = ['DIVE_BOMBER','TORPEDO_PLANE','FIGHTER_PLANE','BOMBER_PLANE','OBS_PLANE','PATROL_PLANE','TRANSPORT']
    TYPE_TANK = ['TANK']
    TYPE_WEAPON = ['MINE']
    TYPE_ACTION = ['SCOUT','HALT','ATTACK']

    TYPE = TYPE_PLANE + TYPE_TANK + TYPE_WEAPON



    STATEMENT_STARTERS = ['SEMICOLON', 'LBRACE', 'IDENTIFIER', 'IF', 'WHILE']
    REL_OP = ['LT', 'LTE', 'GT', 'GTE']
    MUL_OP = ['MUL', 'DIV']
    LITERAL = ['INTEGER_LIT', 'FLOAT_LIT', 'CHAR_LIT']

    def __init__(self,ast, verbose=False):
        self.indentator = Indent(verbose)
        self.tokens = []
        self.errors = 0
        self.ast = ast

    def show_next(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
            sys.exit(1)
            return 0

    def expect(self, kind):
        actualToken = self.show_next()
        actualKind = actualToken.kind
        actualPosition = actualToken.position
        if actualKind == kind:
            return self.accept_it()
        else:
            print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
            sys.exit(1)


    # same as expect() but no error if not correct kind
    def maybe(self, kind):
        if self.show_next().kind == kind:
            return self.accept_it()

    def accept_it(self):
        token = self.show_next()
        output = str(token.kind) + ' ' + token.value
        self.indentator.say(output)
        return self.tokens.pop(0)

    def remove_comments(self):
        result = []
        in_comment = False
        for token in self.tokens:
            if token.kind == 'COMMENT':
                pass
            elif token.kind == 'LCOMMENT':
                in_comment = True
            elif token.kind == 'RCOMMENT':
                in_comment = False
            else:
                if not in_comment:
                    result.append(token)
        return result

    def parse(self, tokens):
        self.tokens = tokens
        self.tokens = self.remove_comments()
        self.parse_program()

    def parse_program(self):
        self.indentator.indent('Parsing Program')

        #TODO: find a sequence defining a new program


        #self.expect('LCOMMENT')
        #print("before parse declaratio\n\n")
        #name = self.expect('IDENTIFIER').value
        #self.expect('RCOMMENT')
        decls=self.parse_declarations()
        stmts=self.parse_updates()

        self.indentator.dedent()
        if (self.errors == 1):
            print('WARNING: 1 error found!')
        elif (self.errors > 1):
            print('WARNING: ' + str(self.errors) + ' errors found!')
        else:
            print('parser: syntax analysis successful!')
        return Program("nom",decls,stmts)


    def parse_declarations(self):
        tab=[]
        self.indentator.indent('Parsing Declarations')
        while(len(self.tokens) > 0 and self.show_next().kind == 'NEW'):
            print("*********PARSING DECLARATION********\n")
            #TODO: si on fait decl up decl2 la decl2 n'est pas prise en compte
            tab.append(self.parse_declaration())
        self.indentator.dedent()
        return tab

    def parse_declaration(self):

        val = None
        self.indentator.indent('Parsing declaration')
        self.accept_it()
        name = self.expect('IDENTIFIER').value
        typ = self.show_next().kind
        pos = self.show_next().position

        if typ in self.TYPE:

            self.accept_it()
            self.expect('INTEGER_LIT')
            if self.show_next().kind in self.TYPE_ACTION :
                self.accept_it()
                valx = self.expect('INTEGER_LIT').value
                valy = self.expect('INTEGER_LIT').value

            print("Declaration de la variable:",name,"de type",typ,"\n")
        val = (valx,valy)
        #self.indentator.dedent()
        return(Declaration(self.ast, name,typ,val,pos))


    def parse_updates(self):
        tab = []
        #self.indentator.indent('Parsing Updates')

        while(len(self.tokens) > 0 and self.show_next().kind == 'CHANGE'):

            print("*********PARSING UPDATE********\n")

            up = self.parse_update()
            print("UPDATE-OVER")
            tab.append(up)
            self.indentator.dedent()

        print("----------------------------------> QUIT UPDATES")


        return tab

    def parse_update(self):
        self.indentator.indent('Parsing Update')
        self.accept_it()
        name = self.expect('IDENTIFIER').value
        pos = self.show_next().position
        print(name,"============")

        if self.show_next().kind in self.TYPE_ACTION:
            self.accept_it()
            coordx = self.expect("INTEGER_LIT")
            coordy = self.expect("INTEGER_LIT")


        return update(self.ast,name,coordx,coordy,pos)



    def parse_if(self):
        self.accept_it()
        self.parse_expression()
        pos = self.show_next().position
        return If(self.ast,pos)

    def parse_while(self):
        self.accept_it()
        self.parse_expression()
        pos = self.show_next().position
        return While(self.ast,pos)


    def parse_expression(self):
        self.indentator.indent('Parsing Expression')

        print(">>>> PARSING EXPRESSION\n")

        self.expect('IDENTIFIER')
        pos = self.show_next().position
        next = self.show_next().kind
        if next in ['EQ','NEQ','DBAR','LTE','LT','GT','GTE','DAMPERSAND']:
            self.accept_it()
            if self.show_next().kind in ['IDENTIFIER','INTEGER_LIT']:
                self.accept_it()
                print("fin de la condition\n")

        self.indentator.dedent()

    def parse_conjunction(self):
        #TODO: define conjunction
        pass

    def parse_relation(self):
        #TODO: define relation
        pass

    def parse_operation(self):
        self.accept_it()
        self.expect('ASSIGN')
        pos = self.show_next().position

        if self.show_next().kind in ['INTEGER_LIT','IDENTIFIER']:
            self.accept_it()
            next = self.show_next().kind

            if next == "ADD":
                self.accept_it()
            elif next == "MUL":
                self.accept_it()
            elif next == "DIV":
                self.accept_it()

        if self.show_next().kind in ['IDENTIFIER','INTEGER_LIT']:
            self.accept_it()

        print("Opération parsée\n")

        self.indentator.dedent()
