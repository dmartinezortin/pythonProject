def main():

#Codi per introduir els valors

    value1 = int(input("Introdueix el primer numero: "))
    value2 = int(input("Introdueix el segon numero: "))
    
    while value2 > 0:
        aux = value2
        value2 = value1 % value2
        a = value2
    
    print(value1, value2)
   

if __name__ == '__main__':
            main()
