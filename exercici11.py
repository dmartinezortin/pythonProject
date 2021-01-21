def main():
    #Variables
    total_approved = 0
    total_suspended = 0
    approved = 0
    suspended = 0
    #Bucle per demanar les notes, condicionals i operacions necesaries
    for i in range(15):
        note = int(input("Introdueix una nota: "))
        while note >10 or note<0:
            note = int(input("Introdueix una nota dins del rang! (0-10): "))
        if note >= 5:
            approved += 1
            total_approved = note + total_approved
        else:
            suspended +=1
            total_suspended = note + total_suspended
    #Printa l'informació a l'usuari
    print("Mitjana aprovats: ", total_approved/approved)
    print("Total aprovats: ", approved)
    print("Mitjana suspesos: ", total_suspended/suspended)
    print("Total suspesos: ", suspended)

if __name__ == '__main__':
        main()