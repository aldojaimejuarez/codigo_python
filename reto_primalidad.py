def es_primo(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def run():
    num = int(input('Escribe un número: '))
    if num == 1:
        print('No es primo')
        return
    else:
        duda = es_primo(num)
        if duda:
            print("Es primo")
        else:
            print("No es primo")

if __name__ == '__main__':
    run()


