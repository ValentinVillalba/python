def solution(s):
    result = []
    #LOS PARAMETROS SE PUEDEN EDITAR Y QUEDAN GUARDADOS
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2): #EN RANGE TAMBIEN SE PUEDE HACER DESDE, HASTA Y PASO
        result.append(s[i:i+2])
    return result

print(solution("jaeiogaio"))
