def main():
    value = 7
    for i in range(value1 + 1):
        space = 1
        for space in range(value1 - i):
            print(" ", end="")
        j = i
        for j in range(j, 0, -1):
            print(j, end="")
        j = 2
        for j in range(j, i + 1):
            print(j, end="")
        print("")
    for i in range(value1 - 1, 0, -1):
        space = 1
        for space in range(value1 - i):
            print(" ", end="")
        j = i
        for j in range(j, 0, -1):
            print(j, end="")
        j = 2
        for j in range(j, i + 1):
            # if j != 0:
            print(j, end="")
        print("")

if __name__ == '__main__':
        main()