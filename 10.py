text = '  double  spaced  words  '

# можно было либо так
def reverse_words(str):
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)

# либо вообще еще проще вот так
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

# мое решение было неверно, потому что я не передавал в сплит пустую строку :фейспалм:
# поэтому пришлось выкатывать вот такую простыню, это жесть

def reverse_words(text):
    space = 0
    letter = 0
    temp = ''
    result = ''
    for i in text:
        if i == ' ':
            space += 1
        else:
            letter += 1
            temp += i
        if space > 0:
            if letter > 0:
                result += temp[::-1]
                result += ' '
                space = 0
                temp = ''
                letter = 0
            else:
                result += ' '
                space = 0
    result += temp[::-1]
    return result