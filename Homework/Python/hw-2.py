'''В этом задании Вам понадобится написать функцию find_substr, 
которая принимает на вход два аргумента: подстроку (любой длины) и строку, в которой нужно ее искать, 
и возвращает кортеж, представляющий собой пару [start, stop) первой позиции, где найдено слово.'''


substring = 'мы'
string = 'мама мыла раму'

def find_substr(substring, string):
    tpl = []
    for i in range(len(string) - len(substring) + 1):
        candidate = string[i:i + len(substring)]
        if candidate == substring:
            tpl.append(i)
            tpl.append(i+len(substring))
            break
    tpl = tuple(tpl)
    return tpl

find_substr(substring, string)
