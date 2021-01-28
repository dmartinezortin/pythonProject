def main():
    #Es crea la llista
    main_list = list()
    #Es demana a l'usuari quants numeros vol
    for x in range(int(input("Quants valors vols? "))):
        #introdueix els valors a la llista
        main_list.append(int(input("Introdueix un numero: ")))
    #Suma i printa
    total = sum(main_list)
    print(total)
if __name__ == '__main__':
        main()