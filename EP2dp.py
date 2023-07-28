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



def valida_questoes(lista_questoes):

    lista_nova = []

    for questao in lista_questoes:

        questao_valida = valida_questao(questao)

        if len(questao_valida) > 0:

            lista_nova.append(questao_valida)

        else:

            lista_nova.append({})

    return lista_nova



import random

def sorteia_questao(dic_nivel,nivel): 
    questao = dic_nivel[nivel]

    return random.choice(questao)

def sorteia_questao_inedita(dic, nivel, questoes_sorteadas):
    questao_sorteada = sorteia_questao(dic, nivel)

    for questao_sorteada in questoes_sorteadas:
        questao_sorteada = sorteia_questao(dic, nivel)

    questoes_sorteadas.append(questao_sorteada)

    return questao_sorteada



'''def questao_para_texto(dicio_da_questao, ide):
    print(f'----------------------------------------')
    print(f'QUESTAO {ide}')
    
    titulo = dicio_da_questao['titulo']
    print(f'\n{titulo}\n')
    
    opcoes = dicio_da_questao['opcoes']
    print('RESPOSTAS:')
    
    for letra, resposta in opcoes.items():
        print(f'{letra}: {resposta}')
        
    return '''



def questao_para_texto(dicio_da_questao, ide):
    formatada = '----------------------------------------\n'
    formatada += f'QUESTAO {ide}\n\n'
    
    titulo = dicio_da_questao['titulo']
    formatada += f'{titulo}\n\n'
    
    formatada += 'RESPOSTAS:'
    
    opcoes = dicio_da_questao['opcoes']
    for letra, resposta in opcoes.items():
        formatada += f'\n{letra}: {resposta}'
        
    return formatada




import random
def gera_ajuda(dicionario):
    lista_vazia=[]
    certa = dicionario['correta']
    for letraquestao in dicionario['opcoes']:
        if letraquestao != certa:
            lista_vazia.append(dicionario['opcoes'][letraquestao])

    dicas = random.randint(1,2)
    if dicas == 1:
        sorteia = random.choice(lista_vazia)
        return f'DICA:\nOpções certamente erradas: {sorteia}'
    if dicas == 2:
        sorteia1 = random.choice(lista_vazia)
        lista_vazia.remove(sorteia1)
        sorteia2 = random.choice(lista_vazia)
        return f'DICA:\nOpções certamente erradas: {sorteia1}|{sorteia2}'
    

quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]


while True:
    print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
    nome_do_jogador = input("qual é o seu nome?")
    print(f'Ok {nome_do_jogador}, você tem direito a pular 3 vezes e 2 ajudas!')                          
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')     










    questoes = transforma_base(quest) 
    numero = 1 

    sorteadas = []
    nivel = "facil"
    jogando = True
    lp = [1000,
5000,
10000,
30000,
50000,
100000,
300000,
500000,
1000000]
    contapulos = 3 
    contajuda = 2 
    contacertos = 0

    while True:


        questao = sorteia_questao_inedita(questoes,nivel,sorteadas)

        transformatexto = questao_para_texto(questao,numero)

        certo = questao['correta']

        while True:

            r = input('qual letra você escolhe para essa questão ?')

            if r not in ['A','B','C','D','ajuda','pular','sair']:
                print('Não aceito isso como resposta!')
            
            else:
                break 
        premio = 0 
        if r == certo:

            contacertos += 1 
            numero += 1 

            print('PARABÉNS VOCÊ ACERTOU :)')

            for i in range(len(lp)):
                k = lp[i]
                premio = k
                del(lp[i])

                if premio == 1000000:
                    print('PARABÉNS VOCÊ GANHOU :)')
                    break 
                break


            print(f'Você obteve de dinheiro {premio}')
            continue

        if r != certo: 

            if r == 'ajuda':
                while contajuda > 0:
                    contajuda  = -1 


                    print(f'Ok, vou te ajudar porém lembre-se você só tem {contajuda} ajudas')

                    print('Aperte ENTER para continuar...')


                    continuar = input('Aperte ENTER para continuar')


                

                    r = input('Qual a sua resposta?!')




        
                    if contajuda == 0: 
                        print('voce errou, acabou suas ajudas !')
                        print('Aperte ENTER para continuar...')

                        continuar = input('Aperte ENTER para continuar')

                        r = input('Qual a sua resposta?!')

               


                



    
            elif r == 'pular': 

                while contapulos > 0:

                    contapulos -= 1

                    print(f'Ok, vou pulat essa questão porém lembre-se te restam {contapulos} pulos')

                    print('Aperte ENTER para continuar...')

                    questao = sorteia_questao_inedita(questoes,nivel,sorteadas)
                    transformatexto = questao_para_texto(questao,numero)


                    r = input('Qual sua resposta')


                    continue

            
                if contapulos == 0: 
                    print('Acabou os seus pulos!')
                    print('Aperte ENTER para continuar...')

                    continuar = input('Aperte ENTER caso queira continuar')

                    r = input('Qual sua resposta')
            

            elif r == "sair":
                print(f'Os seus ganhos foram de {k}')
                break 
            else:
                print('Você perdeu tudo, não ganha nada!')
                break 
        
        


        


            

