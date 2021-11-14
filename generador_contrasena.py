import random

def generar_contrasena():
    mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    minusculas=["a","b","c","d","e","f","g","h","i","j","k"]
    simbolos=["!","#","$",""]
    numeros=["1","2","3","4","5","6","7","8","9","10","11","12","13","0"]
    caracteres=mayusculas+minusculas+simbolos+numeros
    contrasena=[]

    for i in range(15):
        caracter_random=random.choice(caracteres)
        contrasena.append(caracter_random)
    return ''.join(contrasena)

def run():
    contrasena=generar_contrasena()
    print(f"Tu nueva contraseña es -> {contrasena}")

if __name__=="__main__":
    run()