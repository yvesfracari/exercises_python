def get_runners_number():
    runners_number = int(input("Informe o numero de corredores\n"))

    if(runners_number < 2 or runners_number > 10):
        print("O numero deve ser entre 2 e 10")
        return get_runners_number()
    else:
        return(runners_number)

def get_score_list(n):
    scores = list(map(int, input("Informe os pontos\n").split()))
    
    if (not test_score_list(scores, n)):
        return get_score_list(n)

    else:
        scores.sort(reverse=True)
        runners_score = list(set(scores))
        return runners_score

def test_score_list(test_list, size):
    if(len(test_list) != size):
        print(f"Voce deve informar {size} pontos\n")
        return False

    for score in test_list:
        if (score < -100 or score > 100):
            print("Valor Invalido: Pontos devem ser entre -100 e 100")
            return False
        
    return True


def main():
    runners_number = get_runners_number()
    runners_score = get_score_list(runners_number)

    print(f"O segundo colocado fez {runners_score[1]} pontos")

if __name__ == '__main__':
    main()