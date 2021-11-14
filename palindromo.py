def palindromo(word):
    formatted_word=word.replace(' ','').lower()
    inverted_word=formatted_word[::-1]
    return formatted_word==inverted_word

def run():
    word=input("Escribe una palabra...")
    return palindromo(word) if True else False


if __name__=='__main__':
    print(run())