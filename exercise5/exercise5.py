import math

def get_parameters():
    parameters = list(map(int, input().split()))
    k = parameters[0]
    m = parameters[1]

    if(k < 1 or k > 7 or m < 1 or m > 1000):
        print("parametros invalidos")
        return get_parameters()
    
    else:
        return(k, m)

def get_list():
    list_i = list(map(int, input().split()))

    n = list_i.pop(0)

    if (n < 1 or n > 7):
        print("numero de valores errados")
        return get_list()
    
    elif (len(list_i) != n):
        print("numero de valores errados")
        return get_list()
    
    else:
        for i in list_i:
            if (i > 10**9 or (i < 1 and i > -1) or i < -10**9):
                print("valores invalidos")
                return get_list()
    return list_i

def get_max(list_i):
    list_s = []
    
    for i in list_i:
        x = math.fabs(i)
        list_s.append(x)
    
    list_s.sort(reverse=True)
    return list_s[0]

def calculate_module(list_s, m):
    s = 0
    for i in list_s:
        s = s + (i**2)
    
    return s % m

def main():
    k,m = get_parameters()
    list_s = []

    for _ in range(k):
        list_i = get_list()
        list_s.append(get_max(list_i))
    
    module = calculate_module(list_s, m)
    print(module)

    return

if __name__ == '__main__':
    main()