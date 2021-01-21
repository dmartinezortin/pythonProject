def main():
    main_list = list()


    #Demana els numeros i els introdueix a la llista
    for x in range(10):
        main_list.insert(x, int(input("Introdueix un numero: ")))
        while main_list[x] >10 or main_list[x]<0:
            main_list.insert(x, int(input("Introdueix un numero dins del rang! (0-10): ")))



    slice_obj = slice(0, 9, 1)
    pair_list = list(main_list[slice_obj])
    odd_list = list(main_list[slice_obj])

    for x in range(10):
        if main_list[slice_obj] % 2 == 0:
            pair_list = main_list[slice_obj]




    print(pair_list[:])
    print(odd_list[:])
if __name__ == '__main__':
        main()