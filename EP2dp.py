def transforma_base(questions):
    questions_by_level = {}  

    for question in questions:
        level = question.get('nivel')

        if level is not None:
            if level in questions_by_level:
                questions_by_level[level].append(question)
            else:
                questions_by_level[level] = [question]

    return questions_by_level

def valida_questao(questao):
    d = {}

    if 'titulo' not in questao:
        d['titulo'] = 'nao_encontrado'
    elif not questao['titulo'].strip():
        d['titulo'] = 'vazio'
    
    if 'nivel' not in questao:
        d['nivel'] = 'nao_encontrado'
    elif questao['nivel'] not in {'facil', 'medio', 'dificil'}:
        d['nivel'] = 'valor_errado'

    
    if 'opcoes' not in questao:
        d['opcoes'] = 'nao_encontrado'
    elif len(questao['opcoes']) != 4:
        d['opcoes'] = 'tamanho_invalido'
    else:
        d2 = {}
        for opcao in 'ABCD':
            if opcao not in questao['opcoes']:
                d2[opcao] = 'chave_invalida_ou_nao_encontrada'
            elif not questao['opcoes'][opcao].strip():
                d2[opcao] = 'vazia'

        if d2:
            d['opcoes'] = d2

    
    if 'correta' not in questao:
        d['correta'] = 'nao_encontrado'
    elif questao['correta'] not in 'ABCD':
        d['correta'] = 'valor_errado'

    
    if len(questao) != 4:
        d['outro'] = 'numero_chaves_invalido'

    return d