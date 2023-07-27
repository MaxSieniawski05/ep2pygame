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
    resultado = {}

    if 'titulo' not in questao:
        resultado['titulo'] = 'nao_encontrado'
    elif not questao['titulo'].strip():
        resultado['titulo'] = 'vazio'
    
    if 'nivel' not in questao:
        resultado['nivel'] = 'nao_encontrado'
    elif questao['nivel'] not in {'facil', 'medio', 'dificil'}:
        resultado['nivel'] = 'valor_errado'

    if 'opcoes' not in questao:
        resultado['opcoes'] = 'nao_encontrado'
    elif len(questao['opcoes']) != 4:
        resultado['opcoes'] = 'tamanho_invalido'
    else:
        opcoes_invalidas = {}
        for opcao in 'ABCD':
            if opcao not in questao['opcoes']:
                opcoes_invalidas[opcao] = 'chave_invalida_ou_nao_encontrada'
            elif not questao['opcoes'][opcao].strip():
                opcoes_invalidas[opcao] = 'vazia'

        if opcoes_invalidas:
            resultado['opcoes'] = opcoes_invalidas

    if 'correta' not in questao:
        resultado['correta'] = 'nao_encontrado'
    elif questao['correta'] not in 'ABCD':
        resultado['correta'] = 'valor_errado'

    if len(questao) != 4:
        resultado['outro'] = 'numero_chaves_invalido'

    return resultado