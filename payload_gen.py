def generateVEXPayload(input):
    """Generates a payload from the passed line of python, where
       the payload contains only characters within group (Rachael Vex)."""
    ascii = [] # store ascii code representation of chars
    for char in input:
        ascii.append(ord(char))
    
    print("eval(", end="")                   # eval() contains chars only within (Rachael Vex)
    for char_code in ascii[:-1]:             # for all char codes but the last
        print(f"chr({char_code})+", end="")

    print(f"chr({ascii[-1]})", end="")       # no concat for last char
    print(")", end="")

if __name__ == "__main__":
    line = input("Enter a line of python: ") 
    generateVEXPayload(line)
