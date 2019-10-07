'''Code to the exercise 9 of the MPG'''
def get_nm():
    '''Return a valid n, m input'''
    n, m = list(map(int, input().split()))

    if (n < 1 or n > 1000 or m < 1 or m > 1000):
        return get_nm()

    return n, m

def get_k(m):
    '''Return a integeer input less than m'''

    parameters = list(map(int, input().split()))

    if len(parameters) > 1:
        return get_k(m)

    k = parameters[0]
    if (k >= m or k < 0):
        return get_k(m)

    return k

def get_atlhete(m):
    '''Return avalid input line'''

    atlhete = list(map(int, input().split()))

    if len(atlhete) != m:
        return get_atlhete(m)

    for element in atlhete:
        if element > 1000:
            return get_atlhete(m)

    return atlhete

def sort_parameter(elem, k):
    '''Use to sort with the k parameter'''
    return elem[k]

def main():
    '''Main Code'''

    n, m = get_nm()
    k = get_k(m)

    atlhete_list = []

    for _ in range(n):
        atlhete_list.append(get_atlhete(m))

    atlhete_list.sort(key=lambda x: sort_parameter(x, k))

    for line in atlhete_list:
        print(line)

if __name__ == '__main__':
    main()
