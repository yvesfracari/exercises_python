def test_marks(list_scores, name_try, student_marks):
    '''Returns if list of marks is correct.'''

    if name_try in student_marks.keys():
        print("Estudante já informado")
        return False

    if len(list_scores) != 3:
        print("Numero de notas invalido, envie apenas 3 notas")
        return False

    for score in list_scores:
        if (score < 0 or score > 100):
            print("Valor Invalido:", score)
            return False

    return True


def get_name(student_marks):
    '''Run until get a name, with a input, in student_marks dictionary.
    Returns the name.'''

    query_name = input("Qual aluno deseja saber a media acomulada?\n")

    if query_name in student_marks.keys():
        return query_name

    print("Aluno não encontrado")
    return get_name(student_marks)

def main():
    '''Main code funtion.'''

    flag = False

    while not flag:
        students = int(input("Serao informadas as notas de quantos alunos?\n"))
        if 2 <= students <= 10:
            flag = True
        else:
            print("Devem ser informado notas de 2 a 10 alunos")

    student_marks = {}

    for _ in range(students):
        flag = False

        while not flag:
            name, *line = input().split()
            scores = list(map(float, line))
            flag = test_marks(scores, name, student_marks)

        student_marks[name] = scores

    query_name = get_name(student_marks)
    mark = sum(student_marks[query_name]) / 3.0
    print(mark)

if __name__ == '__main__':
    main()
