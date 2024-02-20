import sys
import os
from lunarahelplib import LunaraHelpLib

lhl = LunaraHelpLib()
VERSION = "v0.0.02A"
CREDITS = [
    ["GachaYTB3", "Developer & Creator"]
]

def arun(filepath):
    with open(filepath, "r") as f:
        varnames, vartypes, varcontents = [], [], []
        allowedsymbols = set("abcdefghijklmnopqrstuvwxyz0123456789")
        condition = False
        inanif = False
        error = False
        comment = False
        linenum = 0

        def run(line, inanif):
            nonlocal condition, comment, error, linenum

            line = line.lstrip()
            if inanif and not condition:
                pass
            elif line == "":
                pass
            elif comment:
                pass
            elif line.startswith("//"):
                pass
            elif line.startswith("//["):
                comment = True
            elif line.endswith("]//"):
                comment = False
            elif line.startswith("println(") and line.endswith(")"):
                toprint = line.removeprefix("println(").removesuffix(")")
                if toprint.startswith("'") and toprint.endswith("'"):
                    print(toprint[1:-1])
                elif toprint.startswith('"') and toprint.endswith('"'):
                    print(toprint[1:-1])
                elif toprint.startswith('"') and toprint.endswith("'"):
                    print("Error Code 000-0004\nWhat the hell, do you really create strings like that: \"'? You disgust me.")
                elif toprint.startswith("'") and toprint.endswith('"'):
                    print("Error Code 000-0004\nWhat the hell, do you really create strings like that: '\"? You disgust me.")
                elif toprint in varnames:
                    print(varcontents[varnames.index(toprint)])
            elif "->" in line:
                try:
                    int(line.split("->")[0].removesuffix(" "))
                    print("Error Code 000-0005\nVariable name cannot be an int.")
                except:
                    for char in line.split("->")[0].removesuffix(" "):
                        if char not in allowedsymbols:
                            print(f"Error Code 000-0005\nVariable name cannot contain the character {char}")
                            error = True
                    varnames.append(line.split("->")[0].removesuffix(" "))
                    varcontent = line.split("->")[1].removeprefix(" ")
                    vartype = ""
                    if varcontent.startswith("'") and varcontent.endswith("'"):
                        varcontent = varcontent[1:-1]
                        vartype = "str"
                    elif varcontent.startswith('"') and varcontent.endswith('"'):
                        varcontent = varcontent[1:-1]
                        vartype = "str"
                    elif varcontent.startswith('"') and varcontent.endswith("'"):
                        error = True
                        print("Error Code 000-0004\nWhat the hell, do you really create strings like that: \"'? You disgust me.")
                    elif varcontent.startswith("'") and varcontent.endswith('"'):
                        error = True
                        print("Error Code 000-0004\nWhat the hell, do you really create strings like that: '\"? You disgust me.")
                    elif lhl.isanint(varcontent):
                        vartype = "int"
                        varcontent = int(varcontent)
                    else:
                        print("Error Code 000-0006")
                        print("Variable cannot contain anything other than a string, or an int.")
                        print("Possible Cause: You probably made a typo.")
                    varcontents.append(varcontent)
                    vartypes.append(vartype)
            elif line.startswith("if "):
                condition = line.split("{")[0].removeprefix("if ")
                if condition.endswith(" "): condition = condition.removesuffix(" ")
                if condition == "true":
                    condition = True
                elif condition == "false":
                    condition = False
                    print(f"Warning Code W-000-0001\nif at line {linenum} is never gonna be runned.\nWe prefer you to remove this if at it is never gonna be runned.")
                if line.endswith("}"):
                    if ";" in line.removeprefix(line.split("{")[0] + "{").removesuffix('}'):
                        for miniline in line.removeprefix(line.split("{")[0] + "{").removesuffix('}').split(";"):
                            run(miniline, inanif=True)
                    else:
                        run(line.removeprefix(line.split("{")[0] + "{").removesuffix('}'), inanif=True)
                else:
                    inanif = True
                    run(line.removeprefix(line.split("{")[0] + "{"), inanif=True)
            elif inanif and line.endswith("}"):
                inanif = False
                run(line.removesuffix("}"), inanif=False)

        for line in f:
            linenum += 1
            run(line.strip(), inanif=inanif)
            if error:
                break

def run(filepath):
    if os.path.exists("settings.lnst"):
        RunOnlyLNFiles = None
        for line in open("settings.lnst", "r"):
            if line.startswith("RunOnlyLNFiles"):
                RunOnlyLNFiles = line.strip().endswith("Y")
                break
        if os.path.exists(filepath):
            if filepath.endswith((".ln", ".ln'", '.ln"')) and (not RunOnlyLNFiles or filepath.endswith(".ln")):
                arun(filepath)
            else:
                print("Error Code 000-0003\nFile isn't a .ln file.")
        else:
            print("Error Code 000-0002\nFile doesn't exist.")
    else:
        print("Error Code 000-0001\nsettings.lnst file doesn't exist, did you run the setup.py script before using Lunara ?")

def main():
    if len(sys.argv) < 3:
        print("Usage: lunara <command> <filepath>")
        return
    
    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "run":
        run(filename)
    elif command == "help":
        print("Usage: lunara <command> [filename]")
        print("help: Shows this message")
        print("run: Runs a Lunara file")
        print("credits: Shows credits")
        print("version: Shows the version")
    elif command == "credits":
        print("Credits:")
        for item in CREDITS:
            print(f"{item[0]}: {item[1]}")
    elif command == "version":
        print(f"Lunara {VERSION} by GachaYTB3")
    else:
        print(f"Error Code MM-000-0002\nInvalid command. To get help with commands, run lunara help.")

if __name__ == "__main__":
    main()
