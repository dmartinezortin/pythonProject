def main():
    #Es crean les llistes
    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    aux_list = list()
    #Es crea un bucle
    for x in a:
        #Es comprova que no hi es el numero i s'assigna
        if x not in aux_list:
            aux_list.append(x)
    #es printa
    print(aux_list)
if __name__ == '__main__':
        main()