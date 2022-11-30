def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n
N = - 1
while N == -1:
    N = int(input('Введите натуральное число:\n'))
    N = errorCheck(N)
    if N<=0:
        print('Ошибка! Необходимо ввести натуральное число\n')
        N=-1
