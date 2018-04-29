import re
import sys
from token import Token

regexExpressions = [
    (r'TSAS-KA\b','FOR'),
    (r'E-GADE\b','IF'),
    (r'CHAH-HO-OH-LHAN-IH\b','ELSE'),
    (r'DOLA-ALTH-WHOSH\b','BREAK'),
    (r'AH-NAH-SOZI\b','WHILE'),
    (r'NA-DZAH\b','RETURN'),

    (r'GINI\b','BOOL'),
    (r'TAS-CHIZZIE\b','INT'),
    (r'DA-HE-TIH-HI\b','CHAR'),
    (r'JAY-SHO\b','FLOAT'),
    (r'NE-AS-JAH\b','LONG'),
    (r'GA-GIH\b','DOUBLE'),
    (r'ASTAH\b','SIGNED'),
    (r'WOH-TAH-DE-NE-IH\b','UNSIGNED'),
    (r'TSE-E\b','VOID'),

    (r'NAH-E-THLAI\b', 'LT'),
    (r'BE-AL-DOH-CID-DA-HI\b', 'LTE'),
    (r'NI-DI-DA-HI\b', 'GT'),
    (r'BE-EL-DON-TS-QUODI\b', 'GTE'),

    (r'JISH-CHA\b', 'ASSIGN'),
    (r'ALTSEH-E-JAH-HE\b', 'ADDEQ'),
    (r'A-YE-SHI\b', 'ADD'),
    (r'AH-KIN-CIL-TOH\b', 'SUBEQ'),
    (r'COH-TAH-GHIL-TLID\b', 'SUB'),
    (r'AH-ZHOL\b', 'MUL'),
    (r'NI-MA-SI\b', 'DIV'),
    (r'KHAC-DA\b', 'NEQ'),
    (r'OH-BEHI\b', 'DBAR'),
    (r'NEH-HECHO-DA-NE\b','EQ'),
    (r'NAH-GHIZI\b','DAMPERSAND'),

    (r'ESAT-TSANH\b','COMMENT'),
    (r'BAH-DEH-TAHN\b','NEW')
    ]

def lex(self, inputText):

        lineNumber = 0
        for line in inputText:
            lineNumber += 1
            position = 0
            while position < len(line):
                match = None
                for tokenRegex in regexExpressions:
                    pattern, tag = tokenRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        if tag:
                            token = Token(tag, data, [lineNumber, position])
                            self.tokens.append(token)
                        break
                if not match:
                    print(inputText[position])
                    print("no match")
                    sys.exit(1)
                else:
                    position = match.end(0)
        print("lexer: analysis successful!")
        return self.tokens
