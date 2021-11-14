import random 

def run():
    number_random = random.randint(1,100)
    number_selected=int(input("Elige un numero del 1 al 100: "))
    while number_random!=number_selected:
        if number_selected>number_random:
            print("Busca un numero mas pequeño")
        else:
            print("Elige un numero mas grande...")
        number_selected=int(input("Elige otro numero..."))
    print("GANASTE!")

if __name__=='__main__':
    run()
    