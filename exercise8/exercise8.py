'''Description in the README file'''

def get_nm():
    '''Return the n, m input parrameters.'''

    n, m = map(int, input().split())

    if(n < 1 or n > 10**5):
        print("Erro: parametro n invalido, digite novamente:\n")
        return get_nm()

    if(m < 1 or m > 10**5):
        print("Erro: parametro m invalido, digite novamente:\n")
        return get_nm()

    return n, m

def get_array(n):
    '''Return a valid input array.'''

    array = list(map(int, input().split()))

    if len(array) != n:
        print("Erro: numero de elementos errado, digite novamente:\n")
        return get_array(n)

    for i in array:
        if(i < 1 or i > 10**9):
            print(f"Erro: parametro '{i}' invalido, digite novamente:\n")
            return get_array(n)

    return array

def get_set(m):
    '''Return a valid input set.'''

    array = get_array(m)
    disjoint_set = set(array)

    if len(disjoint_set) != m:
        print("Erro: numero de elementos diferentes errado, digite novamente:\n")
        return get_set(m)

    return disjoint_set

def calculate_hapiness(array, A, B):
    '''Calculate the hapiness with the sets and the list.'''

    hapiness = 0
    for i in array:
        for s in A:
            if s == i:
                hapiness += 1

        for s in B:
            if s == i:
                hapiness -= 1

    return hapiness

def main():
    '''main code'''

    n, m = get_nm()
    array = get_array(n)
    A = get_set(m)
    B = get_set(m)
    print(calculate_hapiness(array, A, B))

if __name__ == '__main__':
    main()
