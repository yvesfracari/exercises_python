'''Print the squares until a input number.'''

def get_natural():
    '''Return a natural input number.'''

    number = int(input())
    if (number < 1 or number > 20):
        print("Escreva um numero natural entre 1 e 20\n")
        return get_natural()

    return number

def main():
    '''Print the squares until a input number.'''
    number = get_natural()

    for i in range(number):
        square = i**2
        print(square)

if __name__ == '__main__':
    main()
