import re

PRINT = re.compile('choo(?P<body>\(.*\))')
INPUT = re.compile('aboard(?P<statement>\(.*\))')
IF = re.compile('switch (?P<condition>.*)')
FUNC = re.compile('chug (?P<name>\w*)(?P<params>\(.*\))')
RETURN = re.compile('caboose (?P<value>.*)')
CLASS = re.compile('car (?P<name>\w*)')
EXCEPT = re.compile('derail(?P<error> \w*)?')
_INIT = re.compile('__conduct__(?P<params>\(.*\))')
_STR = re.compile('__steam__(?P<params>\(.*\))')

f = open("code.train")
output = open("output.py", "w")
while line := f.readline():
    while m := (PRINT.search(line)):
        line = line[0:m.start()] + "print" + m.group('body') + line[m.end():]
    while m := (INPUT.search(line)):
        line = line[0:m.start()] + "input" + m.group('statement') + line[m.end():]
    while m := (IF.search(line)):
        line = line[0:m.start()] + "if " + m.group('condition') + line[m.end():]
        if "else" in line: line = line.replace("else if", "elif")
    while m := (FUNC.search(line)):
        line = line[0:m.start()] + "def " + m.group('name') + m.group('params') + line[m.end():]
    while m := (RETURN.search(line)):
        line = line[0:m.start()] + "return " + m.group('value') + line[m.end():]
    while m := (CLASS.search(line)):
        line = line[0:m.start()] + "class " + m.group('name') + line[m.end():]
    while m := (EXCEPT.search(line)):
        if (m.group("error")):
            line = line[0:m.start()] + "except " + m.group('error') + line[m.end():]
        else:
            line = line[0:m.start()] + "except" + line[m.end():]
    while m := (_INIT.search(line)):
        line = line[0:m.start()] + "__init__" + m.group('params') + line[m.end():]
    while m := (_STR.search(line)):
        line = line[0:m.start()] + "__str__" + m.group('params') + line[m.end():]
    output.write(line)