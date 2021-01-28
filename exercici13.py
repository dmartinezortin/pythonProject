def main():
    value1 = input("Introdueix el primer numero: ")
    value2 = input("Introdueix el segon numero: ")
    size = len(value1)
    value1 += value2
    value2 = value1[0:size]
    value1 = value1[size:]
    int(value1)
    int(value2)
    print("Valor 1: " + value1 + " Valor2: " + value2)
if __name__ == '__main__':
        main()