import re
import sys

# TODO: use this in parseSysArgs
USAGE_TEXT = "train.py INPUT OUTPUT"

def parseSysArgs() -> tuple[str,str]:
    n = len(sys.argv)
    if n >= 2: input_file = open(sys.argv[1])
    else: 
        print("You did not specify an input file")
        print("exiting . . .")
        exit()
    if n >= 3: output_file = open(sys.argv[2], "w")
    else: 
        print("No output file specified - write to output.py? [y/n]")
        if input() == "y":
            output_file = open("output.py", "w")
        else: exit()
    return input_file, output_file

# Track: =|=[. . .]-[. . .]-[. . .]=|=
TRACK = re.compile('^(?P<start>(?:=\|=(?P<main><)?\[)|-\[)(?P<content>.*)\](?P<end>=\|=)?')

# Main track has a < before the first car
# indicating it is the main entry point of the app
MAIN_TRACK = re.compile('^(?P<start>(=\|=<)|-)(?P<content>.*)(?P<end>=\|=)?')

# statement regular expressions 
PRINT    = re.compile('(?P<indentation_flag>#)*?choo(?P<body>\(.*\))')
INPUT    = re.compile('(?P<indentation_flag>#)*?aboard(?P<statement>\(.*\))')
IF       = re.compile('(?P<indentation_flag>#)*?switch (?P<condition>.*)')
FUNC     = re.compile('(?P<indentation_flag>#)*?chug (?P<name>\w*)(?P<params>\(.*\))')
RETURN   = re.compile('(?P<indentation_flag>#)*?caboose (?P<value>.*)')
CLASS    = re.compile('(?P<indentation_flag>#)*?car (?P<name>\w*)')
EXCEPT   = re.compile('(?P<indentation_flag>#)*?derail(?P<error> \w*)?')
_INIT    = re.compile('(?P<indentation_flag>#)*?__conduct__(?P<params>\(.*\))')
_STR     = re.compile('(?P<indentation_flag>#)*?__steam__(?P<params>\(.*\))')

class Code_Parse_Context:
    """
    Tracks states throughout parsing of code
    """
    def __init__(self):
        # tracks if the user is currently in a function
        # True is current line starts with track =|= . . .
        self.in_function = False

        # tracks if the user is exiting a function
        # True if current line ends with track =|= . . .
        self.exiting_function = False
        self.nest_level  = 0
        self.indentation = 0


    def tokenizeLine(self, line: str) -> list:
        while m := (TRACK.search(line)):
            tokenized = m.group("content").split("]-[")
            self.exiting_function = True if m.group("end") else False
            if m.group("start") and not m.group("main"):
                token = tokenized[0]
                if m := (FUNC.search(token)):
                    self.indentation -= 1 if m.group("indentation_flag")==None else 0
                    token = token[0:m.start()] + "def " + m.group('name') + m.group('params') + ":" + token[m.end():]
                    output_file.write(token + '\n')
                    self.in_function = True
                    return tokenized[1:]
            return tokenized


    def parseTokenized(self, tokens: list) -> str:
        if tokens == None: return
        out = ""
        for token in tokens:
            while m := (PRINT.search(token)):
                indentation = m.group("indentation_flag").replace('#',' ')*4 if m.group("indentation_flag")!=None else ''
                token = token[0:m.start()] + indentation + "print" + m.group('body') + token[m.end():]
            while m := (INPUT.search(token)):
                token = token[0:m.start()] + "input" + m.group('statement') + token[m.end():]
            while m := (IF.search(token)):
                token = token[0:m.start()] + "if " + m.group('condition') + ":" + token[m.end():]
                if "else" in token: token = token.replace("else if", "elif")
            while m := (FUNC.search(token)):
                token = token[0:m.start()] + "def " + m.group('name') + m.group('params') + ":" + token[m.end():]
            while m := (RETURN.search(token)):
                token = token[0:m.start()] + "return " + m.group('value') + token[m.end():]
            while m := (CLASS.search(token)):
                token = token[0:m.start()] + "class " + m.group('name') + token[m.end():]
            while m := (EXCEPT.search(token)):
                if (m.group("error")):
                    token = token[0:m.start()] + "except " + m.group('error') + token[m.end():]
                else:
                    token = token[0:m.start()] + "except" + token[m.end():]
            
            out += ("    " if self.in_function else "") + token + '\n'
        return out

if __name__ == "__main__":
    input_file, output_file = parseSysArgs()
    parseSysArgs()
    tokenized = ""
    context = Code_Parse_Context()
    while line := input_file.readline():
        if context.exiting_function: context.in_function = False
        tokenized = context.tokenizeLine(line)
        parsedLine = context.parseTokenized(tokenized)
        if parsedLine != None: output_file.write(parsedLine)