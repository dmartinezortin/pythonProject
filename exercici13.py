def main():
    #Introduir valors
    value1, value2 = input("Introdueix el primer numero: "), input("Introdueix el segon numero: ")
    #Conversió de valors
    value1,value2=value2,value1
    print("Valor 1: " + value1 + " Valor2: " + value2)
if __name__ == '__main__':
        main()