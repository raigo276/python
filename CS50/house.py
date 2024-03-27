def main():
    name = input("What is your name? ")
    print(houseCheck(name))

def houseCheck(iname):
    match iname:
        case "Harry" | "Hermione" | "Ron":
            return "Gryffindor"
        
