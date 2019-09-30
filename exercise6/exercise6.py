def get_year():
    year = int(input())
    if(year < 1900 or year > 10**5):
        print("ano invalido")
        return get_year()

    return year

def leap_year(year):
    if year % 4 != 0:
        return False

    elif year % 100 == 0:
        return False

    elif year % 400 != 0:
        return False
    
    else:
        return True  


def main():
    year = get_year()
    print(leap_year(year))

if __name__ == '__main__':
    main()