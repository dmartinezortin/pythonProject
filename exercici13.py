def main():
    #Introduir valors
    value1 = int(input("Introdueix el primer numero: "))
    value2 = int(input("Introdueix el segon numero: "))
    aux = value1
    value1 = value2
    value2 = aux
    print("Valor 1: " , value1 , "Valor 2: " , value2)

if __name__ == '__main__':
        main()