import array as arr

def main():

#Codi per introduir els valors
    i = 1
    total = 0
    #Iteració
    for i in range(10):
            value=int(input("Introdueix un numero decimal: "))
            total = value + total
            
    print(total/10)

if __name__ == '__main__':
            main()
