def get_natural():
    n = int(input())
    if (n < 1 or n > 20):
        print("Escreva um numero natural entre 1 e 20\n")
        return get_natural()
    else:
        return n

def main():
    n = get_natural()
    for i in range (n):
        square = i**2
        print(square)
    
if __name__ == '__main__':
    main()