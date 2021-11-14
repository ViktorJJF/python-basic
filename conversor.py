def conversor(tipo_pesos,dollar_value):
    lujanes=input("¿Cuántos "+tipo_pesos+" tienes?:")
    lujanes=float(lujanes)
    print("Tienes $"+str(round(lujanes/dollar_value,2))+" dólares...")

menu="""
Bienvenido a este conversor de monedas!! 🤣

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

option=int(input(menu))

if option==1:
    conversor('pesos colombianos',5)
elif option==2:
    conversor('pesos argentinos',6)
    
else:
    conversor('pesos colombianos',7)


    
    



