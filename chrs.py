import importlib, os, re

def getCharacters():
    characters = []
    for chrFile in [file for file in os.listdir('./characters') if file.endswith('.py')]:
        chr = loadChr(chrFile[:-3])
        characters.append(chr)
    return characters

def loadChr(name):
    chr = {}
    chr["name"] = name
    chr["character"] = eval(f"importlib.import_module(\"characters.{name}\").{name}()")
    return chr