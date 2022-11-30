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
k=[64,32,16,8,4,2,1]
print('Сумму можно выплатить:\n')
for i in k:
    num=N//i
    N=N-(num*i)
    if num!=0:
        print(f'{num} куп. : номиналом {i} \n ')
    if N==0:
        break;
