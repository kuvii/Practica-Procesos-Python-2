import os

def ping(args):
    if (args == "?"):
        args = " "
    print(os.system("ping " + args))

if __name__ == '__main__':
    print(" ? / Enter -> Ayuda")
    arg = input("Introduce  una url o una ip: ")
    ping(arg)
