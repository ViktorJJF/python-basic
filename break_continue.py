def run():
    word=input("Escribe tu nombre")
    for letter in word:
        if letter=='o':
            break
        print(letter)

if __name__=='__main__':
    run()