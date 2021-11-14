# count=0
# print('2 elevado a '+str(count)+' es igual a ' + str(2**count))

def run():
    LIMITE = 1000
    # counter=0
    # potencia_2=0
    # while potencia_2<LIMITE:
    #     print(f"2 elevado a {counter} es igual a {2**counter}")
    #     counter+=1
    #     potencia_2=2**counter
    for counter in range(100,201):
        print(f"2 elevado a {counter} es igual a {2**counter}")

if __name__=='__main__':
    run()
