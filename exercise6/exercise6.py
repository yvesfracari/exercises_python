'''Get's a input year and print if is leap year'''

def get_year():
    '''Return a valid input year'''

    year = int(input())

    if(year < 1900 or year > 10**5):
        print("ano invalido")
        return get_year()

    return year

def leap_year(year):
    '''return if year is a leap_year'''

    if year % 4 != 0:
        return False

    if year % 100 == 0:
        return False

    if year % 400 != 0:
        return False

    return True

def main():
    '''Main function.'''

    year = get_year()
    print(leap_year(year))

if __name__ == '__main__':
    main()
