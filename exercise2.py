def get_runners_number():
    runner_number = int(input("Informe o numero de corredores\n"))
    if(runner_number < 2 or runner_number > 10):
        print("O numero deve ser entre 2 e 10")
        return get_runners_number()
    else:
        return(runner_number)

def get_score_list():
    scores = list(map(int, input("Informe os pontos\n").split()))
    
    if (not test_score_list(scores, runners_number)):
        return get_score_list()

    else:
        return scores

def test_score_list(test_list, size):
    if(len(test_list) != size):
        print(f"Voce deve informar {size} pontos\n")
        return False

    for score in test_list:
        if (score < -100 or score > 100):
            print("Valor Invalido: Pontos devem ser entre -100 e 100")
            return False
        
    return True


if __name__ == '__main__':
    runners_number = get_runners_number()

    
    runners_score = get_score_list()
    runners_score.sort(reverse=True)
    print(f"O vencedor fez {runners_score[1]} pontos")