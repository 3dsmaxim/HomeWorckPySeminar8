def parse_Fyrst_example(text):
    temporary_string = []
    for i in text:
        if i == '(' or i == ')' or i == '+' or i == '-' or i == '*' or i == '/':
            position = text.index(i)
            temporary_string.append(text[:position].strip(' '))
            temporary_string.append(i.strip(' '))
            text = text[position + 1:]
    temporary_string.append(text.strip(' '))

    parsed_string = []
    for i in temporary_string:
        if i != '':
            parsed_string.append(i.strip(' '))
    # print(parsed_string)
    return parsed_string


def calc(a, b, c):
    if c == '+':
        return (a + b)
    elif c == '-':
        return (a - b)
    elif c == '/':
        return (a / b)
    elif c == '*':
        return (a * b)


def example(m):
    if '(' in m:
        for i in m:
            if i == '(':
                l = (m[m.index('(')+1: m.index(')')])
                d = len(l)
                t = m.index('(')
                for i in l:
                    if i == '*' or i == '/' in l:
                        l2 = l[l.index(i)-1:l.index(i)+2]
                        k = l.index(i)-1
                        res = calc(int(l2[0]), int(l2[2]), l2[1])
                        l.pop(k)
                        l.pop(k)
                        l.pop(k)
                        l.insert(k, res)
                        res = int(l[0])
                        for i in range(1, len(l)-1, 2):
                            res = calc(res, int(l[i+1]), l[i])

                res = int(l[0])
                for i in range(1, len(l)-1, 2):
                    res = calc(res, int(l[i+1]), l[i])
                z = 0
                while z < d+2:
                    m.pop(t)
                    z += 1
                m.insert(t, res)
    else:
        res = int(m[0])
        for i in range(1, len(m)-1, 2):
            res = calc(res, int(m[i+1]), m[i])
    for i in m:
        if i == '*' or i == '/' in m:
            l2 = m[m.index(i)-1:m.index(i)+2]
            k = m.index(i)-1
            res = calc(int(l2[0]), int(l2[2]), l2[1])
            m.pop(k)
            m.pop(k)
            m.pop(k)
            m.insert(k, res)
            res = int(m[0])
            for i in range(1, len(m)-1, 2):
                res = calc(res, int(m[i+1]), m[i])
    return res
