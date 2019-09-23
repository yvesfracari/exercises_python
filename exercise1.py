def test_marks  (list_scores,list_names ,name_try ):
    for n in list_names: 
        if (name_try == n):
            print("Nome ja informado")
            return False

    if (len(list_scores) != 3):
            print("Numero de notas invalido, envie apenas 3 notas")
            return False

    for score in list_scores:
        if (score < 0 or score > 100):
            print("Valor Invalido:", score)
            return False
    
    return True


if __name__ == '__main__':
    flag = False

    while(not flag):
        n = int(input("Serao informadas as notas de quantos alunos?\n"))
        if (n >= 2 and n <= 10):
            flag = True

    student_marks = {}
    name_list = []
    for _ in range(n):
        flag = False

        while(not flag): 
            name, *line = input().split()
            scores = list(map(float, line))
            flag = test_marks (scores, name_list, name)

        name_list.append(name)
        student_marks[name] = scores

    query_name = input("Qual aluno deseja saber a media acomulada?\n")
    mark = sum(student_marks[query_name]) / 3.0
    print(mark)