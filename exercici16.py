def main():
    while True:
        value = int(input("Introdueix un numero del 1 al 20: "))
        if value < 20 and value > 1:
            break
    print([value*x for x in range(100) if (value * x) < 100])
if __name__ == '__main__':
        main()