def main():

#Codi per introduir els valors

    value1 = int(input("Introdueix el primer numero: "))
    value2 = int(input("Introdueix el segon numero: "))
    x = 1
    #Codi per imprimir

    for value1 in range(value2):
        i = 1
        aux = value1 + i
        for x in range(2, aux):
            if aux % x == 0:
                print(aux)

if __name__ == '__main__':
            main()
