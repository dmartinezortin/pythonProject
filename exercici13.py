def main():
    #Introduir valors
    value1 = input("Introdueix el primer numero: ")
    value2 = input("Introdueix el segon numero: ")
    #Conversió de valors
    size = len(value1)
    value1 += value2
    value2 = value1[0:size]
    value1 = value1[size:]
    int(value1)
    int(value2)
    #Printar valors
    print("Valor 1: " + value1 + " Valor2: " + value2)

if __name__ == '__main__':
        main()