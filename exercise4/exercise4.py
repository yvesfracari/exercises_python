'''Description in the readme file.'''

def get_parameters():
    '''Return valid n, m input paramters'''
    n_limit = 10**5
    m_limit = 10**14

    parameters = list(map(int, input().split()))
    n = parameters[0]
    m = parameters[1]


    if(n < 2 or n > n_limit or m < 1 or m > m_limit):
        print("Erro: Parametros invalidos")
        return get_parameters()
    
    return n,m

def get_array(n):
    '''Return a array in length n'''

    a_limit = 10**18
    a = list(map(int, input().split()))

    if len(a) != n:
        print("Erro: numero errado de parametros")
        return get_array(n)

    for i in a:
        if(i < 1 or i > a_limit):
            print("Erro: parametros invalidos")
            return get_array(n)

    return a

def maximum_sum(a, m, start, end, max_value):
    '''Return a max module of 'm' in the sum of
    a subarray in the subarray a['start:end'].'''

    if end == len(a): 
        return max_value

    if start > end: 
        return maximum_sum(a, m, 0, end + 1, max_value) 
          
    else: 
        sub_array = a[start:end + 1]
        value = sum(sub_array) % m
        
        if(value > max_value):
            max_value = value
        
        return maximum_sum(a, m, start + 1, end, max_value)
     
def main():
    '''main code.'''

    n,m = get_parameters()
    a = get_array(n)
    max_value = maximum_sum(a, m, 0, 0, 0)

    print(max_value)

if __name__ == '__main__':
    main()
