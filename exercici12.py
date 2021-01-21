def main():
    main_list = list()


    #Demana els numeros i els introdueix a la llista
    for x in range(10):
        main_list.append(int(input("Introdueix un numero: ")))
        while main_list[x] >10 or main_list[x]<0:
            main_list.insert(x, int(input("Introdueix un numero dins del rang! (0-10): ")))

    #Separa els parells dels imparells
    pair_list = [x for x in main_list if x % 2 == 0]
    odd_list = [x for x in main_list if x % 2 != 0]

    #Printa parells i imparells
    print(pair_list)
    print(odd_list)

if __name__ == '__main__':
        main()