def main():
    main_dict = dict()
    total = int(input("Quants vols introduir? "))
    for x in range(total):
        while True:
            num_aula = int(input("Numero de l'aula?"))
            if num_aula >= 1 and num_aula <= 50:
                break
        name_aula = input("Quin es el nom de l'aula? ")
        ip = input("Quina es la IP de l'aula? ")
        while True:
            num_pc = int(input("Quin es el numero de PCs? "))
            if num_pc >= 1 and num_pc <= 20:
                break
        aux_dict = {x : {
        'Aula': num_aula,
        'Nom aula': name_aula,
        'IP': ip,
        'Numero PCs': num_pc
            }
        }
        main_dict.update(aux_dict)
    print(main_dict)
    print("Aula\t", "Nom aula\t", "IP\t", "Numero PCs\t")
    for key, value in main_dict.items():
        print("\n")
        for x, y in value.items():
            print(y, "\t\t", end='')
if __name__ == '__main__':
        main()