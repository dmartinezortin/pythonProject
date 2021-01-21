def main():
    #Demana el valor
    value = float(input("Introdueix un numero del 1 al 10: "))
    #Condició
    while value > 10 or value < 0:
            value = int(input("Introdueix un numero dins del rang:  1 - 10: "))
    

if __name__ == '__main__':
            main()
