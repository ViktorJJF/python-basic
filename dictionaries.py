def run():
    persons=[]
    my_dictionary={
        'nombres':{
            'first':"Victor",
            'second':'Juan'
            },
    }
        'apellidos':"Jimenez"
    persons.append(my_dictionary)
    print(my_dictionary.items())
    print(persons)
    for name, value in my_dictionary.items():
        print(f"En la llave {name} hay {value}")

if __name__=='__main__':
    run()