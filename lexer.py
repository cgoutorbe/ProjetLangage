import re
import sys
from token import Token

regexExpressions = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'TSAS-KA\b\s','FOR'),
    (r'E-GADE\b\s','IF'),
    (r'CHAH-HO-OH-LHAN-IH\b\s','ELSE'),
    (r'DOLA-ALTH-WHOSH\b\s','BREAK'),
    (r'AH-NAH-SOZI\b\s','WHILE'),
    (r'NA-DZAH\b\s','RETURN'),

    #TYPES OF VEHICLE
    (r'GINI\b\s','DIVE_BOMBER'),
    (r'TAS-CHIZZIE\b\s','TORPEDO_PLANE'),
    (r'DA-HE-TIH-HI\b\s','FIGHTER_PLANE'),
    (r'JAY-SHO\b\s','BOMBER_PLANE'),
    (r'NE-AS-JAH\b\s','OBS_PLANE'),
    (r'GA-GIH\b\s','PATROL_PLANE'),
    (r'ASTAH\b\s','TRANSPORT'),
    (r'LO-TSO\b\s','BATTLESHIP'),
    (r'CHAY-DA-GAHI\b\s','TANK'),

    #TYPES OF GROUP
    (r'DIN-NEH-IH\b\s','CORPS'),
    (r'TACHEENE\b\s','BATTALION'),
    (r'DEBEH-LI-ZINI\b\s','SQUAD'),

    #TYPES OF RANK
    (r'BIH-KEH-HE\b\s','COMMANDING_GENERAL'),
    (r'ATSAH-BESH-LE-GAI\b\s','COLONEL'),

    #TYPES OF ACTION
    (r'TA-LA-HI-JIH\b\s','CONCENTRATION'),
    (r'TA-AKWAI-I\b\s','HALT'),
    (r'HA-A-SID-AL-SIZI-GIH\b\s','SCOUT'),
    (r'ESAT-TSANH\b\s','RADAR'),
    (r'A-NAH-NE-DZIN\b\s','ATTACK'),

    (r'HA-GADE\b\s','MINE'),



    (r'BAH-DEH-TAHN\b\s','NEW'),

    (r'THLA-GO-A-NAT-ZAH\b\s','CHANGE'),

    (r'[a-zA-Z]\w*\s', 'IDENTIFIER'),
    (r'\d+', 'INTEGER_LIT')


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
                                print('===========> ',tag,lineNumber)
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
