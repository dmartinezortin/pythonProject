def main():
    #Variables
    value1 = int(input("Introdueix un numero del 1 al 10: "))
    value2 = int(input("Introdueix un numero del 1 al 10: "))
    value3 = int(input("Introdueix un numero del 1 al 10: "))
    #Condició tots son iguals
    if ((value1+value2+value3)/value1) == 3:
        final_value = (value1+value2+value3)*3
        print(final_value)
    #Condició no son iguals
    else:
        final_value = (value1+value2+value3)
        print(final_value)

if __name__ == '__main__':
            main()
