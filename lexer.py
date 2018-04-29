import re
import sys
from token import Token

regexExpressions = [
    (r'TSAS-KA\b\s','FOR'),
    (r'E-GADE\b\s','IF'),
    (r'CHAH-HO-OH-LHAN-IH\b\s','ELSE'),
    (r'DOLA-ALTH-WHOSH\b\s','BREAK'),
    (r'AH-NAH-SOZI\b\s','WHILE'),
    (r'NA-DZAH\b\s','RETURN'),
    (r'GINI\b\s','BOOL'),
    (r'TAS-CHIZZIE\b\s','INT'),
    (r'DA-HE-TIH-HI\b\s','CHAR'),
    (r'JAY-SHO\b\s','FLOAT'),
    (r'NE-AS-JAH\b\s','LONG'),
    (r'GA-GIH\b\s','DOUBLE'),
    (r'ASTAH\b\s','SIGNED'),
    (r'WOH-TAH-DE-NE-IH\b\s','UNSIGNED'),
    (r'TSE-E\b\s','VOID'),
    (r'NAH-E-THLAI\b\s', 'LT'),
    (r'BE-AL-DOH-CID-DA-HI\b\s', 'LTE'),
    (r'NI-DI-DA-HI\b\s', 'GT'),
    (r'BE-EL-DON-TS-QUODI\b\s', 'GTE'),
    (r'JISH-CHA\b\s', 'ASSIGN'),
    (r'ALTSEH-E-JAH-HE\b\s', 'ADDEQ'),
    (r'A-YE-SHI\b\s', 'ADD'),
    (r'AH-KIN-CIL-TOH\b\s', 'SUBEQ'),
    (r'COH-TAH-GHIL-TLID\b\s', 'SUB'),
    (r'AH-ZHOL\b\s', 'MUL'),
    (r'NI-MA-SI\b\s', 'DIV'),
    (r'KHAC-DA\b\s', 'NEQ'),
    (r'OH-BEHI\b\s', 'DBAR'),
    (r'NEH-HECHO-DA-NE\b\s','EQ'),
    (r'NAH-GHIZI\b\s','DAMPERSAND'),
    (r'ESAT-TSANH\b\s','COMMENT'),
    (r'BAH-DEH-TAHN\b\s','NEW'),
    (r'[a-zA-Z]\w*\s', 'IDENTIFIER'),

    ]

class Lexer:

    def __init__(self):
        self.tokens = []

    def lex(self, inputText):
            #print(inputText)

            lineNumber = 0
            for line in inputText:
                lineNumber += 1
                position = 0

                while position < len(line):
                    match = None
                    for tokenRegex in regexExpressions:

                        pattern, tag = tokenRegex
                        #print(pattern)
                        regex = re.compile(pattern)
                        match = regex.match(line, position)
                        if match:
                            data = match.group(0)
                            if tag:
                                print('===========> ',tag)
                                token = Token(tag, data, [lineNumber, position])
                                self.tokens.append(token)
                            break
                    if not match:
                        #print(inputText[2])
                        #print(inputText[position])
                        print("no match")
                        sys.exit(1)
                    else:
                        position = match.end(0)
            print("lexer: analysis successful!")
            return self.tokens
