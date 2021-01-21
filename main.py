def main():
    reverse_text = input("Quin es el text desitjat? ")
    #Función ya no necesaria print(reverse_text[::-1])
    #Función no util reverse_text = reverse_text[::-1]
    aux = input("Introdueix la primera lletra: ")
    print(aux + reverse_text[1:])
if __name__ == '__main__':
        main()