def main():
    aux = 1
    for x in range(1, 8):
        slice_obj = slice(1, x-1, -1)
        str_aux = str(aux)
        print(aux  if aux ==1 else aux, str_aux[slice_obj])
        aux = ((x+1)*10) +aux

if __name__ == '__main__':
        main()