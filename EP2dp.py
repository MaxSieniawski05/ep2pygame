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

